from django.utils import timezone
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.models import GoodsVisitCount
from meiduo_admin.serializers.statistical import GoodsVisitSerializer
from users.models import User


class UserTotalCountView(APIView):
    # 添加权限校验
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        获取用户数量
        :param request:
        :return:
        """
        count = User.objects.count()
        return Response({
            'date': timezone.now(),
            'count': count
        })


class UserDayIncrementView(APIView):
    # 添加权限校验
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        获取今日用户访问数量
        :param request:
        :return:
        """
        now_time = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        # 用户创建时间大于等于  今天的0点
        count = User.objects.filter(date_joined__gte=now_time).count()

        return Response({
            'date': timezone.now(),
            'count': count
        })


class UserDayActiveView(APIView):
    # 添加权限校验
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        今日活跃用户
        :param request:
        :return:
        """
        now_time = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        count = User.objects.filter(last_login__gte=now_time).count()
        return Response({
            'date': timezone.now(),
            'count': count
        })


class UserDayOrdersView(APIView):
    # 添加权限校验
    permission_classes = [IsAdminUser]

    def get(self, request):
        """获取今日下单用户数量"""
        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)

        # 订单创建的时间 >= 今天 的用户  去重 的数量
        count = User.objects.filter(orders__create_time__gte=now_date).distinct().count()
        return Response({
            'date': timezone.now(),
            'count': count
        })


class UserMonthCountView(APIView):
    # 添加权限校验
    permission_classes = [IsAdminUser]

    # 获取30天日增长用户
    def get(self, request):
        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)

        # 开始时间
        begin_data = now_date - timezone.timedelta(days=29)
        data_list = []
        while begin_data <= now_date:
            count = User.objects.filter(date_joined__gte=begin_data,
                                        date_joined__lt=begin_data + timezone.timedelta(days=1)).count()
            data_list.append({
                'count': count,
                'date': begin_data.date()
            })

            begin_data += timezone.timedelta(days=1)

        return Response(data_list)


class GoodsDayView(APIView):
    permission_classes = [IsAdminUser]

    # 日分类商品访问量
    def get(self, request):
        now_time = timezone.now().date()
        goods_visit = GoodsVisitCount.objects.filter(date=now_time)
        serializer = GoodsVisitSerializer(goods_visit, many=True)
        return Response(serializer.data)
