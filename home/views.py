import os
import requests
from sre_parse import State
from turtle import done
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, JsonResponse
from home.models import *
from home.forms import *
from home.util import *
import json

def home(request):
    return render(request, "authentication/index.html")


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

def customerpanel(request):
    userobj=UserMasterTable.objects.all()
    print(userobj)
    return render(request, "authentication/customerpanel.html",{'userobj':userobj})

def stateadd(request):
    stateobj=StateMasterTable.objects.all()
    print(stateobj)
    form = stateForm()
    return render(request, "authentication/stateadd.html",{'form':form,'stateobj':stateobj})

def statesave(request):
    form = stateForm()
    if request.method == 'POST':
        form = stateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/stateView")
        else:
            return redirect("/stateView")
    return redirect("/stateView")
    
def login(request):
  #  modeldt = adminModel.objects.all()
        
        if request.method == 'POST':
            email_id = request.POST['email']
            passw = request.POST['password']
            print(email_id)
            try:
                 user_instance = UserMasterTable.objects.get(user_email_id = email_id)
                 print(user_instance)
                 if user_instance.user_password == passw:
                          print(user_instance.user_password)
                          user_details = UserDetails.objects.get(user_master = user_instance.user_master_id )
                          print("login done")
                          if user_details.user_type == 1:
                              print("checked the type")
                              return dashboard(request)
                          if user_details.user_type == 2:
                              print("checked the type")
                              return customerpanel(request)
                          if user_details.user_type == 3:
                              print("checked the type") 
                              return employee(request)
                 else:
                          return render(request, 'authentication/login.html', {'error': 'Incorrect password'})
            except  Exception as e: 
                print(e)
                return render(request, 'authentication/login.html', {'error': 'User not found'})
        return HttpResponse(render(request,'authentication/login.html'))
def stateView(request):
    if request.method=="POST":
        search = request.POST.get('search')
        objCity = StateMasterTable.objects.filter(stat_name=search)
        return render(request, "authentication/state-list.html",{'stateobj':objCity,"search":search})
    objStateMaster = StateMasterTable.objects.all()
    print(objStateMaster)
    return render(request, "authentication/state-list.html",{'stateobj':objStateMaster})

def stateedit(request,id):
    instance = get_object_or_404(StateMasterTable, state_id=id)
    if request.method == 'POST':
        form = stateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/stateView')  # Redirect to a success page
    else:
        form = stateForm(instance=instance)
    return render(request, "authentication/stateedit.html",{'form':form})

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
    form = cityVilageForm()
    cityobj=CityVillageMaster.objects.all()
    print(cityobj)
    return render(request, "authentication/cityadd.html",{'form':form,'cityobj':cityobj})

def citysave(request):
    form=cityVilageForm()
    if request.method == 'POST':
        form = cityVilageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/cityView")
        else:
            return redirect("/cityView")
    return redirect("/cityView")

def cityedit(request,id):
    instance = get_object_or_404(CityVillageMaster, city_village_id=id)
    if request.method == 'POST':
        form = cityVilageForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/cityView')  # Redirect to a success page
    else:
        form = cityVilageForm(instance=instance)
    return render(request, "authentication/cityedit.html",{'form':form})

def getState(request,id):
    DistId =id
    disobj = DistrictMaster.objects.filter(district_id=DistId)
    state=disobj.first().state
    print(state.state_id)
    stateobj = StateMasterTable.objects.filter(state_id=state.state_id)
    statedata = [{'id': sub.state_id, 'name': sub.stat_name} for sub in stateobj]
    print(statedata)
    return JsonResponse({'statedata': statedata})

def citydelete(request,id):
    city=CityVillageMaster.objects.get(city_village_id=id)
    city.delete()
    return redirect("/cityView")

def cityView(request):
    if request.method=="POST":
        search = request.POST.get('search')
        objCity = CityVillageMaster.objects.filter(city_village_name=search)
        return render(request, "authentication/city-list.html",{'cityobj':objCity,"search":search})
    objCityMaster = CityVillageMaster.objects.all()
    print(objCityMaster)
    return render(request, "authentication/city-list.html",{'cityobj':objCityMaster})

def empcomplain(request):
    form=empcomplainform()
    complain = ComplainStatus.objects.all()
    print(complain)
    return render(request,'authentication/empcomplain.html',{"complain":complain})
     
