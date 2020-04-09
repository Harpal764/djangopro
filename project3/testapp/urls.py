from django.urls import path
from . import views

urlpatterns = [
   # path('', views.test_view1,name='test_view1'),
    path('', views.test_view2,name='test_view2'),
    path('', views.test_view3,name='test_view3'),
    path('', views.test_view4,name='test_view4'),

]