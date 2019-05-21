from django.urls import path

from . import views

app_name = 'Hotelapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<food_id>[0-9]+)/', views.detail, name='detail'),
    path('(?P<food_id>[0-9]+)/order', views.final, name='final'),
    path('(?P<food_id>[0-9]+)/add_item', views.add_item, name='add_item'),
    path('(?P<food_id>[0-9]+)/cancel_order/(?P<item_id>[0-9]+)/', views.cancel_order, name='cancel_order'),

]