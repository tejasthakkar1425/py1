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
    return render(request, "authentication/stateadd.html")

def statesave(request):
    if request.method=="POST":
        id=request.POST.get('txtsid')
        name=request.POST.get('txtsname')
        desc=request.POST.get('txtdesc')
        cbui=request.POST.get('txtuser')
        cd=request.POST.get('txtuserdate')
        ubui=request.POST.get('txtupdate')
        ud=request.POST.get('txtup')
        state=StateMasterTable(state_id=id,stat_name=name,description=desc,created_by_user=cbui,created_date=cd,updated_by_user=ubui,updated_date=ud)
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
    if request.method=="GET":
        state=StateMasterTable.objects.get(state_id=id)
        name=request.POST.get('txtsname')
        desc=request.POST.get('txtdesc')
        cbui=request.POST.get('txtuser')
        cd=request.POST.get('txtuserdate')
        ubui=request.POST.get('txtupdate')
        ud=request.POST.get('txtup')
        state.stat_name=name
        state.description=desc
        state.created_by_user=cbui
        state.created_date=cd
        state.updated_by_user=ubui
        state.updated_date=ud
        state.save()
    return redirect("/stateView")

def statedelete(request,id):
    state=StateMasterTable.objects.get(state_id=id)
    state.delete()
    return redirect("/stateView")

def city(request):
    return render(request, "authentication/cityadd.html")

def citysave(request):
    if request.method=="POST":
        cid=request.POST.get('txtcid')
        did=request.POST.get('txtdid')
        sid=request.POST.get('txtsid')
        name=request.POST.get('txtcname')
        desc=request.POST.get('txtcdesc')
        cbui=request.POST.get('txtuser')
        cd=request.POST.get('txtuserdate')
        ubui=request.POST.get('txtupdate')
        ud=request.POST.get('txtup')
        city=CityVillageMaster(city_village_id=cid,district=did,state=sid,city_village_name=name,description=desc,created_by_user=cbui,created_date=cd,updated_by_user=ubui,updated_date=ud)
        city.save()
    return redirect("/cityView")

def cityedit(request,id):
    city=CityVillageMaster.objects.get(city_village_id=id)
    return render(request, "authentication/cityedit.html",{'city':city})

def cityupdate(request,id):
        city=CityVillageMaster.objects.get(city_village_id=id)
        cid=request.POST.get('txtcid')
        did=request.POST.get('txtdid')
        sid=request.POST.get('txtsid')
        name=request.POST.get('txtcname')
        desc=request.POST.get('txtcdesc')
        cbui=request.POST.get('txtuser')
        cd=request.POST.get('txtuserdate')
        ubui=request.POST.get('txtupdate')
        ud=request.POST.get('txtup')
        city.city_village_id=cid
        city.district=did
        city.state=sid
        city.city_village_name=name
        city.description=desc
        city.created_by_user=cbui
        city.created_date=cd
        city.updated_by_user=ubui
        city.updated_date=ud
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
    if request.method=="POST":
        form=Gst(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/gstView")
            except:
                pass
    else:
        form=Gst()
    return render(request, "authentication/gstadd.html",{'form':form})
    
def gstedit(request,id):
    gst=Gstcharges.objects.get(gst_char_id=id)
    return render(request, "authentication/gstedit.html",{'gst':gst})

def gstupdate(request,id):
    gst=Gstcharges.objects.get(gst_char_id=id)
    form=Gst(request.POST,instance=gst)
    if form.is_valid():
        form.save()
        return redirect("/gstView")
    
    return render(request, "authentication/gstedit.html",{'gst':gst})

def gstdelete(request,id):
    gst=Gstcharges.objects.get(gst_char_id=id)
    gst.delete()
    return redirect("/gstView")


def gstView(request):
    objGstMaster = Gstcharges.objects.all()
    print(objGstMaster)
    return render(request, "authentication/gst-list.html",{'gstobj':objGstMaster})

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

def userView(request):
    objUserMaster = UserMasterTable.objects.all()
    print(objUserMaster)
    return render(request, "authentication/user_master-list.html",{'userobj':objUserMaster})

def reviewView(request):
    objReviewMaster = ReviewFeedback.objects.all()
    print(objReviewMaster)
    return render(request, "authentication/review&feedback-list.html",{'reviewobj':objReviewMaster})