def empcomplainedit(request,id):
    instance = get_object_or_404(ComplainStatus, com_status_id=id)
    if request.method == 'POST':
        form = empcomplainform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/empcomplain')  # Redirect to a success page
    else:
        form = empcomplainform(instance=instance)
    return render(request, "authentication/empcompedit.html",{'form':form})
     
def empdocview(request):
    docobj2=DocDetail.objects.all()
    print(docobj2)
    return render(request, "authentication/empdoc.html",{'docobj2':docobj2})
     
def employee(request):
    return render(request, "authentication/employee.html")
   
def get_district(request):
    get_district_obj=DocDetail.objects.all()
    return render(request, "authentication/update-district.html",{'update_district':get_district_obj})


def gst(request):
    form=Gstform()
    gstobj=Gstcharges.objects.all()
    print(gstobj)
    return render(request, "authentication/gstadd.html",{'form':form,'gstobj':gstobj})

def gstsave(request):
    form = Gstform()
    if request.method == 'POST':
        form = Gstform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/gstView")
        else:
            return redirect("/gstView")
    return redirect("/gstView")
        
def gstedit(request,id):
    instance = get_object_or_404(Gstcharges, gst_char_id=id)
    if request.method == 'POST':
        form = Gstform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/gstView')  # Redirect to a success page
    else:
        form = Gstform(instance=instance)
    return render(request, "authentication/gstedit.html",{'form':form})

def gstdelete(request,id):
    gst=Gstcharges.objects.get(gst_char_id=id)
    gst.delete()
    return redirect("/gstView")

def gstView(request):
    
    if request.method=="POST":
        search = request.POST.get('search')
        objCity = Gstcharges.objects.filter(gst_char_id=search)
        return render(request, "authentication/gst-list.html",{'gstobj':objCity,"search":search})
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
    form = DisForm()
    return render(request, "authentication/distadd.html",{'form':form,'distobj':distobj})

def distsave(request):
    form = DisForm()
    if request.method == 'POST':
        form = DisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/distView")
        else:
            return redirect("/distView")
    return redirect("/distView")

def distedit(request,id):
    instance = get_object_or_404(DistrictMaster, district_id=id)
    if request.method == 'POST':
        form = DisForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/distView')  # Redirect to a success page
    else:
        form = DisForm(instance=instance)
    return render(request, "authentication/distedit.html",{'form':form})

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
    if request.method=="POST":
        search = request.POST.get('search')
        objCity = DistrictMaster.objects.filter(district_name=search)
        return render(request, "authentication/district-list.html",{'distobj':objCity,"search":search})
    objDistMaster = DistrictMaster.objects.all()
    return render(request, "authentication/district-list.html",{'distobj':objDistMaster})

def doc(request):
    form=Docform()
    docobj=DocMaster.objects.all()
    print(docobj)
    return render(request, "authentication/docadd.html",{'form':form,'docobj':docobj})

def docsave(request):
    form = Docform()
    if request.method == 'POST':
        form = Docform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/docView")
        else:
            return redirect("/docView")
    return redirect("/docView")

def docedit(request,id):
    instance = get_object_or_404(DocMaster, doc_id=id)
    if request.method == 'POST':
        form = Docform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/docView')  # Redirect to a success page
    else:
        form = Docform(instance=instance)
    return render(request, "authentication/docedit.html",{'form':form})

# def docupdate(request,id):
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
    return render(request, "authentication/doc-list.html",{'objDocMaster':objDocMaster})

def veh(request):
    form=Vehicleform()
    vehobj=VehicleMaster.objects.all()
    print(vehobj)
    return render(request, "authentication/vehadd.html",{'form':form,'vehobj':vehobj})

def vehsave(request):
    form = Vehicleform()
    if request.method == 'POST':
        form = Vehicleform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/vehView")
        else:
            return redirect("/vehView")
    return redirect("/vehView")

def vehedit(request,id):
    instance = get_object_or_404(VehicleMaster, vehicle_id=id)
    if request.method == 'POST':
        form = Vehicleform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/vehView')  # Redirect to a success page
    else:
        form = Vehicleform(instance=instance)
    return render(request, "authentication/vehedit.html",{'form':form})

