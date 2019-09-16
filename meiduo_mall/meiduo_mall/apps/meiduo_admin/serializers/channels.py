from rest_framework import serializers

from goods.models import GoodsChannel, GoodsChannelGroup, GoodsCategory


class ChannelSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(label='一级分类名称')
    group = serializers.StringRelatedField(label='频道组ID')
    category_id = serializers.IntegerField(label='一级分类ID')
    group_id = serializers.IntegerField(label='频道组ID')

    class Meta:
        model = GoodsChannel
        exclude = ('create_time', 'update_time')

    def validate_category_id(self, value):
        try:
            GoodsCategory.objects.get(id=value, parent=None)
        except GoodsCategory.DoesNotExist as e:
            raise serializers.ValidationError('一级分类不存在')
        return value

    def validate_group_id(self, value):
        try:
            GoodsCategory.objects.get(id=value, parent=None)
        except GoodsChannelGroup.DoesNotExist as e:
            raise serializers.ValidationError('频道组不存在')
        return value


class ChannelGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsChannelGroup
        fields = ('id', 'name')


class ChannelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ('id', 'name')
