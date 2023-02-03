from django.shortcuts import render,redirect
from furnitureweb.models import logindb


# Create your views here.
from koppee.models import catdb,furnituredb,contactdb


def homepage(request):
    data=catdb.objects.all()
    product = furnituredb.objects.all()
    context = {
        'product': product,
        'data': data,
    }
    return render(request,"home.html",context)

def aboutpage(request):
    return render(request,"aboutus.html")
def contactpage(request):
    return render(request,"contactus.html")

def discategory(request,itemcatg):
    data=catdb.objects.all()
    print("===itemcatg===",itemcatg)
    catg=itemcatg.upper()
    products=furnituredb.objects.filter(Category=itemcatg)
    context={
        'products':products,
        'catg':catg,
        'data':data
    }
    return render(request,"categorydisplay.html",context)

def coffeedetails(request,dataid):
    data=furnituredb.objects.get(id=dataid)
    return render(request,"furnituredetails.html",{'dat':data})

def pagelogin(request):
    return render(request,"login.html")

def logindata(request):
    if request.method == "POST":
        us = request.POST.get('username')
        il = request.POST.get('mail')
        pd = request.POST.get('pswrd1')
        cd = request.POST.get('cnfrm1')
        if pd == cd:
           obj = logindb(username=us,email=il, password=pd, confirmpassword=cd)
           obj.save()
           return redirect(pagelogin)
        else:
            return render(request,'login.html')


def registerdata(request):
    if request.method == "POST":
        us = request.POST.get('username')
        pd = request.POST.get('pswrd1')
        if logindb.objects.filter(username=us, password=pd).exists():
            # obj = LoginRegister(UserName=un, Password=pd).values('email','id').first()
            request.session['username'] = us
            request.session['pswrd1'] = pd
            # request.session['email']=data['email']
            # request.session['userid']=data['id']
            return redirect(homepage)
        else:

            return render(request, 'login.html', {'msg': "Sorry... password not matched."})


def logoutp(request):
    del request.session['username']
    del request.session['pswrd1']
    return redirect(homepage)

def contactsave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('mail')
        sub = request.POST.get('subject')
        ms = request.POST.get('msg')
    obj = contactdb(name=na, mail=em, subject=sub, msg=ms)
    obj.save()
    return redirect(contactpage)
