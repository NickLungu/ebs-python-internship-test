from drf_util.decorators import serialize_decorator
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.blog.models import Category, Blog, Comment
from apps.blog.serializers import CategorySerializer, BlogSerializer, CommentSerializer
from apps.common.permissions import ReadOnly


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (AllowAny, )

    def get(self, request):
        blogs = Blog.objects.all()
        return Response(BlogSerializer(blogs, many=True).data)


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (AllowAny, )

    def get(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(pk=pk))
        comments = get_object_or_404(Comment.objects.filter(blog=blog))
        data = BlogSerializer(blog).data
        data['comments'] = CommentSerializer(comments).data
        return Response(data)


class AddBlogView(GenericAPIView):
    serializer_class = BlogSerializer

    permission_classes = (AllowAny, )
    authentication_classes = ()

    @serialize_decorator(BlogSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        blog = Blog.objects.create(
            **validated_data,
        )

        blog.save()

        return Response(BlogSerializer(blog).data)


class AddCommentView(GenericAPIView):
    serializer_class = CommentSerializer

    permission_classes = (AllowAny, )
    authentication_classes = ()

    @serialize_decorator(CommentSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        comment = Comment.objects.create(
            **validated_data,
        )

        comment.save()

        return Response(CommentSerializer(comment).data)