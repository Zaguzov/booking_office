from django.urls import path

from . import views

urlpatterns = [
    path('500/', views.server_error, name='server_error'),
    path('404/', views.page_not_found, name='page_not_found'),
    path('', views.index, name='index'),
    path('kind/<str:name>/', views.kind_events, name='kind'),
    path('event/<int:event_id>/', views.event_view, name='event'),
    path('location/<str:name>/', views.location_view, name='location'),
    path('artist/<str:initials>/', views.artist_view, name='artist'),
    path('kinds/', views.kinds_view, name='kinds'),
    path('shoppingcart/', views.shopping_cart_view, name='shopping_cart'),
    path('add_to_shopping_cart/<int:event_id>/', views.add_to_shopping_cart,
         name='add_to_shopping_cart'),
    path('delete_from_shopping_cart/<int:shopping_cart_id>/',
         views.delete_from_shopping_cart,
         name='delete_from_shopping_cart'),
]