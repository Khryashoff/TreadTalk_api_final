from django.shortcuts import get_object_or_404

from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from posts.models import Group, Post

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (GroupSerializer, PostSerializer,
                             CommentSerializer, FollowSerializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Набор представлений для работы с группами.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для работы с постами.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """
        Создает новый пост и сохраняет информацию об авторе поста.
        """
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для обработки комментариев, связанных с постом.
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        """
        Возвращает queryset, который содержит все комментарии,
        связанные с определенным постом.
        """
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        """
        Создает новый комментарий, связанный с определенным постом.
        """
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Набор представлений для работы с подписками.
    """
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('following__username',)

    def get_queryset(self):
        """
        Возвращает queryset всех подписчиков текущего пользователя.
        """
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """
        Сохраняет объект подписки текущего пользователя.
        """
        serializer.save(user=self.request.user)
