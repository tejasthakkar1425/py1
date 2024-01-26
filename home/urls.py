from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "home"

urlpatterns = [
    #path('',views.home, name="home"),
    #path('about',views.about, name="about"),
    #path('contact',views.contact, name="contact"),
    #path('service',views.service, name="service"),
    #path('login',views.login, name="login"),
    path('citysave',views.citysave),
    path('city',views.city),
    path('cityedit/<int:id>',views.cityedit),
    path('cityupdate/<int:id>',views.cityupdate),
    path('citydelete/<int:id>',views.citydelete),
    path('cityView',views.cityView,name="cityView"),
    path('gst',views.gst),
    path('gstsave',views.gstsave),
    path('gstedit/<int:id>',views.gstedit),
    path('gstupdate/<int:id>',views.gstupdate),
    path('gstdelete/<int:id>',views.gstdelete),
    path('gstView',views.gstView,name='gstView'),
    path('dist',views.dist),
    path('distsave',views.distsave),
    path('distedit/<int:id>',views.distedit),
    path('distupdate/<int:id>',views.distupdate),
    path('distdelete/<int:id>',views.distdelete),
    path('distView',views.distView,name="cityView"),
    path('docView',views.docView,name="docView"),
    path('vehView',views.vehView,name="vehView"),
    path('vehroutView',views.vehroutView,name="vehroutView"),
    path('user',views.user),
    path('usersave',views.usersave),
    path('userView',views.userView,name="userView"),
    path('reviewView',views.reviewView,name="reviewView"),
    path('stateadd',views.stateadd),
    path('statesave',views.statesave),
    path('stateView',views.stateView),
    path('stateedit/<int:id>',views.stateedit),
    path('stateupdate/<int:id>',views.stateupdate),
    path('statedelete/<int:id>',views.statedelete),
]