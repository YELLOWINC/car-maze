from django.conf.urls import url, include
from cars import views

urlpatterns = [
    url(r'^login/$', views.user_login),
    url(r'^logout/$', views.user_logout),
    url(r'^register/$', views.register),
    url(r'^search/', views.search_form),
    url(r'^search-results/$', views.search),
    url(r'^search-by-type/$', views.search_type),
    url(r'^search-by-type-results/', views.search_type_results),
    url(r'^cars/(?P<manufacturer>[\w\-]+)/(?P<slug>[\w-]+)/$', views.car_details),
    url(r'^search-price-range/', views.search_price_range),
    url(r'^dealer-admin/', views.dealer_admin),
    url(r'^dealer-approve/$', views.dealer_approve),
    url(r'^wishlist/$', views.wishlist_display),
    url(r'^dealer-login/$', views.dealer_login),
    url(r'^about/$', views.about),
]