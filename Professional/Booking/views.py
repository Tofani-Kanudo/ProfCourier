from django.shortcuts import render,redirect
from Booking.models import party,apod,book,p_user,branch,content,origin,location,price
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.views.generic import View
from django.template.loader import get_template
from .pdf import render_to_pdf
import datetime
from django.db.models import Min
# Create your views here.
mode=""
sau=["RAJKOT","BHAVNAGAR","JUNAGADH","SURENDRANAGAR","PORBANDAR","AMRELI","MORBI"]
west=["Maharastra","Rajasthan","MadhyaPradesh","Goa"]
sp=["PONDICHERRY","Andaman and Nico.In.","Jammu and Kashmir","HimachalPradesh"]
def start(request):
    if request.user:
        logout(request)
    return render(request,'index.html',{})
def u_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return ways(request)
            else:
                return HttpResponse("Account Deactivated")
        else:
            print("Login Failed")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("Invalid Login Details")
    if request.method=='GET':
        return start(request)
@login_required
def ways(request):
    if request.user.is_superuser:
        return redirect('cont')
    else:
        return redirect('book/')
@login_required
def br(request):
    if request.user.admin or request.user.is_superuser:
        z=branch.objects.filter(origin=request.user.origin)
        b=request.POST.get('bulk',False)
        if b==False:
            b='false'
        return render(request,'nor.html',{'branches':z,'b':b})
    else:
        u=apod.objects.filter(p_user=request.user)
        u=u.aggregate(Min('apod'))
        u=u['apod__min']
        v=branch.objects.filter(branch=request.user.branches)
        b=request.POST.get('bulk',False)
        if b==False:
            b='false'
        return render(request,'nor.html',{'apod':u,'branches':v,'b':b})
