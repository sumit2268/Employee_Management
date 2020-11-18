from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination


class ListLimitoffsetPagination(LimitOffsetPagination):
    max_limit=10
    default_limit=5