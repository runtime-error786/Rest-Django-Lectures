# from rest_framework.pagination import PageNumberPagination

# class MY_page(PageNumberPagination):
#     page_size = 2
#     max_page_size=4


from rest_framework.pagination import LimitOffsetPagination

class MY_page(LimitOffsetPagination):
    default_limit = 3
    max_limit = 5