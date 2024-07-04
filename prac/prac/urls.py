# """
# URL configuration for prac project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """

# from django.contrib import admin
# from django.urls import path
# from api import views
# from rest_framework.routers import DefaultRouter
# from django.urls import include
# router = DefaultRouter()

# router.register("stuapi",views.Student_View,basename="student")

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('stu/', views.Student_View.as_view()),
#     # path('stu/<int:pk>/', views.Student_View1.as_view())
#     # path('stu/<int:pk>/', views.Student_View.as_view())
#     # path('stu/', views.Student_View),
#     path('',include(router.urls))
# ]


# urls.py
from django.urls import path, include
from api.views import RegisterView, CustomTokenObtainPairView,CustomTokenRefreshView
from rest_framework.routers import DefaultRouter
from api.views import CustomUserViewSet
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]

