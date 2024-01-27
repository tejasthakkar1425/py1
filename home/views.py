from sre_parse import State
from django.shortcuts import redirect, render
from django.http import HttpResponse
from home.models import *
from home.forms import *

""""
def home(request):
    return render(request, "authentication/index.html")

def about(request):
    return render(request, "authentication/about.html")

def contact(request):
    return render(request, "authentication/contact.html")

def service(request):
    return render(request, "authentication/service.html")

def login(request):
    return render(request, "authentication/login.html")
"""

def stateadd(request):
    stateobj=StateMasterTable.objects.all()
    print(stateobj)
    return render(request, "authentication/stateadd.html",{'stateobj':stateobj})

def statesave(request):
    id=request.POST.get('txtsid')
    name=request.POST.get('txtsname')
    desc=request.POST.get('txtdesc')
    #cbui=request.POST.get('txtuser')
    #cd=request.POST.get('txtuserdate')
    #ubui=request.POST.get('txtupdate')
    #ud=request.POST.get('txtup')
    state=StateMasterTable(state_id=id,stat_name=name,description=desc)#(created_by_user=cbui,created_date=cd,updated_by_user=ubui,updated_date=ud)
    state.save()
    return redirect("/stateView")

def stateView(request):
    objStateMaster = StateMasterTable.objects.all()
    print(objStateMaster)
    return render(request, "authentication/state-list.html",{'stateobj':objStateMaster})

def stateedit(request,id):
    state=StateMasterTable.objects.get(state_id=id)
    return render(request, "authentication/stateedit.html",{"state":state})

def stateupdate(request,id):
    if request.method=="POST":
        state=StateMasterTable.objects.get(state_id=id)
        sname=request.POST.get('txtname')
        sdesc=request.POST.get('txtsdesc')
        #cbui=request.POST.get('txtuser')
        #cd=request.POST.get('txtuserdate')
        #ubui=request.POST.get('txtupdate')
        #ud=request.POST.get('txtup')
        state.stat_name=sname
        state.description=sdesc
        #state.created_by_user=cbui
        #state.created_date=cd
        #state.updated_by_user=ubui
        #state.updated_date=ud
        state.save()
    return redirect("/stateView")

def statedelete(request,id):
    state=StateMasterTable.objects.get(state_id=id)
    state.delete()
    return redirect("/stateView")

def city(request):
    cityobj=CityVillageMaster.objects.all()
    print(cityobj)
    return render(request, "authentication/cityadd.html",{'cityobj':cityobj})

def citysave(request):
    cid=request.POST.get('txtcid')
    did=request.POST.get('txtdid')
    sid=request.POST.get('txtsid')
    name=request.POST.get('txtcname')
    desc=request.POST.get('txtcdesc')
    #cbui=request.POST.get('txtuser')
    #cd=request.POST.get('txtuserdate')
    #ubui=request.POST.get('txtupdate')
    #ud=request.POST.get('txtup')
    city=CityVillageMaster(city_village_id=cid,district=did,state=sid,city_village_name=name,description=desc)#created_by_user=cbui,created_date=cd,updated_by_user=ubui,updated_date=ud)
    city.save()
    return redirect("/cityView")

def cityedit(request,id):
    city=CityVillageMaster.objects.get(city_village_id=id)
    return render(request, "authentication/cityedit.html",{'city':city})

def cityupdate(request,id):
        city=CityVillageMaster.objects.get(city_village_id=id)
        #cid=request.POST.get('txtcid')
        #did=request.POST.get('txtdid')
        #sid=request.POST.get('txtsid')
        name=request.POST.get('txtcname')
        desc=request.POST.get('txtcdesc')
        #cbui=request.POST.get('txtuser')
        #cd=request.POST.get('txtuserdate')
        #ubui=request.POST.get('txtupdate')
        #ud=request.POST.get('txtup')
        #city.city_village_id=cid
        #city.district=did
        #city.state=sid
        city.city_village_name=name
        city.description=desc
        #city.created_by_user=cbui
        #city.created_date=cd
        #city.updated_by_user=ubui
        #city.updated_date=ud
        city.save()
        return redirect("/cityView")

def citydelete(request,id):
    city=CityVillageMaster.objects.get(city_village_id=id)
    city.delete()
    return redirect("/cityView")

def cityView(request):
    objCityMaster = CityVillageMaster.objects.all()
    print(objCityMaster)
    return render(request, "authentication/city-list.html",{'cityobj':objCityMaster})

def gst(request):
    gstobj=Gstcharges.objects.all()
    print(gstobj)
    return render(request, "authentication/gstadd.html",{'gstobj':gstobj})

def gstsave(request):
    gid=request.POST.get('txtgid')
    gyear=request.POST.get('txtgyear')
    gcgst=request.POST.get('txtcgst')
    gsgst=request.POST.get('txtsgst')
    gst=Gstcharges(gst_char_id=gid,year=gyear,cgst_per=gcgst,sgst_per=gsgst)
    gst.save()
    return redirect("/gstView")
    
def gstedit(request,id):
    gst=Gstcharges.objects.get(gst_char_id=id)
    return render(request, "authentication/gstedit.html",{'gst':gst})

