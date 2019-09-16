


from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from meiduo_admin.serializers.users import AdminAuthSerializer, UserSerializer


# POST /meiduo_admin/authorizations/
from users.models import User


class AdminAuthorizeView(APIView):
    def post(self,request):
        serializer = AdminAuthSerializer(data = request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()


        return Response(serializer.data,status=status.HTTP_201_CREATED)


class UserInfoView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class =UserSerializer


    # 重写查询集
    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword:
            # 搜索
            users = User.objects.filter(is_staff=False, username__contains=keyword)
        else:
            users = User.objects.all()
        return  users



