from rest_framework.pagination import PageNumberPagination

class MY_page(PageNumberPagination):
    page_size = 2
    max_page_size=4