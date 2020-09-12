from django.contrib import admin
from django.urls import path

from vendor.views import apitry
from vendor.postorders import insertorders
from vendor.findbystoreid import findbystore
from vendor.storeandcategory import storeandcategory
urlpatterns = [
    path('admin/', admin.site.urls),
    path('grocerySOS/insert/orders',insertorders),
    path('grocerySOS/Store/1.0.1-oas3/store/card/findByFranchise', apitry),
    path('grocerySOS/Product/1.0.0/Product/findCategoriesByStore', findbystore),
    path('grocerySOS/Product/1.0.0/Product/findByCategoryAndStore',storeandcategory)
]
