from django.contrib import admin
from django.urls import path
from itnext.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('it_shop/', product_list, name='it_shop'),
    path('about/', about, name='about'),
    path('blog_list/',blog_list, name='blog_list'),
    path('search/',SearchResultsView.as_view(),name = 'search'),
    path('blog_grid/', blog_grid, name ='blog_grid'),
    path('it_blog_detail.html/', blog_detail, name ='blog_detail'),
    path('service/', service, name = 'service'),


    # path('service_list/', )
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

