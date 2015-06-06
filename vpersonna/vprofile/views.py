from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils.timezone import utc
from collections import OrderedDict
from .forms import RuleForm
import datetime
from django.shortcuts import redirect, get_object_or_404
from vprofile.models import *
from django.db.models import Sum


# Create your views here.
def home(request):
    client_list = Client.objects.all()
    template = loader.get_template('profile/index.html')
    context = {
        'client_list' : client_list,
    }
    return HttpResponse(template.render(context))
    #return redirect('/dashboard')
    
def dashboard(request, client_id):
    template = loader.get_template('profile/dashboard.html')
    
    client = Client.objects.get(id = client_id)
    news = News.objects.filter(active = True).order_by('-date')
    services_list = ServiceType.objects.all()
    top_5_sites = SiteAccess.objects.order_by('-num_accesses')[:5]

    #today - need change
    date_string = '03-06-2015 22:30'
    date_format = '%d-%m-%Y %H:%M'
    today = datetime.datetime.strptime(date_string, date_format)

    dashboard_dict={}
    dashboard_dict_m1={}
    dashboard_dict_m2={}
    dashboard_dict_m3={}
   
    #PIE CHARTS stats 
    #filter by client_id, month and year. Sum of all num_accesses fields corresponding to 
    #a specific service
    for s in services_list:
        crt_service_access =  ServiceUtilizationStatistics.objects.filter(client=client_id, 
                                                    date__month=today.month, 
                                                    date__year=today.year,
                                                    service=s).aggregate(Sum('num_accesses'))
        dashboard_dict[s.service_name] = crt_service_access.values()[0]
    
        crt_service_access_m1 =  ServiceUtilizationStatistics.objects.filter(client=client_id, 
                                                    date__month=(today.month - 1), #possible error for january 
                                                    date__year=(today.year + ((today.month - 1)/12)),#install dateutils
                                                    service=s).aggregate(Sum('num_accesses'))
        dashboard_dict_m1[s.service_name] = crt_service_access_m1.values()[0]

        crt_service_access_m2 =  ServiceUtilizationStatistics.objects.filter(client=client_id, 
                                                    date__month=(today.month - 2), #possible error for january 
                                                    date__year=(today.year + ((today.month - 2)/12)),
                                                    service=s).aggregate(Sum('num_accesses'))
        dashboard_dict_m2[s.service_name] = crt_service_access_m2.values()[0]

        crt_service_access_m3 =  ServiceUtilizationStatistics.objects.filter(client=client_id, 
                                                    date__month=(today.month - 3), #possible error for january 
                                                    date__year=(today.year + ((today.month - 3)/12)),
                                                    service=s).aggregate(Sum('num_accesses'))
        dashboard_dict_m3[s.service_name] = crt_service_access_m3.values()[0]

    #TOP GLOBAL SITES STATS
    top_rate_sites_matrix = []
    for sa in top_5_sites:
        top_rate_sites_matrix.append([sa.url, sa.num_accesses])


    context = RequestContext(request, {
        'dashboard_dict':dashboard_dict,
        'dashboard_dict_m1':dashboard_dict_m1,
        'dashboard_dict_m2':dashboard_dict_m2,
        'dashboard_dict_m3':dashboard_dict_m3,
        'top_rate_sites_matrix':top_rate_sites_matrix,
        'client_id': client_id,
        'client': client,
        'year': today.year + ((today.month - 3) / 12),
        'month': (today.month - 1) % 12,
        'day': today.day,
        'hours': today.hour,
        'minutes': today.minute,
        'news': news,
        
        
    })
    return HttpResponse(template.render(context))
    #	return render(request, 'profile/dashboard.html', {})

def stats(request, client_id):
    #today - need change
    today = '03-06-2015'


    template = loader.get_template('profile/advanced_statistics.html')
    client = Client.objects.get(id = client_id)
    context = RequestContext(request, {
        'client_id': client_id,
        'today': today,
    })
    return HttpResponse(template.render(context))

