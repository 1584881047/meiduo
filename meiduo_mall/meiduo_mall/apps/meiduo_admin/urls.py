from django.conf.urls import url

from meiduo_admin.views import users, statistical, channels, skus
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^authorizations/$', users.AdminAuthorizeView.as_view()),
    url(r'^statistical/total_count/$', statistical.UserTotalCountView.as_view()),
    url(r'^statistical/day_increment/$', statistical.UserDayIncrementView.as_view()),
    url(r'^statistical/day_active/$', statistical.UserDayActiveView.as_view()),
    url(r'^statistical/day_orders/$', statistical.UserDayOrdersView.as_view()),
    url(r'^statistical/month_increment/$', statistical.UserMonthCountView.as_view()),
    url(r'^statistical/goods_day_views/$', statistical.GoodsDayView.as_view()),
    url(r'^users/$', users.UserInfoView.as_view()),
    url(r'^goods/channel_types/$', channels.ChannelTypesView.as_view()),
    url(r'^goods/categories/$', channels.ChannelCategoriesView.as_view()),
    url(r'^skus/simple/$', skus.SKUSimpleView.as_view()),
]
router = DefaultRouter()
router.register('goods/channels', channels.ChannelViewSet, base_name='channels')
urlpatterns += router.urls

router = DefaultRouter()
router.register(r'skus/images', skus.SKUImageViewSet, base_name='images')
urlpatterns += router.urls
