from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect, get_object_or_404

#database imports
from vprofile.models import *
from django.db.models import Sum
from .forms import RuleForm
from collections import OrderedDict

#time imports
from django.utils.timezone import utc
import datetime
from dateutil.relativedelta import relativedelta

#authentication imports
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

#time functions:
def first_day_of_month(d):
    return datetime.date(d.year, d.month, 1)

def get_today():
    #change the value here - hardcoded 3-06-2015 22:30
    date_string = '03-06-2015 22:30'
    date_format = '%d-%m-%Y %H:%M'
    today = datetime.datetime.strptime(date_string, date_format)
    #today = datetime.datetime.today()
    return today

def get_n_months_ago_date(n):
    today = get_today()
    return today + relativedelta(months=-(n))

def get_n_months_ago_date_ref(date, n):
    return date + relativedelta(months=-(n))


# login_decorators
def user_login_required(f):
    def wrap(request, *args, **kwargs):
        if 'userid' not in request.session.keys():
            return redirect('login')
        return f(request, *args, **kwargs)
    wrap.__doc__ = f.__doc__
    wrap.__name__= f.__name__
    return wrap
            
        
# Create your views here.
def auth_method(request):
    template = loader.get_template('profile/auth.html')
    username = '';
    password = '';
    state = 'Insert credentials'
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = 'Success'
                client = Client.objects.get(user=user)
                request.session['userid'] = client.id
                return redirect('dashboard')
                
            else:
                state = 'Account not active'
        else:
            state = 'Username/Password incorrect'
    context = RequestContext(request, {
     'state': state, 
     'username': username,
    })
    return HttpResponse(template.render(context))
                
def home(request):
    client_list = Client.objects.all()
    template = loader.get_template('profile/index.html')
    context = {
        'client_list' : client_list,
    }
    return redirect('login')
    return HttpResponse(template.render(context))

@user_login_required 
def dashboard(request):
    template = loader.get_template('profile/dashboard.html')
    
    client = Client.objects.get(user = request.user)
    news = News.objects.filter(active = True).order_by('-date')
    services_list = ServiceType.objects.all()
    top_5_sites = SiteAccess.objects.order_by('-num_accesses')[:5]

    today = get_today() 

    dashboard_dict={}
    dashboard_dict_m1={}
    dashboard_dict_m2={}
    dashboard_dict_m3={}
   
    #PIE CHARTS stats 
    #filter by client_id, month and year. Sum of all num_accesses fields corresponding to 
    #a specific service
    for s in services_list:
        crt_service_access =  ServiceUtilizationStatistics.objects.filter(client=client.id, 
                                                    date__month=today.month, #stats from current month (not day) 
                                                    date__year=today.year,
                                                    service=s).aggregate(Sum('num_accesses'))
        #criteria returns nothing
        dashboard_dict[s.service_name] = crt_service_access.values()[0] if crt_service_access.values()[0] != None else 0 
    
        
        date_old = get_n_months_ago_date(1)
        crt_service_access_m1 =  ServiceUtilizationStatistics.objects.filter(client=client.id, 
                                                    date__month=date_old.month,  
                                                    date__year=date_old.year ,  
                                                    service=s).aggregate(Sum('num_accesses'))
        #criteria returns nothing
        dashboard_dict_m1[s.service_name] = crt_service_access_m1.values()[0] if crt_service_access_m1.values()[0] != None else 0

        date_older = get_n_months_ago_date(2) 
        crt_service_access_m2 =  ServiceUtilizationStatistics.objects.filter(client=client.id, 
                                                    date__month=date_older.month,  
                                                    date__year=date_older.year ,  
                                                    service=s).aggregate(Sum('num_accesses'))
        #criteria returns nothing
        dashboard_dict_m2[s.service_name] = crt_service_access_m2.values()[0] if crt_service_access_m2.values()[0] != None else 0

        date_oldest = get_n_months_ago_date(3) 
        crt_service_access_m3 =  ServiceUtilizationStatistics.objects.filter(client=client.id, 
                                                    date__month=date_oldest.month,  
                                                    date__year=date_oldest.year ,  
                                                    service=s).aggregate(Sum('num_accesses'))
        #criteria returns nothing
        dashboard_dict_m3[s.service_name] = crt_service_access_m3.values()[0] if crt_service_access_m3.values()[0] != None else 0

    #TOP GLOBAL SITES STATS
    top_rate_sites_matrix = []
    for sa in top_5_sites:
        top_rate_sites_matrix.append([sa.url, sa.num_accesses])


    context = RequestContext(request, {
        'dashboard_dict':OrderedDict(sorted(dashboard_dict.items(), key = lambda t: t[0])),
        'dashboard_dict_m1':OrderedDict(sorted(dashboard_dict_m1.items(), key = lambda t: t[0])),
        'dashboard_dict_m2':OrderedDict(sorted(dashboard_dict_m2.items(), key = lambda t: t[0])),
        'dashboard_dict_m3':OrderedDict(sorted(dashboard_dict_m3.items(), key = lambda t: t[0])),
        'top_rate_sites_matrix':top_rate_sites_matrix,
        'news': news,
        'client': client,
        'year': today.year,
        'month': (today.month - 1) % 12, #google charts: months starts from 00 - January
        'day': today.day,
        'hours': today.hour,
        'minutes': today.minute,
        
        
    })
    return HttpResponse(template.render(context))

