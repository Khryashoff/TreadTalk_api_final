from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


from posts.models import Group, Post, Comment, Follow, User


class GroupSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Group.
    """
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Post.
    """
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Comment.
    """
    author = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Follow.
    """
    user = SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы не можете подписаться на себя.'
            )
        ]

    def validate_following(self, data):
        """
        Проверяет, что пользователь не подписывается сам на себя.
        """
        if self.context.get('request').user == data:
            raise serializers.ValidationError(
                'Вы не можете подписаться на себя.'
            )
        return data