#def vehupdate(request,id):
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
    form=vehroutmasterform()
    vehroutobj=VehicleRoutMaster.objects.all()
    print(vehroutobj)
    return render(request, "authentication/vehroutadd.html",{'form':form,'vehroutobj':vehroutobj})

def vehroutsave(request):
    form = vehroutmasterform()
    if request.method == 'POST':
        form = vehroutmasterform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/vehroutView")
        else:
            return redirect("/vehroutView")
    return redirect("/vehroutView")

def vehroutedit(request,id):
    instance = get_object_or_404(VehicleRoutMaster, veh_rout_id=id)
    if request.method == 'POST':
        form = vehroutmasterform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/vehroutView')  # Redirect to a success page
    else:
        form = vehroutmasterform(instance=instance)
    return render(request, "authentication/vehroutedit.html",{'form':form})

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
    form_master = Userform()
    userobj=UserMasterTable.objects.all()
    print(userobj)
    return render(request, "authentication/useradd.html",{'form_master':form_master,'userobj':userobj})

def usersave(request):
    form_master = Userform()
    if request.method == 'POST':
        form_master = Userform(request.POST)
        if form_master.is_valid():
            form_master.save()
            return redirect("/userdet")
        else:
            return redirect("/userView")
    return redirect("/userView")

def useredit(request,id):
    instance = get_object_or_404(UserMasterTable, user_master_id=id)
    if request.method == 'POST':
        form = Userform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            userMaster = UserMasterTable.objects.filter(user_master_id=id).first().user_master_id

            userDetailsId = UserDetails.objects.filter(user_master =userMaster ).first().user_deatil_id
            return redirect('/userdetedit/'+ str(userDetailsId))  # Redirect to a success page
    else:
        form = Userform(instance=instance)
    return render(request, "authentication/useredit.html",{'form':form})

def userdelete(request,id):
    user=UserMasterTable.objects.get(user_master_id=id)
    user.delete()
    return redirect("/userView")

def userView(request):
    userdt =[]
    if request.method=="POST":
        search = request.POST.get('search')
        objCity = UserMasterTable.objects.filter(user_name=search)
        for obj in objCity:
            for itme in UserDetails.objects.filter(user_master=obj):
                strenm = UserDetails.USER_TYPES(itme.user_type).name
                userdt.append({
                'user_master_id':obj.user_master_id,
                'user_email_id':obj.user_email_id,
                'user_password':obj.user_password,
                'user_name':obj.user_name,
                'user_type':strenm,
                'contact':itme.contact,
                'address':itme.address
            })
        return render(request, "authentication/user_master-list.html",{'userobj':userdt,"search":search})
    objStateMaster = UserMasterTable.objects.all()
    for obj in objStateMaster:
            for itme in UserDetails.objects.filter(user_master=obj):
                strenm = UserDetails.USER_TYPES(itme.user_type).name
                userdt.append({
                'user_master_id':obj.user_master_id,
                'user_email_id':obj.user_email_id,
                'user_password':obj.user_password,
                'user_name':obj.user_name,
                'user_type':strenm,
                'contact':itme.contact,
                'address':itme.address
            })
    print(objStateMaster)
    return render(request, "authentication/user_master-list.html",{'userobj':userdt})

    
    
    userobj = UserMasterTable.objects.all()
    userdt =[]
    for obj in userobj:
        for itme in UserDetails.objects.filter(user_master=obj):
            strenum = UserDetails.USER_TYPES(itme.user_type).name
            userdt.append({
                'user_master_id':obj.user_master_id,
                'user_email_id':obj.user_email_id,
                'user_password':obj.user_password,
                'user_name':obj.user_name,
                'user_type':strenum,
                'contact':itme.contact,
                'address':itme.address
            })
    return render(request, "authentication/user_master-list.html",{'userobj':userdt})

def review(request):
    form=Reviewform()
    reviewobj=ReviewFeedback.objects.all()
    print(reviewobj)
    return render(request, "authentication/reviewadd.html",{'form':form,'reviewobj':reviewobj})

def reviewsave(request):
    form = Reviewform()
    if request.method == 'POST':
        form = Reviewform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/review_cust")
        else:
            return redirect("/review_cust")
    return redirect("/review_cust")