def gstupdate(request,id):
    gst=Gstcharges.objects.get(gst_char_id=id)
    gyear=request.POST.get('txtgyear')
    gcgst=request.POST.get('txtcgst')
    gsgst=request.POST.get('txtsgst')
    gst.year=gyear
    gst.cgst_per=gcgst
    gst.sgst_per=gsgst
    gst.save()
    return redirect("/gstView")

def gstdelete(request,id):
    gst=Gstcharges.objects.get(gst_char_id=id)
    gst.delete()
    return redirect("/gstView")

def gstView(request):
    objGstMaster = Gstcharges.objects.all()
    print(objGstMaster)
    return render(request, "authentication/gst-list.html",{'gstobj':objGstMaster})

def dist(request):
    distobj=DistrictMaster.objects.all()
    print(distobj)
    return render(request, "authentication/distadd.html",{'distobj':distobj})

def distsave(request):
    did=request.POST.get('txtdid')
    dname=request.POST.get('txtdname')
    sid=request.POST.get('txtsid')
    ddesc=request.POST.get('txtddesc')
    dist=DistrictMaster(district_id=did,district_name=dname,state=sid,description=ddesc)
    dist.save()
    return redirect("/distView")

def distedit(request,id):
    dist=DistrictMaster.objects.get(district_id=id)
    return render(request, "authentication/distedit.html",{'dist':dist})

def distupdate(request,id):
    dist=DistrictMaster.objects.get(district_id=id)
    dname=request.POST.get('txtdname')
    sid=request.POST.get('txtsid')
    ddesc=request.POST.get('txtddesc')
    dist.district_name=dname
    dist.state=sid
    dist.description=ddesc
    dist.save()
    return redirect("/distView")

def distdelete(request,id):
    dist=DistrictMaster.objects.get(district_id=id)
    dist.delete()
    return redirect("/distView")

def distView(request):
    objDistMaster = DistrictMaster.objects.all()
    print(objDistMaster)
    return render(request, "authentication/district-list.html",{'distobj':objDistMaster})

def docView(request):
    objDocMaster = DocMaster.objects.all()
    print(objDocMaster)
    return render(request, "authentication/doc-list.html",{'docobj':objDocMaster})

def vehView(request):
    objVehMaster = VehicleMaster.objects.all()
    print(objVehMaster)
    return render(request, "authentication/vehicle_master-list.html",{'vehobj':objVehMaster})

def vehroutView(request):
    objVehroutMaster = VehicleRoutMaster.objects.all()
    print(objVehroutMaster)
    return render(request, "authentication/vehicle_rout_master-list.html",{'vehroutobj':objVehroutMaster})

def user(request):
    userobj=UserMasterTable.objects.all()
    print(userobj)
    return render(request, "authentication/useradd.html",{'userobj':userobj})

def usersave(request):
    id=request.POST.get('txtuid')
    mail=request.POST.get('txtemail')
    name=request.POST.get('txtuname')
    pas=request.POST.get('txtpass')
    user=UserMasterTable(user_master_id=id,user_email_id=mail,user_name=name,user_password=pas)
    user.save()
    return redirect("/userView")

def useredit(request,id):
    user=UserMasterTable.objects.get(user_master_id=id)
    return render(request, "authentication/useredit.html",{'user':user})

def userupdate(request,id):
    user=UserMasterTable.objects.get(user_master_id=id)
    email=request.POST.get('txtemail')
    name=request.POST.get('txtuname')
    pas=request.POST.get('txtpass')
    user.user_email_id=email
    user.user_name=name
    user.user_password=pas
    user.save()
    return redirect("/userView")

def userdelete(request,id):
    user=UserMasterTable.objects.get(user_master_id=id)
    user.delete()
    return redirect("/userView")

def userView(request):
    objUserMaster = UserMasterTable.objects.all()
    print(objUserMaster)
    return render(request, "authentication/user_master-list.html",{'userobj':objUserMaster})

def review(request):
    reviewobj1=ReviewFeedback.objects.all()
    print(reviewobj1)
    return render(request, "authentication/reviewadd.html",{'reviewobj1':reviewobj1})

def reviewsave(request):
    rid=request.POST.get('txtrid')
    ruid=request.POST.get('txtruid')
    img=request.POST.get('txtrimg')
    rdesc=request.POST.get('txtrdesc')
    rstar=request.POST.get('txtrstar')
    review=ReviewFeedback(review_id=rid,user=ruid,review_image=img,review_description=rdesc,review_star=rstar)
    review.save()
    return redirect("/reviewView")

def reviewedit(request,id):
    review=ReviewFeedback.objects.get(review_id=id)
    return render(request, "authentication/reviewedit.html",{'review':review})

def reviewupdate(request,id):
    review=ReviewFeedback.objects.get(review_id=id)
    rimg=request.POST.get('txtrimg')
    rdesc=request.POST.get('txtrdesc')
    rstar=request.POST.get('txtrstar')
    review.review_image=rimg
    review.review_description=rdesc
    review.review_star=rstar
    review.save()
    return redirect("/reviewView")

def reviewdelete(request,id):
    review=ReviewFeedback.objects.get(review_id=id)
    review.delete()
    return redirect("/reviewView")


def reviewView(request):
    objReviewMaster = ReviewFeedback.objects.all()
    print(objReviewMaster)
    return render(request, "authentication/review&feedback-list.html",{'reviewobj':objReviewMaster})
