from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from goods.models import SKUImage, SKU
from meiduo_admin.serializers.skus import SKUImageSerializer, SKUSimpleSerializer


class SKUImageViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    lookup_value_regex = '\d+'
    queryset = SKUImage.objects.all().order_by('-create_time')
    serializer_class = SKUImageSerializer



class SKUSimpleView(ListAPIView):
    # 指定视图所使用的查询集
    queryset = SKU.objects.all()

    # 指定视图所使用的序列化器类
    serializer_class = SKUSimpleSerializer

    # 注：关闭分页
    pagination_class = None

