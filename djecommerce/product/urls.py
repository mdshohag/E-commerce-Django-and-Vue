from django.urls import re_path

from product import views

urlpatterns = [
    re_path('latest-products/', views.LatestProductsList.as_view()),

   #re_path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
  
   # re_path(r'^(?P<category_slug>[-\w]+)/$', views.CategoryDetail.as_view()),
    re_path(r'^products/(?P<category_slug>\w+)/$',  views.CategoryDetail.as_view()),



#re_path(r'^products/(?P<category_slug>\d+)/(?P<product_slug>\d+)/', views.ProductDetail.as_view()),

    
    # re_path(r'^(?P<slug>[0-9-a-z]+)$', views.ProductDetail.as_view()),
   # path("<slug:category_slug>/<slug:series_slug>/<int:tutorial_id>/", views.episode_blocks, name="episode_blocks"),
     

   # re_path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    #re_path(r'^products/(?P<category_slug>[0-9]{4})/(?P<product_slug>[0-9]{2})/(?P<slug>[\w-]+)/$', views.ProductDetail.as_view()),
    #re_path('<path:cat_slug><slug:prod_slug>/', views.ProductDetail.as_view()),

    # re_path(r'^products/(?P<category_slug>[0-9]{4})/(?P<product_slug>[0-9]{2})/(?P<slug>[\w-]+)/$', views.ProductDetail.as_view()),
    #re_path(r'^(?P<products>\w+)/(?P<category_slug>\w+)/(?P<product_slug>\w+)/$', views.ProductDetail.as_view()),
]