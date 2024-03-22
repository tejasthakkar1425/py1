from sre_parse import State
from turtle import done
from django.shortcuts import redirect, render
from django.http import HttpResponse
from home.models import *
from home.forms import *
import json

def home(request,done=0):
    return render(request, "authentication/index.html",{"done":done})


def about(request):
    return render(request, "authentication/about.html")

def success_order(request):

    return render(request, "authentication/success_order.html")

def payment_option(request):
    name = request.POST["name"]
    price = request.POST["estimatePrice"]
    weight = request.POST["weight"]
    lr = request.POST["LRNumber"]
    phonenumber = request.POST["phoneNumber"]
    passdone=1
    return render(request, "authentication/payment_option.html",{"name":name})
    
    

def order(request):
    return render(request, "authentication/order.html")
  
def estimate(request):
    return render(request, "authentication/estimate.html")

def dashboard(request):
    return render(request, "authentication/dashboard.html")

def contact(request):
    return render(request, "authentication/contact.html")

def service(request):
    return render(request, "authentication/service.html")

def login1(request):
    return render(request, "authentication/login.html")

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
def login(request):
  #  modeldt = adminModel.objects.all()
        
        if request.method == 'POST':
            email_id = request.POST['email']
            passw = request.POST['password']
            try:
                 user_instance = UserMasterTable.objects.get(user_email_id = email_id)
                 if user_instance.user_password == passw:
                          print(user_instance.user_password)
                          user_details = UserDetails.objects.get(user_master = user_instance.user_master_id )
                          print("login done")
                          if user_details.user_type == 1:
                              print("checked the type")
                              return dashboard(request)
                          if user_details.user_type == 2:
                              print("checked the type")
                              done=1
                              return home(request,done)
                          if user_details.user_type == 3:
                              print("checked the type") 
                              return employee(request)
                 else:
                          return render(request, 'authentication/login.html', {'error': 'Incorrect password'})
            except:
                    return render(request, 'authentication/login.html', {'error': 'User not found'})
        return HttpResponse(render(request,'authentication/login.html'))
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
def curior_close(request):
     if request.method == 'GET':
        category = DocMaster.objects.all()
        return render(request,'authentication/curior-close.html',{"docIds":category})
     if request.method == 'POST':
        ids= DocMaster.objects.all()
        id=request.POST['id']
        print("post done")
        category = DocMaster.objects.get(doc_id=id)
        return render(request,'authentication/curior-close.html',{"docIds":ids,"docDetail":category})

def employee(request):
    return render(request, "authentication/curior-close.html")
   
def get_district(request):
    get_district_obj=DocDetail.objects.all()
    return render(request, "authentication/update-district.html",{'update_district':get_district_obj})


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
""""
def UserMasterTable(request):
    if request.method == 'POST':
        user_email_id=request.POST.get('email')
        user_name=request.POST.get('username')
        user_password=request.POST.get('userpassword')
        umt=UserMasterTable(user_email_id=user_email_id,user_name=user_name,user_password=user_password)
        umt.save()
        print("registered")
        return home(request,done)
    return render(request,"authentication/registration.html")
"""
        
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

def report(request):
    objreport = DocDetail.objects.all()
    print(objreport)
    return render(request, "authentication/report.html",{'reportobj':objreport})

def dist(request):
    distobj=StateMasterTable.objects.all()
    print(distobj)
    return render(request, "authentication/distadd.html",{'distobj':distobj})

def distsave(request):
    form = DisForm(request.POST)
    data = form.cleaned_data['data_field']
    print(data)
    did=request.POST.get('txtdid')
    dname=request.POST.get('txtdname')
    sid=request.POST.get('DisId')
    print(sid)
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
    userobj = UserMasterTable.objects.all()
    print(userobj)
    return render(request, "authentication/user_master-list.html",{'userobj':userobj})

def review(request):
    reviewobj=ReviewFeedback.objects.all()
    print(reviewobj)
    return render(request, "authentication/reviewadd.html",{'reviewobj':reviewobj})

def reviewsave(request):
    rid=request.POST.get('txtrid')
    uid=request.POST.get('txtuid')
    img=request.POST.get('txtrimg')
    rdesc=request.POST.get('txtrdesc')
    rstar=request.POST.get('txtrstar')
    review=ReviewFeedback(review_id=rid,user=uid,review_image=img,review_description=rdesc,review_star=rstar)
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

def complain(request):
    complainobj=ComplainMaster.objects.all()
    print(complainobj)
    return render(request, "authentication/complainadd.html",{'complainobj':complainobj})

