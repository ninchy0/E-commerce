from django.urls import path
from .views import *
app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', CategoryItemView.as_view(), name='category'),
    path('item_detail/<slug>', ItemDetailView.as_view(), name='item_detail'),
    path('search', ItemSearchView.as_view(), name='search'),
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('api_data', api_data, name='api_data'),
]
