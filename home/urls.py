from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "home"

urlpatterns = [
    path('home',views.home, name="home"),
    path('order',views.order, name="order"),
    path('report',views.report, name="report"),
    path('success_order',views.success_order, name="success_order"),
    path('payment_option',views.payment_option, name="payment_option"),
    path('estimate',views.estimate, name="estimate"),
    path('registration',views.UserMasterTable, name="registration"),
    path('curior-close',views.curior_close, name="curior-close"),
    path('update_distict',views.get_district, name="update_distict"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('service',views.service, name="service"),
    path('',views.login1, name="login"),
    path('login',views.login),
    path('admin',views.admin),
    path('citysave',views.citysave),
    path('city',views.city),
    path('cityedit/<int:id>',views.cityedit),
    path('getState/<int:id>/', views.getState, name='getState'),
    # path('cityupdate/<int:id>',views.cityupdate),
    path('citydelete/<int:id>',views.citydelete),
    path('cityView',views.cityView,name="cityView"),
    path('gst',views.gst),
    path('gstsave',views.gstsave),
    path('gstedit/<int:id>',views.gstedit),
    # path('gstupdate/<int:id>',views.gstupdate),
    path('gstdelete/<int:id>',views.gstdelete),
    path('gstView',views.gstView,name='gstView'),
    path('dist',views.dist),
    path('distsave',views.distsave),
    path('distedit/<int:id>',views.distedit),
    # path('distupdate/<int:id>',views.distupdate),
    path('distdelete/<int:id>',views.distdelete),
    path('distView',views.distView,name="cityView"),
    path('doc',views.doc),
    path('docsave',views.docsave),
    path('docedit/<int:id>',views.docedit),
    path('docupdate/<int:id>',views.docupdate),
    path('docdelete/<int:id>',views.docdelete),
    path('docView',views.docView,name="docView"),
    path('veh',views.veh),
    path('vehsave',views.vehsave),
    path('vehedit/<int:id>',views.vehedit),
    # path('vehupdate/<int:id>',views.vehupdate),
    path('vehdelete/<int:id>',views.vehdelete),
    path('vehView',views.vehView,name="vehView"),
    path('vehrout',views.vehrout),
    path('vehroutsave',views.vehroutsave),
    path('vehroutedit/<int:id>',views.vehroutedit),
    path('vehroutupdate/<int:id>',views.vehroutupdate),
    path('vehroutdelete/<int:id>',views.vehroutdelete),
    path('vehroutView',views.vehroutView,name="vehroutView"),
    path('user',views.user),
    path('usersave',views.usersave),
    path('useredit/<int:id>',views.useredit),
    # path('userupdate/<int:id>',views.userupdate),
    path('userdelete/<int:id>',views.userdelete),
    path('userView',views.userView,name="userView"),
    path('review',views.review),
    path('reviewsave',views.reviewsave),
    path('reviewedit/<int:id>',views.reviewedit),
    # path('reviewupdate/<int:id>',views.reviewupdate),
    path('reviewdelete/<int:id>',views.reviewdelete),
    path('reviewView',views.reviewView,name="reviewView"),
    path('stateadd',views.stateadd),
    path('statesave',views.statesave),
    path('stateView',views.stateView),
    path('stateedit/<int:id>',views.stateedit),
    path('stateupdate/<int:id>',views.stateupdate),
    path('statedelete/<int:id>',views.statedelete),
    path('complain',views.complain),
    path('complainsave',views.complainsave),
    path('complainView',views.complainView),
    path('complainedit/<int:id>',views.complainedit),
    # path('complainupdate/<int:id>',views.complainupdate),
    path('complaindelete/<int:id>',views.complaindelete),
    path('complainstatus',views.complainstatus),
    path('complainstatussave',views.complainstatussave),
    path('complainsView',views.complainsView),
    path('complainstatusedit/<int:id>',views.complainstatusedit),
    # path('complainstatusupdate/<int:id>',views.complainstatusupdate),
    path('complainstatusdelete/<int:id>',views.complainstatusdelete),
    path('docdetail',views.docdetail),
    path('docdetsave',views.docdetsave),
    path('docdetView',views.docdetView),
    path('docdetedit/<int:id>',views.docdetedit),
    path('docdetupdate/<int:id>',views.docdetupdate),
    path('docdetdelete/<int:id>',views.docdetdelete),
    path('docvehdet',views.docvehdet),
    path('docvehdetsave',views.docvehdetsave),
    path('docvehdetView',views.docvehdetView),
    path('docvehdetedit/<int:id>',views.docvehdetedit),
    path('docvehdetupdate/<int:id>',views.docvehdetupdate),
    path('docvehdetdelete/<int:id>',views.docvehdetdelete),
    path('reviewstatus',views.reviewstatus),
    path('reviewstatussave',views.reviewstatussave),
    path('reviewstatusView',views.reviewstatusView),
    path('reviewstatusedit/<int:id>',views.reviewstatusedit),
    path('reviewstatusupdate/<int:id>',views.reviewstatusupdate),
    path('reviewstatusdelete/<int:id>',views.reviewstatusdelete),
    path('payment',views.payment),
    path('paymentsave',views.paymentsave),
    path('paymentView',views.paymentView),
    path('paymentedit/<int:id>',views.paymentedit),
    # path('paymentupdate/<int:id>',views.paymentupdate),
    path('paymentdelete/<int:id>',views.paymentdelete),
    path('userdet',views.userdet),
    path('userdetsave',views.userdetsave),
    path('userdetView',views.userdetView),
    path('userdetedit/<int:id>',views.userdetedit),
    path('userdetupdate/<int:id>',views.userdetupdate),
    path('userdetdelete/<int:id>',views.userdetdelete),
    path('vehroutdet',views.vehroutdet),
    path('vehroutdetsave',views.vehroutdetsave),
    path('vehroutdetView',views.vehroutdetView),
    path('vehroutdetedit/<int:id>',views.vehroudetedit),
    path('vehroutdetupdate/<int:id>',views.vehroutdetupdate),
    path('vehroutdetdelete/<int:id>',views.vehroutdetdelete),
    path('product',views.product),
    path('newadmin',views.newadmin),
    path('customerpanel',views.customerpanel),
]