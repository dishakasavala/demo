"""
URL configuration for project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import *
from adminapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index),
    path('about/',about),
    path('blog/',blog),
    path('contact/',contactp),
    path('shop/',shop),
    path('single_post/',singlepost),
    path('style/',styles),
    path('thank_you/',thankyou),
    path('blog_masonry/',blogmasony),
    path('blog_sidebar/',blogsidebar),
    path('cart/',cartp),
    path('checkout/',checkout),
    path('coming_soon/',comingsoon),
    path('error/',error),
    path('faqs/',faqs),
    path('login_admin/',loginadmin),
    path('shop_grid/',shpogrid),
    path('shop_list/',shoplist),
    path('shop_slider/',shopslider),
    path('wishlist/',wishlist),
    path('single_product/<int:p_id>/',singleproduct),


    ## webapp urls
    path('login/',loginpage),
    path('enter/',enterpage),
    path('data/',datapage),
    path('logout/',logout),
    # slider
    path('slider/',sliderpage),
    path('tables/',slidertable),
    path('edit-slider/<int:sed_id>',editslider),
    path('delete-slider/<int:sdel_id>',deleteslider),
    ## mcatagory
    path('cat_table/',cattable),
    path('add_catagory/',addcatagory),
    path('edit_cat/<int:ced_id>',editcat),
    path('del_cat/<int:cdel_id>',delcat),
    ##category
    path('category_table/',catetable),
    path('add_category/',addcategory),
    path('edit_category/<int:caed_id>',editcate),
    path('delete_category/<int:cadel_id>',delcate),
    ##product
    path('product_table/',producttable),
    path('add_product/',addproduct),
    path('edit_product/<int:proed_id>',editproduct),
    path('delete_product/<int:prodel_id>',delproduct),

    path('cart_table',carttable),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