def complainsave(request):
    id=request.POST.get('txtcid')
    uid=request.POST.get('txtuid')
    desc=request.POST.get('txtcdesc')
    complain=ComplainMaster(com_id=id,user_master=uid,com_description=desc)
    complain.save()
    return redirect("/complainView")

def complainedit(request,id):
    complain=ComplainMaster.objects.get(com_id=id)
    return render(request, "authentication/complainedit.html",{'complain':complain})

def complainupdate(request,id):
    complain=ComplainMaster.objects.get(com_id=id)
    uid=request.POST.get('txtuid')
    desc=request.POST.get('txtcdesc')
    complain.user_master=uid
    complain.com_description=desc
    complain.save()
    return redirect("/complainView")

def complaindelete(request,id):
    complain=ComplainMaster.objects.get(com_id=id)
    complain.delete()
    return redirect("/complainView")

def complainView(request):
    complainobj=ComplainMaster.objects.all()
    print(complainobj)
    return render(request, "authentication/complainlist.html",{'complainobj':complainobj})

def complainstatus(request):
    complainstatusobj=ComplainStatus.objects.all()
    print(complainstatusobj)
    return render(request, "authentication/complainstatusadd.html",{'complainstatusobj':complainstatusobj})

def complainstatussave(request):
    cid=request.POST.get('txtcid')
    id=request.POST.get('txtcsid')
    date=request.POST.get('txtcsdate')
    status=request.POST.get('txtcstatus')
    complainstatus=ComplainStatus(com=cid,com_status_id=id,com_status_date=date,com_status=status)
    complainstatus.save()
    return redirect("/complainsView")

def complainstatusedit(request,id):
    complainstatus=ComplainStatus.objects.get(com_status_id=id)
    return render(request, "authentication/complainsedit.html",{'complainstatus':complainstatus})

def complainstatusupdate(request,id):
    complainstatus=ComplainStatus.objects.get(com_status_id=id)
    cid=request.POST.get('txtcid')
    date=request.POST.get('txtcsdate')
    status=request.POST.get('txtcstatus')
    complainstatus.com=cid
    complainstatus.com_status_date=date
    complainstatus.com_status=status
    complainstatus.save()
    return redirect("/complainsView")

def complainstatusdelete(request,id):
    complainstatus=ComplainStatus.objects.get(com_status_id=id)
    complainstatus.delete()
    return redirect("/complainsView")

def complainsView(request):
    complainstatusobj=ComplainStatus.objects.all()
    print(complainstatusobj)
    return render(request, "authentication/complainstatuslist.html",{'complainstatusobj':complainstatusobj})

def docdetail(request):
    docdetobj=DocDetail.objects.all()
    print(docdetobj)
    return render(request, "authentication/docdetadd.html",{'docdetobj':docdetobj})

def docdetsave(request):
    did=request.POST.get('txtddid')
    id=request.POST.get('txtdid')
    addre=request.POST.get('txtdadd')
    vrid=request.POST.get('txtvrid')
    wet=request.POST.get('txtwet')
    vrdid=request.POST.get('txtvrdid')
    amount=request.POST.get('txtamount')
    docdet=DocDetail(doc_detail_id=did,doc=id,doc_address=addre,vehc_rout=vrid,doc_weight=wet,veh_rout_det=vrdid,total_amount=amount)
    docdet.save()
    return redirect("/docdetView")

def docdetedit(request,id):
    docdet=DocDetail.objects.get(doc_detail_id=id)
    return render(request, "authentication/docdetedit.html",{'docdet':docdet})

def docdetupdate(request,id):
    docdet=DocDetail.objects.get(doc_detail_id=id)
    id=request.POST.get('txtdid')
    addre=request.POST.get('txtdadd')
    vrid=request.POST.get('txtvrid')
    wet=request.POST.get('txtwet')
    vrdid=request.POST.get('txtvrdid')
    amount=request.POST.get('txtamount')
    docdet.doc=id
    docdet.doc_address=addre
    docdet.vehc_rout=vrid
    docdet.doc_weight=wet
    docdet.veh_rout_det=vrdid
    docdet.total_amount=amount
    docdet.save()
    return redirect("/docdetView")

def docdetdelete(request,id):
    docdet=DocDetail.objects.get(doc_detail_id=id)
    docdet.delete()
    return redirect("/docdetView")

def docdetView(request):
    docdetobj=DocDetail.objects.all()
    print(docdetobj)
    return render(request, "authentication/docdetlist.html",{'docdetobj':docdetobj})

def docvehdet(request):
    docvehdet=DocVehDetailsTable.objects.all()
    print(docvehdet)
    return render(request, "authentication/docvehdet.html",{'docvehdet':docvehdet})