def reviewedit(request,id):
    instance = get_object_or_404(ReviewFeedback, review_id=id)
    if request.method == 'POST':
        form = Reviewform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/reviewView')  # Redirect to a success page
    else:
        form = Reviewform(instance=instance)
    return render(request, "authentication/reviewedit.html",{'form':form})

# def reviewupdate(request,id):
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
    
    if request.method=="POST":
        search = request.POST.get('search')
        objReviewMaster = ReviewFeedback.objects.filter(review_id=search)
        return render(request, "authentication/review&feedback-list.html",{'reviewobj':objReviewMaster,"search":search})
    objReviewMaster = ReviewFeedback.objects.all()
    print(objReviewMaster)
    return render(request, "authentication/review&feedback-list.html",{'reviewobj':objReviewMaster})
    # objReviewMaster = ReviewFeedback.objects.all()
    # print(objReviewMaster)
    # return render(request, "authentication/review&feedback-list.html",{'reviewobj':objReviewMaster})

def complain(request):
    form=Complainform()
    complainobj=ComplainMaster.objects.all()
    print(complainobj)
    return render(request, "authentication/complainadd.html",{'form':form,'complainobj':complainobj})

def complainsave(request):
    form = Complainform()
    if request.method == 'POST':
        form = Complainform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/com_mast_cust")
        else:
            return redirect("/com_mast_cust")
    return redirect("/com_mast_cust")

def complainedit(request,id):
    instance = get_object_or_404(ComplainMaster, com_id=id)
    if request.method == 'POST':
        form = Complainform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/complainView')  # Redirect to a success page
    else:
        form = Complainform(instance=instance)
    return render(request, "authentication/complainedit.html",{'form':form})

# def complainupdate(request,id):
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
    
    if request.method=="POST":
        search = request.POST.get('search')
        objCity = ComplainMaster.objects.filter(com_id=search)
        return render(request, "authentication/complainlist.html",{'complainobj':objCity,"search":search})
    objComplainMaster = ComplainMaster.objects.all()
    # print(objStateMaster)
    return render(request, "authentication/complainlist.html",{'complainobj':objComplainMaster})
    # complainobj=ComplainMaster.objects.all()
    # print(complainobj)
    # return render(request, "authentication/complainlist.html",{'complainobj':complainobj})

def complainstatus(request):
    form = Complainstatusform()
    complainstatusobj = ComplainStatus.objects.all()
    print(complainstatusobj)    
    return render(request, "authentication/complainstatusadd.html", {'form': form, 'complainstatusobj': complainstatusobj})

def complainstatussave(request):
    form = Complainstatusform()
    if request.method == 'POST':
        form = Complainstatusform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/complainsView")
        else:
            return redirect("/complainsView")
    return redirect("/complainsView")

def complainstatusedit(request,id):
    instance = get_object_or_404(ComplainStatus, com_status_id=id)
    if request.method == 'POST':
        form = Complainstatusform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/complainView')  # Redirect to a success page
    else:
        form = Complainstatusform(instance=instance)
    return render(request, "authentication/complainsedit.html",{'form':form})

# def complainstatusupdate(request,id):
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
    form=Docdetform()
    docdetobj=DocDetail.objects.all()
    print(docdetobj)
    return render(request, "authentication/docdetadd.html",{'form':form,'docdetobj':docdetobj})

def docdetsave(request):
    form = Docdetform()
    if request.method == 'POST':
        form = Docdetform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/docdetView")
        else:
            return redirect("/docdetView")
    return redirect("/docdetView")

def docdetedit(request,id):
    instance = get_object_or_404(DocDetail, doc_detail_id=id)
    if request.method == 'POST':
        form = Docdetform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/docdetView')  # Redirect to a success page
    else:
        form = Docdetform(instance=instance)
    return render(request, "authentication/complainsedit.html",{'form':form})


def docdetdelete(request,id):
    docdet=DocDetail.objects.get(doc_detail_id=id)
    docdet.delete()
    return redirect("/docdetView")

def docdetView(request):
    docdetobj=DocDetail.objects.all()
    print(docdetobj)
    return render(request, "authentication/docdetlist.html",{'docdetobj':docdetobj})

def docvehdet(request):
    form=docvehdetform()
    docvehdet=DocVehDetailsTable.objects.all()
    print(docvehdet)
    return render(request, "authentication/docvehdet.html",{'form':form,'docvehdet':docvehdet})

