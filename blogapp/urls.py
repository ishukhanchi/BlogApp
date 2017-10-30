from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$',views.index,name='index'),
url(r'^addblog$', views.AddBlog.as_view(), name='add_blog'),
url(r'^detail/(?P<blog_id>[0-9]+)$',views.detail,name='detail'),
]