@login_required
def save(request):
    global mode,sau,west,sp
    if request.method=='POST':
        try:
            mod=request.POST.get('mode',"")
            if mode!="":
                if mode!=mod:
                    raise ValueError
            if request.POST.get('Amount','')=='0':
                raise ValueError
            number,name,address1,address2,city,email,gst=request.POST['number'],request.POST['shipper'],request.POST['add1'],request.POST['add2'],request.POST['city'],request.POST.get('email',""),request.POST.get('gst',"")
            if number=="" or name=="" or address1=="" or city=="":
                raise ValueError
            s=party(number=number,name=name,address1=address1,address2=address2,city=city,email=email,gst=gst,reference=request.POST.get('ref',''),phone=request.POST.get('phone',''))
            number,name,address1,address2,city,email,gst=request.POST['numbers'],request.POST['cons'],request.POST['adds1'],request.POST['adds2'],request.POST['citys'],request.POST.get('emails',""),request.POST.get('gsts',"")
            if number=="" or name=="" or address1=="" or city=="":
                raise ValueError
            c=party(number=number,name=name,address1=address1,address2=address2,city=city,email=email,gst=gst,company=request.POST.get('company',''))
            s.save()
            c.save()
            pod,booktype,bra,dest,nop,Weight,Amount,value,content=request.POST['pod'],request.POST['book'],request.POST['branch'],request.POST['destination'],int(request.POST['nop']),request.POST['Weight'],request.POST['Amount'],request.POST.get('value',""),request.POST.get('content',"")
            q=book(pod=pod,booktype=booktype,sender=s,branch=bra,reciever=c,destination=dest,nop=nop,weight=Weight,amount=Amount,value=value,content=content,p_user=request.user)
            q.save()
            apod.objects.filter(apod=q).delete()
            print("Reached almost")
            if not request.POST.get('bulk',False):
                print("Reached")
                return GeneratePDF.as_view()(request)
            else:
                return br(request)
        except :
            w=party.objects.filter(number=request.POST.get('number',""))
            if w:
                w=w[0]
                if request.POST.get('shipper','')!=''!=w.name or request.POST.get('add1','')!=''!=w.address1 or request.POST.get('add2','')!=''!=w.address2 or request.POST.get('city','')!=''!=w.city or request.POST.get('email',"")!=''!=w.email or request.POST.get('gst',"")!=''!=w.gst:
                    number,name,address1,address2,city,email,gst=request.POST.get('number',''),request.POST.get('shipper',''),request.POST.get('add1',''),request.POST.get('add2',''),request.POST.get('city',''),request.POST.get('email',""),request.POST.get('gst',"")
                    w=party(number=number,name=name,address1=address1,address2=address2,city=city,email=email,gst=gst,reference=request.POST.get('ref',''),phone=request.POST.get('phone',''))
            else:
                number,name,address1,address2,city,email,gst=request.POST.get('number',''),request.POST.get('shipper',''),request.POST.get('add1',''),request.POST.get('add2',''),request.POST.get('city',''),request.POST.get('email',""),request.POST.get('gst',"")
                w=party(number=number,name=name,address1=address1,address2=address2,city=city,email=email,gst=gst,reference=request.POST.get('ref',''),phone=request.POST.get('phone',''))
            c=party.objects.filter(number=request.POST.get('numbers',""))
            if c:
                c=c[0]
                if request.POST.get('cons','')!=''!=c.name or request.POST.get('adds1','')!=''!=c.address1 or request.POST.get('adds2','')!=''!=c.address2 or request.POST.get('citys','')!=''!=c.city or request.POST.get('emails',"")!=''!=c.email or request.POST.get('gsts',"")!=''!=c.gst or request.POST.get('company')!=''!=c.company or request.POST.get('phone','')!=''!=c.phone:
                    number,name,address1,address2,city,email,gst,company,phone=request.POST.get('numbers',''),request.POST.get('cons',''),request.POST.get('adds1',''),request.POST.get('adds2',''),request.POST.get('citys',''),request.POST.get('emails',""),request.POST.get('gsts',""),request.POST.get('company'),request.POST.get('phone','')
                    c=party(number=number,name=name,address1=address1,address2=address2,city=city,email=email,gst=gst,company=company,phone=phone)
            else:
                number,name,address1,address2,city,email,gst,company,phone=request.POST.get('numbers',''),request.POST.get('cons',''),request.POST.get('adds1',''),request.POST.get('adds2',''),request.POST.get('citys',''),request.POST.get('emails',""),request.POST.get('gsts',""),request.POST.get('company'),request.POST.get('phone','')
                c=party(number=number,name=name,address1=address1,address2=address2,city=city,email=email,gst=gst,company=company,phone=phone)
            u=apod.objects.filter(apod=request.POST.get('pod',""))
            if u:
                u=u[0]
            else:
                u=""
            if request.POST.get('pin',0)=='':
                a=0
            else:
                a=request.POST.get('pin',0)
            l=location.objects.filter(pincode=a)
            z=branch.objects.filter(origin=request.user.origin)
            b=request.POST.get('bulk',False)
            if b==False:
                b='false'
            bo=request.POST.get('book',"")
            bra=request.POST.get('branch',"")
            if l:
                l=l[0]
                l.district.capitalize()
                l.state.capitalize()
            else:
                l=""
            mode=request.POST.get('mode',"")
            if mode=="Surface" and l:
                if w.sur_price:
                    pr=w.sur_price
                else:
                    pr=price.objects.filter(first_local=5)
                    pr=pr[0]
                    if l.state!="Gujarat":
                        if l.state in west:
                            if l.district=='Mumbai':
                                fpr=pr.first_metro
                                pr=pr.metro
                            else:
                                fpr=pr.first_west
                                pr=pr.west
                        elif l.state in sp or l.district in sp:
                            fpr=pr.first_spec
                            pr=pr.spec
                        else:
                            if l.district=='Delhi':
                                fpr=pr.first_metro
                                pr=pr.metro
                            else:
                                fpr=pr.first_ROI
                                pr=pr.ROI
                    else:
                        if l.district in sau:
                            fpr=pr.first_sau
                            pr=pr.sau
                        elif l.district == "Jamnagar":
                            fpr=pr.first_local
                            pr=pr.local
                        else:
                            fpr=pr.first_guj
                            pr=pr.guj
            elif mode=="Air" and l:
                if w.air_price:
                    pr=w.air_price
                else:
                    pr=price.objects.filter(first_local=10)
                    pr=pr[0]
                    if l.state!="Gujarat":
                        if l.state in west:
                            if l.district=='Mumbai':
                                fpr=pr.first_metro
                                pr=pr.metro
                            else:
                                fpr=pr.first_west
                                pr=pr.west
                        elif l.state in sp or l.district in sp:
                            fpr=pr.first_spec
                            pr=pr.spec
                        else:
                            if l.district=='Delhi':
                                fpr=pr.first_metro
                                pr=pr.metro
                            else:
                                fpr=pr.first_ROI
                                pr=pr.ROI
                    else:
                        if l.district in sau:
                            fpr=pr.first_sau
                            pr=pr.sau
                        elif l.district == "Jamnagar":
                            fpr=pr.first_local
                            pr=pr.local
                        else:
                            fpr=pr.first_guj
                            pr=pr.guj
            else:
                pr=""
                fpr=""
            print(fpr,pr)
            nop=request.POST.get('nop','')
            wt=request.POST.get('Weight','')
            return render(request,'nor.html',{'party':w,'apod':u,'branches':z,'b':b,'loc':l,'cons':c,'book':bo,'branch':br,'mode':mode,'fpr':fpr,'pr':pr,'nop':nop,'wt':wt})
    else:
        return render(request,'nor.html',{'party':w,'apod':u,'branches':z,'b':b,'loc':l,'cons':c,'book':bo,'branch':br,'mode':mode,'fpr':fpr,'pr':pr,'nop':nop,'wt':wt})
