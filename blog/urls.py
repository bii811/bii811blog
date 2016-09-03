from django.conf.urls import url
from . import views
from blog.views import PostListView, PostDetailView


urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    ]