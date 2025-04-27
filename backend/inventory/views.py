from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Supplier, Item
from .serializers import CategorySerializer, SupplierSerializer, ItemSerializer
from django.db.models import Sum, Avg, Count
from django.db.models import F

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # Custom action untuk ringkasan stok
    @action(detail=False, methods=['get'])
    def stock_summary(self, request):
        total_stock = Item.objects.aggregate(Sum('stock'))['stock__sum'] or 0
        total_value = Item.objects.aggregate(total_value=Sum(F('price') * F('stock')))['total_value'] or 0
        avg_price = Item.objects.aggregate(Avg('price'))['price__avg'] or 0
        return Response({
            "total_stock": total_stock,
            "total_value": total_value,
            "average_price": avg_price
        })

    # Custom action untuk barang stok di bawah ambang
    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        threshold = int(request.query_params.get('threshold', 5))  # default 5
        low_stock_items = Item.objects.filter(stock__lt=threshold)
        serializer = self.get_serializer(low_stock_items, many=True)
        return Response(serializer.data)

    # Custom action untuk laporan per kategori
    @action(detail=False, methods=['get'])
    def report_by_category(self, request):
        data = []
        for category in Category.objects.all():
            items = Item.objects.filter(category=category)
            total_value = sum([item.price * item.stock for item in items])
            avg_price = items.aggregate(Avg('price'))['price__avg'] or 0
            data.append({
                "category": category.name,
                "total_items": items.count(),
                "total_value": total_value,
                "average_price": avg_price,
            })
        return Response(data)

    # Custom action untuk laporan per supplier
    @action(detail=False, methods=['get'])
    def report_by_supplier(self, request):
        data = []
        for supplier in Supplier.objects.all():
            items = Item.objects.filter(supplier=supplier)
            total_value = sum([item.price * item.stock for item in items])
            data.append({
                "supplier": supplier.name,
                "total_items": items.count(),
                "total_value": total_value,
            })
        return Response(data)

    # Custom action untuk ringkasan keseluruhan
    @action(detail=False, methods=['get'])
    def system_summary(self, request):
        total_items = Item.objects.count()
        total_value = sum([item.price * item.stock for item in Item.objects.all()])
        total_categories = Category.objects.count()
        total_suppliers = Supplier.objects.count()
        return Response({
            "total_items": total_items,
            "total_stock_value": total_value,
            "total_categories": total_categories,
            "total_suppliers": total_suppliers
        })
