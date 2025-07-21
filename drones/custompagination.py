from rest_framework.pagination import LimitOffsetPagination

class LimitOffsetPaginationWithUpperBound(LimitOffsetPagination):
    max_limit = 8 # Set the maximum limit value to 8
