from rest_framework import viewsets, mixins


class ListCreateViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                        mixins.CreateModelMixin):
    pass
