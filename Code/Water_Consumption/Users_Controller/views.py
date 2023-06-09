from django.db.models import Count
from django.shortcuts import render, redirect

# Create your views here.
from Users_Controller.models import Userregisters_Model, Userwateranalysis_Model, Userfeedback_Model


def index(request):
    return render(request, 'users/index.html')
def base(request):
    return render(request, 'users/base.html')

def user_logins(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        try:
            enter = Userregisters_Model.objects.get(name=name,password=password)
            request.session["name"]= enter.id
            return redirect('user_wateranalysis')
        except:
            pass

    return render(request, 'users/user_logins.html')

def user_registers(request):

    if request.method == "POST":
        userid= request.POST.get('userid')
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        address = request.POST.get('address')
        Userregisters_Model.objects.create(userid=userid,name=name,password=password,email=email,phoneno=phoneno,address=address)

    return render(request, 'users/user_registers.html')

def user_wateranalysis(request):
    name = request.session['name']
    obj = Userregisters_Model.objects.get(id=name)



    if request.method =="POST":
        useridorbillno = request.POST.get("useridorbillno")
        branch = request.POST.get("branch")
        now = request.POST.get("now")
        nol = request.POST.get("nol")
        amount = request.POST.get("amount")
        wpd = request.POST.get("wpd")
        receipt = request.POST.get("receipt")
        bookdate = request.POST.get("bookdate")
        deliverydate = request.POST.get("deliverydate")
        Userwateranalysis_Model.objects.create(uregid=obj,useridorbillno=useridorbillno,branch=branch,now=now,nol=nol,amount=amount,wpd=wpd,receipt=receipt,bookdate=bookdate,deliverydate=deliverydate)


    return render(request, 'users/user_wateranalysis.html')

def user_feedback(request):
    name = request.session['name']
    userObj = Userregisters_Model.objects.get(id=name)
    result = ''
    pos = []
    neg = []
    oth = []
    se = 'se'
    if request.method == "POST":
        name = request.POST.get('name')
        branches = request.POST.get('branches')
        rating = request.POST.get('rating')
        mobilenumber = request.POST.get('mobilenumber')
        emailid = request.POST.get('emailid')
        twt = request.POST.get('feedback')

        if '#' in twt:
            startingpoint = twt.find('#')
            a = twt[startingpoint:]
            endingPoint = a.find(' ')
            title = a[0:endingPoint]
            result = title[1:]
        # return redirect('tweetpage')

        for f in twt.split():
            if f in ('good', 'nice', 'beteer', 'best', 'excellent', 'extraordinary', 'happy', 'wonder', 'love', 'greate',):
                pos.append(f)
            elif f in ('worst', 'waste', 'poor', 'worsttaste', 'advance amount', 'extrachage', 'late', 'imporve', 'bad', 'unhealthy'):
                neg.append(f)
            else:
                oth.append(f)
        if len(pos) > len(neg):
            se = 'positive'
        elif len(neg) > len(pos):
            se = 'negative'
        else:
            se = 'nutral'
        Userfeedback_Model.objects.create(uregsid=userObj,name=name,branches=branches,rating=rating,mobilenumber=mobilenumber,sentiment=se ,topics=result, feedback=twt, )
    obj = Userfeedback_Model.objects.all()






    return render(request, 'users/user_feedback.html',{'list_objects': obj,'result':result,'se':se})


def ucharts(request,chart_type):
    chart = Userfeedback_Model.objects.values('topics').annotate(dcount=Count('sentiment'))

    return render(request,"users/ucharts.html", {'form':chart, 'chart_type':chart_type})

