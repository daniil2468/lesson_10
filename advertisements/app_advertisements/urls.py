from django.urls import path
from .views import index, top_sellers, advertisement_post, advertisement_datail

urlpatterns = [
    path('', index, name='main-page'),
    path('adertisement-post/', advertisement_post, name='adv-post'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement/<int:pk>', advertisement_datail, name='adv-datail')

]