def docvehdetsave(request):
    id=request.POST.get('txtdvdid')
    did=request.POST.get('txtdid')
    vid=request.POST.get('txtvid')
    vrid=request.POST.get('txtvrid')
    desc=request.POST.get('txtdesc')
    docvehdet=DocVehDetailsTable(doc_veh_det_id=id,doc=did,veh=vid,vehc_rout=vrid,description=desc)
    docvehdet.save()
    return redirect("/docvehdetView")

def docvehdetedit(request,id):
    docvehdet=DocVehDetailsTable.objects.get(doc_veh_det_id=id)
    return render(request, "authentication/docvehdetedit.html",{'docvehdet':docvehdet})

def docvehdetupdate(request,id):
    docvehdetobj=DocVehDetailsTable.objects.get(doc_veh_det_id=id)
    did=request.POST.get('txtdid')
    vid=request.POST.get('txtvid')
    vrid=request.POST.get('txtvrid')
    desc=request.POST.get('txtdesc')
    docvehdetobj.doc=did
    docvehdetobj.veh=vid
    docvehdetobj.vehc_rout=vrid
    docvehdetobj.description=desc
    docvehdetobj.save()
    return redirect("/docvehdetView")

def docvehdetdelete(request,id):
    docvehdet=DocVehDetailsTable.objects.get(doc_veh_det_id=id)
    docvehdet.delete()
    return redirect("/docvehdetView")

def docvehdetView(request):
    docvehdet=DocVehDetailsTable.objects.all()
    print(docvehdet)
    return render(request, "authentication/docvehdetlist.html",{'docvehdet':docvehdet})

def reviewstatus(request):
    revstaobj=ReviewFeedbackStatus.objects.all()
    print(revstaobj)
    return render(request, "authentication/reviewstatus.html",{'revstaobj':revstaobj})

def reviewstatussave(request):
    id=request.POST.get('txtrsid')
    rid=request.POST.get('txtrid')
    stat=request.POST.get('txtstatus')
    uid=request.POST.get('txtuid')
    reviewstatus=ReviewFeedbackStatus(review_status_id=id,review=rid,status=stat,user=uid)
    reviewstatus.save()
    return redirect("/reviewstatusView")

def reviewstatusedit(request,id):
    revstaobj=ReviewFeedbackStatus.objects.get(review_status_id=id)
    return render(request, "authentication/reviewstatusedit.html",{'revstaobj':revstaobj})

def reviewstatusupdate(request,id):
    revstaobj=ReviewFeedbackStatus.objects.get(review_status_id=id)
    stat=request.POST.get('txtstatus')
    revstaobj.status=stat
    revstaobj.save()
    return redirect("/reviewstatusView")

def reviewstatusdelete(request,id):
    revstaobj=ReviewFeedbackStatus.objects.get(review_status_id=id)
    revstaobj.delete()
    return redirect("/reviewstatusView")

def reviewstatusView(request):
    revstaobj=ReviewFeedbackStatus.objects.all()
    print(revstaobj)
    return render(request, "authentication/reviewstatuslist.html",{'revstaobj':revstaobj})

def payment(request):
    paymentobj=PaymentMaster.objects.all()
    print(paymentobj)
    return render(request, "authentication/paymentadd.html",{'paymentobj':paymentobj})

def paymentsave(request):
    detail=request.POST.get('txtpdet')
    payid=request.POST.get('txtpayid')
    did=request.POST.get('txtdid')
    paysta=request.POST.get('txtpaysta')
    paymet=request.POST.get('txtpaymet')
    transid=request.POST.get('txttransid')
    resp=request.POST.get('txtresp')
    payment=PaymentMaster(doc_pay_detail=detail,doc_pay_detail_id=payid,doc=did,pay_status=paysta,pay_method=paymet,pay_tran_id=transid,pay_response=resp)
    payment.save()
    return redirect("/paymentView")

def paymentedit(request,id):
    payment=PaymentMaster.objects.get(doc_pay_detail_id=id)
    return render(request, "authentication/paymentedit.html",{'payment':payment})

def paymentupdate(request,id):
    payment=PaymentMaster.objects.get(doc_pay_detail_id=id)
    detail=request.POST.get('txtpdet')
    paysta=request.POST.get('txtpaysta')
    paymet=request.POST.get('txtpaymet')
    transid=request.POST.get('txttransid')
    resp=request.POST.get('txtresp')
    payment.doc_pay_detail=detail
    payment.pay_status=paysta
    payment.pay_method=paymet
    payment.pay_tran_id=transid
    payment.pay_response=resp
    payment.save()
    return redirect("/paymentView")