def docvehdetsave(request):
    form = docvehdetform()
    if request.method == 'POST':
        form = docvehdetform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/docvehdetView")
        else:
            return redirect("/docvehdetView")
    return redirect("/docvehdetView")

def docvehdetedit(request,id):
    instance = get_object_or_404(DocVehDetailsTable, doc_veh_det_id=id)
    if request.method == 'POST':
        form = docvehdetform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/docvehdetView')  # Redirect to a success page
    else:
        form = docvehdetform(instance=instance)
    return render(request, "authentication/docvehdetedit.html",{'form':form})


def docvehdetdelete(request,id):
    docvehdet=DocVehDetailsTable.objects.get(doc_veh_det_id=id)
    docvehdet.delete()
    return redirect("/docvehdetView")

def docvehdetView(request):
    docvehdet=DocVehDetailsTable.objects.all()
    print(docvehdet)
    return render(request, "authentication/docvehdetlist.html",{'docvehdet':docvehdet})

def reviewstatus(request):
    form=Reviewstatusform()
    revstaobj=ReviewFeedbackStatus.objects.all()
    print(revstaobj)
    return render(request, "authentication/reviewstatus.html",{'form':form,'revstaobj':revstaobj})

def reviewstatussave(request):
    form = Reviewstatusform()
    if request.method == 'POST':
        form = Reviewstatusform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/reviewstatusView")
        else:
            return redirect("/reviewstatusView")
    return redirect("/reviewstatusView")

def reviewstatusedit(request,id):
    instance = get_object_or_404(ReviewFeedbackStatus, review_status_id=id)
    if request.method == 'POST':
        form = Reviewstatusform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/reviewstatusView')  # Redirect to a success page
    else:
        form = Reviewstatusform(instance=instance)
    return render(request, "authentication/complainsedit.html",{'form':form})

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
    form=Paymentform()
    paymentobj=PaymentMaster.objects.all()
    print(paymentobj)
    return render(request, "authentication/paymentadd.html",{'form':form,'paymentobj':paymentobj})

def paymentsave(request):
    form = Paymentform()
    if request.method == 'POST':
        form = Paymentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/paymentView")
        else:
            return redirect("/paymentView")
    return redirect("/paymentView")

def paymentedit(request,id):
    instance = get_object_or_404(PaymentMaster, doc_pay_detail_id=id)
    if request.method == 'POST':
        form = Paymentform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/paymentView')  # Redirect to a success page
    else:
        form = Paymentform(instance=instance)
    return render(request, "authentication/useredit.html",{'form':form})

#def paymentupdate(request,id):
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
    
    if request.method=="POST":
        search = request.POST.get('search')
        objCity = Gstcharges.objects.filter(doc_pay_detail_id=search)
        return render(request, "authentication/paymentlist.html",{'paymentobj':objCity,"search":search})
    paymentobj = Gstcharges.objects.all()
    print(paymentobj)
    return render(request, "authentication/paymentlist.html",{'gstobj':paymentobj})

def paymentView(request):
    paymentobj=PaymentMaster.objects.all()
    print(paymentobj)
    return render(request, "authentication/paymentlist.html",{'paymentobj':paymentobj})


def userdet(request):
    form=userdetform()
    userdetobj=UserDetails.objects.all()
    print(userdetobj)
    return render(request, "authentication/userdetail.html",{'form':form,'userdetobj':userdetobj})

def userdetsave(request):
    form = userdetform()
    try:
        if request.method == 'POST':
            form = userdetform(request.POST,request.FILES)
            if form.is_valid():
                print(2)
                form.save()
                return redirect("/userdetView")
            else:
                print(form.errors)
                return render(request, "authentication/userdetail.html",{'form':form})
    except Exception as e:
        print(e)
    return redirect("/userdetView")

def userdetedit(request,id):
    instance = get_object_or_404(UserDetails, user_deatil_id=id)
    if request.method == 'POST':
        form = userdetform(request.POST, request.FILES,instance=instance)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/userView')  # Redirect to a success page
    else:
        form = userdetform(instance=instance)
    return render(request, "authentication/userdetedit.html",{'form':form})

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
    form=vehroutdetform()
    vehroutdetobj=VehRoutDetalis.objects.all()
    print(vehroutdetobj)
    return render(request, "authentication/vehroutdet.html",{'form':form,'vehroutdetobj':vehroutdetobj})

