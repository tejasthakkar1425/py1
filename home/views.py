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
def admin(request):
    return render(request, "authentication/masterpage.html")

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

def doc(request):
    docobj=DocMaster.objects.all()
    print(docobj)
    return render(request, "authentication/docadd.html",{'docobj':docobj})

def docsave(request):
    id=request.POST.get('txtdocid')
    num=request.POST.get('txtdnum')
    date=request.POST.get('txtddate')
    lnum=request.POST.get('txtlnum')
    gid=request.POST.get('txtgid')
    net=request.POST.get('txtnet')
    cancel=request.POST.get('txtis')
    doc=DocMaster(doc_id=id,doc_number=num,doc_date=date,lr_number=lnum,gst_charges=gid,net_amount=net,is_cancel=cancel)
    doc.save()
    return redirect("/docView")

def docedit(request,id):
    doc=DocMaster.objects.get(doc_id=id)
    return render(request, "authentication/docedit.html",{'doc':doc})

def docupdate(request,id):
    doc=DocMaster.objects.get(doc_id=id)
    num=request.POST.get('txtdnum')
    date=request.POST.get('txtddate')
    lnum=request.POST.get('txtlnum')
    gid=request.POST.get('txtgid')
    net=request.POST.get('txtnet')
    cancel=request.POST.get('txtis')
    doc.doc_number=num
    doc.doc_date=date
    doc.lr_number=lnum
    doc.gst_charges=gid
    doc.net_amount=net
    doc.is_cancel=cancel
    doc.save()
    return redirect("/docView")

def docdelete(request,id):
    doc=DocMaster.objects.get(doc_id=id)
    doc.delete()
    return redirect("/docView")

def docView(request):
    objDocMaster = DocMaster.objects.all()
    print(objDocMaster)
    return render(request, "authentication/doc-list.html",{'docobj':objDocMaster})

def veh(request):
    vehobj=VehicleMaster.objects.all()
    print(vehobj)
    return render(request, "authentication/vehadd.html",{'vehobj':vehobj})

def vehsave(request):
    id=request.POST.get('txtvid')
    name=request.POST.get('txtvname')
    rcnum=request.POST.get('txtrcnum')
    rnum=request.POST.get('txtrnum')
    cap=request.POST.get('txtcap')
    insf=request.POST.get('txtfdate')
    inst=request.POST.get('txttdate')
    com=request.POST.get('txtcom')
    own=request.POST.get('txtown')
    veh=VehicleMaster(vehicle_id=id,vehicle_name=name,rc_book_number=rcnum,reg_no=rnum,capacity=cap,insurance_from=insf,insurance_to=inst,insurance_company_name=com,owner_name=own)
    veh.save()
    return redirect("/vehView")

def vehedit(request,id):
    veh=VehicleMaster.objects.get(vehicle_id=id)
    return render(request,"authentication/vehedit.html",{'veh':veh})

def vehupdate(request,id):
    veh=VehicleMaster.objects.get(vehicle_id=id)
    name=request.POST.get('txtvname')
    rcnum=request.POST.get('txtrcnum')
    rnum=request.POST.get('txtrnum')
    cap=request.POST.get('txtcap')
    insf=request.POST.get('txtfdate')
    inst=request.POST.get('txttdate')
    com=request.POST.get('txtcom')
    own=request.POST.get('txtown')
    veh.vehicle_name=name
    veh.rc_book_number=rcnum
    veh.reg_no=rnum
    veh.capacity=cap
    veh.insurance_from=insf
    veh.insurance_to=inst
    veh.insurance_company_name=com
    veh.owner_name=own
    veh.save()
    return redirect("/vehView")

def vehdelete(request,id):
    veh=VehicleMaster.objects.get(vehicle_id=id)
    veh.delete()
    return redirect("/vehView")

def vehView(request):
    objVehMaster = VehicleMaster.objects.all()
    print(objVehMaster)
    return render(request, "authentication/vehicle_master-list.html",{'vehobj':objVehMaster})

def vehrout(request):
    vehroutobj=VehicleRoutMaster.objects.all()
    print(vehroutobj)
    return render(request, "authentication/vehroutadd.html",{'vehroutobj':vehroutobj})

def vehroutsave(request):
    id=request.POST.get('txtvrid')
    fsid=request.POST.get('txtfsid')
    tsid=request.POST.get('txttsid')
    vrd=request.POST.get('txtvrd')
    vrdid=request.POST.get('txtvrdid')
    vehrout=VehicleRoutMaster(veh_rout_id=id,from_state=fsid,to_state=tsid,vehc_rout_det=vrd,veh_rout_details=vrdid)
    vehrout.save()
    return redirect("/vehroutView")

def vehroutedit(request,id):
    vehrout=VehicleRoutMaster.objects.get(veh_rout_id=id)
    return render(request, "authentication/vehroutedit.html",{'vehrout':vehrout})

def vehroutupdate(request,id):
    vehrout=VehicleRoutMaster.objects.get(veh_rout_id=id)
    fsid=request.POST.get('txtfsid')
    tsid=request.POST.get('txttsid')
    vrd=request.POST.get('txtvrd')
    vrdid=request.POST.get('txtvrdid')
    vehrout.from_state=fsid
    vehrout.to_state=tsid
    vehrout.vehc_rout_det=vrd
    vehrout.veh_rout_details=vrdid
    vehrout.save()
    return redirect("/vehroutView")

def vehroutdelete(request,id):
    vehrout=VehicleRoutMaster.objects.get(veh_rout_id=id)
    vehrout.delete()
    return redirect("/vehroutView")

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
