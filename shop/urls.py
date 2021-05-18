
from django.urls import path

from . import views
urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("product/<int:myid>",views.prodectView,name="ProductView"),
    path("about/",views.about,name="About"),
    path("contact/",views.contact,name="Contact"),
]