def vehroutdetsave(request):
    form = vehroutdetform()
    if request.method == 'POST':
        form = vehroutdetform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/vehroutdetView")
        else:
            return redirect("/vehroutdetView")
    return redirect("/vehroutdetView")

def vehroudetedit(request,id):
    instance = get_object_or_404(VehRoutDetalis, veh_rout_det_id=id)
    if request.method == 'POST':
        form = vehroutdetform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/vehroutdetView')  # Redirect to a success page
    else:
        form = vehroutdetform(instance=instance)
    return render(request, "authentication/vehroutdetedit.html",{'form':form})

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

def newadmin(request):
    return render(request, "authentication/newadmin.html")

def myorders(request):
    form=myorderform()
    docob=DocMaster.objects.all()
    print(docob)
    return render(request, "authentication\myorders.html",{'form':form,'docob':docob})

def myorderssave(request):
    form = myorderform()
    if request.method == 'POST':
        form = Docform(request.POST)
        if form.is_valid():
            form.save()
            objDoc = DocMaster.objects.last()
            PAYMNETURL="https://secure-ptg.payphi.com/pg/api/v2/initiateSale"
            ENDPOINTURL="https://secure-ptg.payphi.com/pg/api/v2/authRedirect?tranCtx=Rda76d3e8-a3f1-4281-aadf-2b1cc56b64c1"
            MERCHANTID="T_21225"
            CURRENCYCODE="356"

            strurl=PAYMNETURL
            endpoint=ENDPOINTURL
            url = f"{strurl}/{endpoint}"
            HASKEY="abc"
            endpoint=""
            tranNumber=datetime.now().strftime('%Y%m%d%H%M%S%f')
            dtobj= datetime.now().strftime("%Y%m%d%H%M%S")
            strValue=str(objDoc.net_amount)+CURRENCYCODE+"s.nikhil4@gmail.com"+ MERCHANTID+tranNumber+"0"+"http://localhost:8000/PayphiDonatesuccess/"+"SALE"+dtobj
            hasValue = getShaStr(strValue)
            print(hasValue)
            payload =json.dumps({
                        "merchantId": MERCHANTID,
                        "merchantTxnNo": tranNumber,
                        "amount": str(objDoc.net_amount),
                        "currencyCode": "356",
                        "payType": "0",
                        "customerEmailID": "s.nikhil4@gmail.com",
                        "transactionType": "SALE",
                        "returnURL": "http://localhost:8000/myordersview/",
                        "txnDate": dtobj,
                        "secureHash": hasValue
                    })
            print(payload)
            headers = {
                    'Content-Type': 'application/json'
            }
            # ticket.payment_transaction_id=tranNumber
            resData = requests.post(strurl, headers=headers, data=payload)
            jsobj = resData.json()
            redirectUrls= jsobj['redirectURI']+"?tranCtx="+jsobj['tranCtx']
            print(redirectUrls)
            # urlobj = resData.json()
            request.success_url = redirectUrls
            return redirect(resData)
        else:
            return redirect("/myordersview")
    return redirect("/myordersview")

def myordersview(request):
    docobj1 = DocMaster.objects.all()
    print(docobj1)
    return render(request, "authentication/myordersview.html",{'docobj1':docobj1})

def registration(request):
    return render(request, "authentication/registration.html")

def com_mast_cust(request):
    obj=ComplainMaster.objects.all()
    return render(request, "authentication/com_mast_cust.html",{'obj':obj})

def review_cust(request):
    obj=ReviewFeedback.objects.all()
    return render(request, "authentication/review_cust.html",{'obj':obj})

def register(request):
    uemail=request.POST.get('email')
    uname=request.POST.get('username')
    password=request.POST.get('userpassword')
    user=UserMasterTable1(user_email_id=uemail,user_name=uname,user_password=password)
    user.save()
    return redirect("/home")

def homepage(request):
    return render(request, "authentication/homepage.html")

def homeservice(request):
    return render(request, "authentication/homeservice.html")

def homeabout(request):
    return render(request, "authentication/homeabout.html")

def homecontact(request):
    return render(request, "authentication/homecontact.html")