def paymentdelete(request,id):
    payment=PaymentMaster.objects.get(doc_pay_detail_id=id)
    payment.delete()
    return redirect("/paymentView")

def paymentView(request):
    paymentobj=PaymentMaster.objects.all()
    print(paymentobj)
    return render(request, "authentication/paymentlist.html",{'paymentobj':paymentobj})

def userdet(request):
    userdetobj=UserDetails.objects.all()
    print(userdetobj)
    return render(request, "authentication/userdetail.html",{'userdetobj':userdetobj})

def userdetsave(request):
    id=request.POST.get('txtudid')
    uid=request.POST.get('txtuid')
    typ=request.POST.get('txttyp')
    pic=request.POST.get('txtpic')
    con=request.POST.get('txtcon')
    gen=request.POST.get('txtgen')
    add=request.POST.get('txtadd')
    userdet=UserDetails(user_deatil_id=id,user_master=uid,user_type=typ,profile_pic=pic,contact=con,gender=gen,address=add)
    userdet.save()
    return redirect("/userdetView")

def userdetedit(request,id):
    userdet=UserDetails.objects.get(user_deatil_id=id)
    return render(request, "authentication/userdetedit.html",{'userdet':userdet})

def userdetupdate(request,id):
    userdet=UserDetails.objects.get(user_deatil_id=id)
    pic=request.POST.get('txtpic')
    con=request.POST.get('txtcon')
    add=request.POST.get('txtadd')
    userdet.profile_pic=pic
    userdet.contact=con
    userdet.address=add
    userdet.save()
    return redirect("/userdetView")

def userdetdelete(request,id):
    userdet=UserDetails.objects.get(user_deatil_id=id)
    userdet.delete()
    return redirect("/userdetView")

def userdetView(request):
    userdetobj=UserDetails.objects.all()
    print(userdetobj)
    return render(request, "authentication/userdetlist.html",{'userdetobj':userdetobj})

def vehroutdet(request):
    vehroutdetobj=VehRoutDetalis.objects.all()
    print(vehroutdetobj)
    return render(request, "authentication/vehroutdet.html",{'vehroutdetobj':vehroutdetobj})

def vehroutdetsave(request):
    id=request.POST.get('txtvrdid')
    vrid=request.POST.get('txtvrid')
    sid=request.POST.get('txtsid')
    did=request.POST.get('txtdid')
    cid=request.POST.get('txtcid')
    desc=request.POST.get('txtdesc')
    chbe50=request.POST.get('txtchbe50')
    chbe150=request.POST.get('txtchbe150')
    chab150=request.POST.get('txtchab150')
    vehroutdet=VehRoutDetalis(veh_rout_det_id=id,veh_rout=vrid,state=sid,ditrict=did,city_village=cid,decription=desc,char_bel_50=chbe50,char_bel_150=chbe150,char_abo_150=chab150)
    vehroutdet.save()
    return redirect("/vehroutdetView")

def vehroudetedit(request,id):
    vehroutdet=VehRoutDetalis.objects.get(veh_rout_det_id=id)
    return render(request, "authentication/vehroutdetedit.html",{'vehroutdet':vehroutdet})

def vehroutdetupdate(request,id):
    vehroutdet=VehRoutDetalis.objects.get(veh_rout_det_id=id)
    vrid=request.POST.get('txtvrid')
    sid=request.POST.get('txtsid')
    did=request.POST.get('txtdid')
    cid=request.POST.get('txtcid')
    desc=request.POST.get('txtdesc')
    chbe50=request.POST.get('txtchbe50')
    chbe150=request.POST.get('txtchbe150')
    chab150=request.POST.get('txtchab150')
    vehroutdet.veh_rout=vrid
    vehroutdet.state=sid
    vehroutdet.ditrict=did
    vehroutdet.city_village=cid
    vehroutdet.decription=desc
    vehroutdet.char_bel_50=chbe50
    vehroutdet.char_bel_150=chbe150
    vehroutdet.char_abo_150=chab150
    vehroutdet.save()
    return redirect("/vehroutdetView")

def vehroutdetdelete(request,id):
    vehroutdet=VehRoutDetalis.objects.get(veh_rout_det_id=id)
    vehroutdet.delete()
    return redirect("/vehroutdetView")

def vehroutdetView(request):
    vehroutdetobj=VehRoutDetalis.objects.all()
    print(vehroutdetobj)
    return render(request, "authentication/vehroutdetlist.html",{'vehroutdetobj':vehroutdetobj})

def product(request):
    return render(request ,"authentication/services.html")