from rest_framework import viewsets, mixins


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """
    Класс представления DRF, содержащий методы для создания новых объектов и
    получения списка объектов.
    """