@user_login_required 
def stats(request):
    today = get_today() 

    template = loader.get_template('profile/advanced_statistics.html')
    client = Client.objects.get(user = request.user)
    context = RequestContext(request, {
        'today': today.strftime("%d-%m-%Y"),
        'min_date': get_n_months_ago_date_ref(first_day_of_month(today), 3).strftime("%d-%m-%Y"),
    })
    return HttpResponse(template.render(context))

@user_login_required 
def stats_date(request):

    client = Client.objects.get(user = request.user)
    template = loader.get_template('profile/stats_by_date.html')
    
    #date format returned by datepicker
    date_format = '%d-%m-%Y'
    start_date = datetime.datetime.strptime(request.POST['datepicker-start'], date_format)
    end_date = datetime.datetime.strptime(request.POST['datepicker-end'], date_format)
    
    tag_list = ServiceType.objects.all().order_by('service_name');

    next_day = end_date + datetime.timedelta(days = 1) # range is not inclusive so it necessary the date of the next day
    traffic_per_timeslot = {} 

    for i in range(0, 24):
        crt_hours_range_dict = {}
        for s in tag_list:
            if start_date < end_date:
                #data range
                crt_service_accesses = ServiceUtilizationStatistics.objects.filter(
                                                        date__range=[start_date.strftime("%Y-%m-%d"), 
                                                                     next_day.strftime("%Y-%m-%d")], #range is not inclusive
                                                        client = client.id,
                                                        service = s,
                                                        date__hour=i, 
                                                            ).aggregate(Sum('num_accesses', 
                                                                                        default=0))
            elif start_date == end_date:
                #stats from the same day
                crt_service_accesses = ServiceUtilizationStatistics.objects.filter(
                                                        date__year = start_date.year,
                                                        date__month = start_date.month,
                                                        date__day = start_date.day,
                                                        date__hour = i,
                                                        client = client.id,
                                                        service = s,).aggregate(Sum('num_accesses', default=0))
            else:
                crt_service_accesses = []

            if crt_service_accesses.values()[0] != None: #no criteria match, no traffic stats stored 
                crt_hours_range_dict[s.service_name] = crt_service_accesses.values()[0]
            else:
                crt_hours_range_dict[s.service_name] = 0

        traffic_per_timeslot[str(i).zfill(2) + ":00" +"-" + str(i).zfill(2) + ":59"] = OrderedDict(sorted(crt_hours_range_dict.items(),
                                                                                                          key = lambda t: t[0]))

    context = RequestContext(request, {
        'traffic_per_timeslot': OrderedDict(sorted(traffic_per_timeslot.items(), key=lambda t: t[0])),
        'tag_list': tag_list,
        'start_date': start_date.strftime("%Y-%b-%d"),
        'end_date': end_date.strftime("%Y-%b-%d"),
        
        
    })

    return HttpResponse(template.render(context))

def compute_total_bandwidth(request):
    client = Client.objects.get(user = request.user)
    rules_list = Rule.objects.filter(client = client.id) 
    bandwidth_total = 0
    
    for rule in rules_list: 
        bandwidth_total = bandwidth_total + rule.bandwidth_percent
    return bandwidth_total

def manage(request):
    client = Client.objects.get(user = request.user)
    rules_list = Rule.objects.filter(client = client.id) 
    template = loader.get_template('profile/resources_mng.html')
    context = RequestContext(request, {
        'rules_list': rules_list,
        'total_bw_used' : 100 - compute_total_bandwidth(request),
        })
    return HttpResponse(template.render(context))

#send client, not client id
def rule_edit(request):
    client = Client.objects.get(user = request.user)
    bandwidth_total = compute_total_bandwidth(request) 

    if request.method == "POST":
        form = RuleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.client = client
            if post.bandwidth_percent + bandwidth_total <= 100:
                post.save()
            return redirect('manage')
    else:
        form = RuleForm()
    return render(request, 'profile/rule_edit.html', {'form':form})

def rule_update(request, pk):

    bandwidth_total = compute_total_bandwidth(request) 
    rule = get_object_or_404(Rule, pk=pk)
    crt_bandwidth = rule.bandwidth_percent

    if request.method == "POST":
        form = RuleForm(request.POST, instance=rule)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if post.bandwidth_percent + bandwidth_total - crt_bandwidth <= 100:
                post.save()
            return redirect('manage')
    else:
        form = RuleForm(instance=rule)
    return render(request, 'profile/rule_edit.html', {'form':form})

def rule_delete(request, pk):
    client = Client.objects.get(user = request.user)
    rule = get_object_or_404(Rule, pk=pk)
    rule.delete()
    return redirect('manage')

def offers(request):
    client = Client.objects.get(user = request.user)
    offers_list = Offer.objects.all() 
    template = loader.get_template('profile/offers.html')
    context = RequestContext(request, {
        'offers_list': offers_list,
        })
    return HttpResponse(template.render(context))

def transactions(request):
    client = Client.objects.get(user = request.user)
    template = loader.get_template('profile/transaction_hist.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))

