from sre_parse import State
from django.shortcuts import redirect, render
from django.http import HttpResponse

from home.models import city_village_master_table, district_master_table, doc_master_table, gstcharges, review_feedback_table, state_master_table, user_master_table, vehicle_master_table, vehicle_route_master_table

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

def stateView(request):
    objStateMaster = state_master_table.objects.all()
    print(objStateMaster)
    return render(request, "authentication/state-list.html",{'stateobj':objStateMaster})

def stateupdate(request,id):
    state=State.objects.get(state_id=id)
    name=request.POST.get('txtsname')
    state.state_name=name

    state.save()
    return redirect("/state/")

def cityView(request):
    objCityMaster = city_village_master_table.objects.all()
    print(objCityMaster)
    return render(request, "authentication/city-list.html",{'cityobj':objCityMaster})

def gstView(request):
    objGstMaster = gstcharges.objects.all()
    print(objGstMaster)
    return render(request, "authentication/gst-list.html",{'gstobj':objGstMaster})

def distView(request):
    objDistMaster = district_master_table.objects.all()
    print(objDistMaster)
    return render(request, "authentication/district-list.html",{'distobj':objDistMaster})

def docView(request):
    objDocMaster = doc_master_table.objects.all()
    print(objDocMaster)
    return render(request, "authentication/district-list.html",{'docobj',objDocMaster})

def vehViwe(request):
    objVehMaster = vehicle_master_table.objects.all()
    print(objVehMaster)
    return render(request, "authentication/vehicle_master-list.html",{'vehobj',objVehMaster})

def vehroutViwe(request):
    objVehroutMaster = vehicle_route_master_table.objects.all()
    print(objVehroutMaster)
    return render(request, "authentication/vehicle_rout_master-list.html",{'vehroutobj',objVehroutMaster})

def userView(request):
    objUserMaster = user_master_table.objects.all()
    print(objUserMaster)
    return render(request, "authentication/user_master-list.html",{'userobj',objUserMaster})

def reviewView(request):
    objReviewMaster = review_feedback_table.objects.all()
    print(objReviewMaster)
    return render(request, "authentication/review&feedback-list.html",{'reviewobj',objReviewMaster})