def stats_date(request, client_id):

    #today - need change
    date_format = '%d-%m-%Y'
    
    client = Client.objects.get(id = client_id)
    template = loader.get_template('profile/stats_by_date.html')
    start_date = datetime.datetime.strptime(request.POST['datepicker-start'], date_format)
    end_date = datetime.datetime.strptime(request.POST['datepicker-end'], date_format)
    
    #tag_list = [ 'VoIP', 'HTTP (non-video)', 'BitTorent', 'Video' ]
    tag_list = ServiceType.objects.all();

    #traffic_per_timeslot = {
    #        '08-10': {
    #            'VoIP': 10, 'HTTP (non-video)': 20, 'BitTorrent': 30, 'Video': 15
    #            },
    #        '10-12': {
    #            'VoIP': 10, 'HTTP (non-video)': 20, 'BitTorrent': 30, 'Video': 15
    #            },
    #        '12-14': {
    #            'VoIP': 5, 'HTTP (non-video)': 2, 'BitTorrent': 20, 'Video': 5
    #            },
    #        '14-16': {
    #            'VoIP': 1, 'HTTP (non-video)': 0, 'BitTorrent': 0, 'Video': 1
    #            },
    #        '16-18': {
    #            'VoIP': 3, 'HTTP (non-video)': 4, 'BitTorrent': 4, 'Video': 3
    #            },
    #        '18-20': {
    #            'VoIP': 5, 'HTTP (non-video)': 2, 'BitTorrent': 17, 'Video': 20
    #            },
    #        '20-22': {
    #            'VoIP': 5, 'HTTP (non-video)': 10, 'BitTorrent': 30, 'Video': 30
    #            },
    #        '22-24': {
    #            'VoIP': 10, 'HTTP (non-video)': 5, 'BitTorrent': 10, 'Video': 15
    #            },
    #        }

    traffic_per_timeslot = {} 
    for i in range(0, 23):
        crt_hours_range_dict = {}
        for s in tag_list:
            if start_date < end_date:
                #data range
                crt_service_accesses = ServiceUtilizationStatistics.objects.filter(
                                                        date__range=[start_date.strftime("%Y-%m-%d"), 
                                                                    end_date.strftime("%Y-%m-%d")],
                                                        client = client_id,
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
                                                        client = client_id,
                                                        service = s).aggregate(Sum('num_accesses', default=0))

            if crt_service_accesses.values()[0] != None: #no criteria match, no traffic stats stored 
                crt_hours_range_dict[s.service_name] = crt_service_accesses.values()[0]
            else:
                crt_hours_range_dict[s.service_name] = 0

        traffic_per_timeslot[str(i).zfill(2) + ":00" +"-" + str(i).zfill(2) + ":59"] = crt_hours_range_dict

    context = RequestContext(request, {
        'traffic_per_timeslot': OrderedDict(sorted(traffic_per_timeslot.items(), key=lambda t: t[0])),
        'tag_list': tag_list,
        'client_id': client_id,
        'start_date': start_date.strftime("%Y-%b-%d"),
        'end_date': end_date.strftime("%Y-%b-%d"),
        
        
    })

    return HttpResponse(template.render(context))
	#return render(request, 'profile/stats_by_date.html', {})

def compute_total_bandwidth(client_id):
    client = Client.objects.get(id = client_id)
    rules_list = Rule.objects.filter(client = client_id) 
    bandwidth_total = 0
    
    for rule in rules_list: 
        bandwidth_total = bandwidth_total + rule.bandwidth_percent
    return bandwidth_total

def manage(request, client_id):
    client = Client.objects.get(id = client_id)
    rules_list = Rule.objects.filter(client = client_id) 
    template = loader.get_template('profile/resources_mng.html')
    context = RequestContext(request, {
        'rules_list': rules_list,
        'total_bw_used' : 100 - compute_total_bandwidth(client_id),
        'client_id': client_id,
        })
    return HttpResponse(template.render(context))

#send client, not client id
def rule_edit(request, client_id):
    client = Client.objects.get(id = client_id)
    bandwidth_total = compute_total_bandwidth(client_id) 

    if request.method == "POST":
        form = RuleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.client = client
            if post.bandwidth_percent + bandwidth_total <= 100:
                post.save()
            return redirect('manage', client_id=client_id)
    else:
        form = RuleForm()
    return render(request, 'profile/rule_edit.html', {'client_id':client_id,'form':form})

def rule_update(request, pk, client_id):

    bandwidth_total = compute_total_bandwidth(client_id) 
    rule = get_object_or_404(Rule, pk=pk, client=client_id)
    crt_bandwidth = rule.bandwidth_percent

    if request.method == "POST":
        form = RuleForm(request.POST, instance=rule)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if post.bandwidth_percent + bandwidth_total - crt_bandwidth <= 100:
                post.save()
            return redirect('manage', client_id=client_id)
    else:
        form = RuleForm(instance=rule)
    return render(request, 'profile/rule_edit.html', {'client_id':client_id,'form':form})

def rule_delete(request, pk, client_id):
    client = Client.objects.get(id = client_id)
    rule = get_object_or_404(Rule, pk=pk, client=client_id)
    rule.delete()
    return redirect('manage', client_id=client_id)

def offers(request, client_id):
    client = Client.objects.get(id = client_id)
    offers_list = Offer.objects.all() 
    template = loader.get_template('profile/offers.html')
    context = RequestContext(request, {
        'offers_list': offers_list,
        'client_id': client_id,
        })
    return HttpResponse(template.render(context))

def transactions(request, client_id):
    client = Client.objects.get(id = client_id)
    template = loader.get_template('profile/transaction_hist.html')
    context = RequestContext(request, {
        'client_id': client_id,
    })
    return HttpResponse(template.render(context))

