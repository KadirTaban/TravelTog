from django.urls import path
from .views import MainFlowView, MyGalleryView


urlpatterns=[
    path('api/myGallery',MyGalleryView.as_view(), name="all-post"),
    path('api/home',MainFlowView.as_view())
] 