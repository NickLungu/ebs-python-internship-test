from django.urls import path

from apps.blog.views import CategoryViewSet, BlogListView, BlogItemView, AddBlogView, AddCommentView
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(
    r"categories",
    CategoryViewSet,
    basename="category",
)

urlpatterns = router.urls

urlpatterns += [
    path("blog", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>", BlogItemView.as_view(), name="blog_item"),
    path("addblog", AddBlogView.as_view(), name="blog_add"),
    path("addcomment", AddCommentView.as_view(), name="comment_add"),
]
