
from django.urls.conf import path
from . import views
urlpatterns=[
    path('',views.login,name="login"),
    path('home',views.home,name="home"),
    path('logout',views.logout,name='logout')
]