@login_required
def cont(request):
    if request.user.is_superuser:
        if request.method=='POST':
            if request.POST.get('newstext',False):
                content(content=request.POST['newstext'],author=request.user).save()
        c=content.objects.all()
        return render(request,'superad.html',{'content':c,'user':request.user})
    return start(request)
@login_required
def delete(request,todo_id):
    itemdel = content.objects.get(id=todo_id)
    itemdel.delete()
    return ways(request)
@login_required
def register(request):
    if request.user.is_superuser:
        if request.method=='POST':
            a=request.POST.get('admin',False)
            o=origin.objects.get(origin=request.POST['origin'])
            b=branch.objects.get(branch=request.POST['branch'])
            if a=='on':
                a=p_user(username=request.POST['username'],password=request.POST['password'],origin=o,branches=b,admin=True,is_superuser=False)
            else:
                a=request.POST.get('superadmin',False)
                if a=='on':
                    a=p_user(username=request.POST['username'],password=request.POST['password'],origin=o,branches=b,admin=False,is_superuser=True,is_staff=True)
                else:
                    a=p_user(username=request.POST['username'],password=request.POST['password'],origin=o,branches=b,admin=False,is_superuser=False)
            # a=p_user(username=request.POST['username'],password=request.POST['password'],origin=o,branches=b)
            a.set_password(a.password)
            a.save()
        o=origin.objects.all()
        b=branch.objects.all()
        return render(request,'register.html',{'user':request.user,'origin':o,'branches':b})
    return start(request)
@login_required
def reg_page(request):
    if request.user.is_superuser:
        o=origin.objects.all()
        b=branch.objects.all()
        return render(request,'register.html',{'user':request.user,'origin':o,'branches':b})
    return start(request)
@login_required
def pod_pg(request):
    if request.user.is_superuser:
    # if request.method=='GET':
        b=p_user.objects.all()
        return render(request,'pod.html',{'users':b})
    return start(request)
@login_required
def pod(request):
    if request.user.is_superuser:
        if request.method=='GET':
            a=int(request.GET['from'])
            c=p_user.objects.get(username=request.GET['user'])
            if request.GET['to']=="":
                apod(apod=a,p_user=c).save()
            else:
                b=int(request.GET['to'])
                for i in range(a,b+1):
                    apod(apod=i,p_user=c).save()
        return pod_pg(request)
    return start(request)
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_logout(request):
    if request.method=='POST':
        logout(request)
    return HttpResponseRedirect('/')
@login_required
def search(request):
    if request.method=='GET':
        st=request.GET.get('searchbox')
        res=book.objects.filter(pod__icontains=st)
        s=party.objects.filter(number__icontains=st)
        resu=book.objects.filter(sender__in=s)
        if res or resu:
            return render(request,'search.html',{'result':res,'resu':resu})
        else:
            return HttpResponse("No result found")
class GeneratePDF(View):
    def get(self, request, id, *args, **kwargs):
        b=book.objects.get(pod=id)
        context = {
            "num": str(request.user.origin)+str(b.pod),
            "cust": b.sender.name,
            "no": b.sender.number,
            "pho": b.sender.phone,
            "phos": b.reciever.phone,
            "date": b.time,
            "add1": b.sender.address1,
            "add2": b.sender.address2,
            "nu": b.reciever.number,
            "cons": b.reciever.name,
            "adds1": b.reciever.address1,
            "adds2": b.reciever.address2,
            "dest": b.destination,
            "weight": b.weight,
            "amount": b.amount,
        }
        return render(request,'receipt.html',context)
    def post(self, request, *args, **kwargs):
        template = get_template('receipt.html')
        context = {
            "num": str(request.user.origin)+request.POST['pod'],
            "cust": request.POST['shipper'],
            "no": request.POST['number'],
            "pho": request.POST['phone'],
            "phos": request.POST['phones'],
            "date": datetime.datetime.now().strftime("%d")+" "+datetime.datetime.now().strftime("%B")+" "+datetime.datetime.now().strftime("%Y"),
            "add1": request.POST['add1'],
            "add2": request.POST['add2'],
            "nu": request.POST['numbers'],
            "cons": request.POST['cons'],
            "adds1": request.POST['adds1'],
            "adds2": request.POST['adds2'],
            "dest": request.POST['destination'],
            "weight": request.POST['Weight'],
            "amount": request.POST['Amount'],
        }
        html = template.render(context)
        pdf = render_to_pdf('receipt.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %(datetime.datetime.now())
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
