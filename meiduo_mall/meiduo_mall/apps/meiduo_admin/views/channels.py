from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from goods.models import GoodsChannel, GoodsChannelGroup, GoodsCategory
from meiduo_admin.serializers.channels import ChannelSerializer, ChannelGroupSerializer, ChannelCategorySerializer


class ChannelViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ChannelSerializer
    queryset = GoodsChannel.objects.all()
    lookup_value_regex = '\d+'


class ChannelTypesView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ChannelGroupSerializer
    queryset = GoodsChannelGroup.objects.all()
    pagination_class = None




class ChannelCategoriesView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ChannelCategorySerializer
    queryset = GoodsCategory.objects.all()
    pagination_class = None
