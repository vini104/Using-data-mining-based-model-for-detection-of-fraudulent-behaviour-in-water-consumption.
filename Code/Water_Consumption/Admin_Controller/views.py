from django.db.models import Count
from django.shortcuts import render, redirect


# Create your views here.
from Users_Controller.models import Userfeedback_Model, Userwateranalysis_Model


def base1(request):
    return render(request,'admins/base1.html')

def admin_login(request):
    if request.method =="POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name=='admin' and password == 'admin':
            return redirect('admin_viewfeedback')

    return render(request,'admins/admin_login.html')

def viewalldetails(request):
    objes = Userwateranalysis_Model.objects.all()

    return render(request, 'admins/viewalldetails.html',{'objes':objes})


def admin_viewfeedback(request):


    obj = Userfeedback_Model.objects.all()


    return render(request,'admins/admin_viewfeedback.html',{'objects':obj})

def viewtreandingtopics(request,chart_type):
    dd = {}
    pos,neu,neg =0,0,0
    poss=None
    topic = Userfeedback_Model.objects.values('topics').annotate(dcount=Count('topics')).order_by('-dcount')
    for t in topic:
        topics=t['topics']
        pos_count=Userfeedback_Model.objects.filter(topics=topics).values('sentiment').annotate(topiccount=Count('topics'))
        poss=pos_count
        for pp in pos_count:
            senti= pp['sentiment']
            if senti == 'positive':
                pos= pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics]=[pos,neg,neu]
    return render(request,'admins/viewtreandingtopics.html',{'object':topic,'dd':dd,'chart_type':chart_type})

def negativefeedbacktivechart(request,chart_type):
    dd = {}
    pos, neu, neg = 0, 0, 0
    poss = None
    topic = Userfeedback_Model.objects.values('topics').annotate(dcount=Count('topics')).order_by('-dcount')
    for t in topic:
        topics = t['topics']
        pos_count = Userfeedback_Model.objects.filter(topics=topics).values('sentiment').annotate(topiccount=Count('topics'))
        poss = pos_count
        for pp in pos_count:
            senti = pp['sentiment']
            if senti == 'positive':
                pos = pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics] = [pos, neg, neu]
    return render(request,'admins/negativefeedbacktivechart.html',{'object':topic,'dd':dd,'chart_type':chart_type})


def charts(request,chart_type):
    chart = Userfeedback_Model.objects.values('topics').annotate(dcount=Count('sentiment'))

    return render(request,"admins/charts.html", {'form':chart, 'chart_type':chart_type})

