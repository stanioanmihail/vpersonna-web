from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils.timezone import utc
from collections import OrderedDict
from .forms import RuleForm
import datetime
from django.shortcuts import redirect, get_object_or_404
from vprofile.models import Rule, Offer, Client


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
    client = Client.objects.get(id = client_id)
    template = loader.get_template('profile/dashboard.html')
    dashboard_dict = {
        'HTTP (non-video)' : 200,
        'VoIP' : 5,
        'BitTorrent' : 400,
        'Video' : 105,
        'FTP' : 3,
    
    }
    top_rate_sites_matrix = [
        ["www.facebook.com","66.220.152.19", 480],
        ["www.google.com", "173.194.112.178", 304],
        ["www.9gag.com", "54.215.82.230", 211],
        ["www.youtube.com", "217.73.160.236", 120],
        ["www.engadget.com", "195.93.85.193", 80],
    ]
    
    context = RequestContext(request, {
        'dashboard_dict':dashboard_dict,
        'top_rate_sites_matrix':top_rate_sites_matrix,
        'client_id': client_id,
        'client': client,
    })
    return HttpResponse(template.render(context))
    #	return render(request, 'profile/dashboard.html', {})

def stats(request, client_id):
    template = loader.get_template('profile/advanced_statistics.html')
    client = Client.objects.get(id = client_id)
    context = RequestContext(request, {
        'client_id': client_id,
    })
    return HttpResponse(template.render(context))

def stats_date(request, client_id):
    client = Client.objects.get(id = client_id)
    template = loader.get_template('profile/stats_by_date.html')
    start_date = request.POST['datepicker-start']
    end_date = request.POST['datepicker-end'] 
    tag_list = [ 'VoIP', 'HTTP (non-video)', 'BitTorent', 'Video' ]
    traffic_per_timeslot = {
            '08-10': {
                'VoIP': 10, 'HTTP (non-video)': 20, 'BitTorrent': 30, 'Video': 15
                },
            '10-12': {
                'VoIP': 10, 'HTTP (non-video)': 20, 'BitTorrent': 30, 'Video': 15
                },
            '12-14': {
                'VoIP': 5, 'HTTP (non-video)': 2, 'BitTorrent': 20, 'Video': 5
                },
            '14-16': {
                'VoIP': 1, 'HTTP (non-video)': 0, 'BitTorrent': 0, 'Video': 1
                },
            '16-18': {
                'VoIP': 3, 'HTTP (non-video)': 4, 'BitTorrent': 4, 'Video': 3
                },
            '18-20': {
                'VoIP': 5, 'HTTP (non-video)': 2, 'BitTorrent': 17, 'Video': 20
                },
            '20-22': {
                'VoIP': 5, 'HTTP (non-video)': 10, 'BitTorrent': 30, 'Video': 30
                },
            '22-24': {
                'VoIP': 10, 'HTTP (non-video)': 5, 'BitTorrent': 10, 'Video': 15
                },
            }
     #traffic_per_timeslot = {
     #       '08-10': {
     #           'VoIP': "0.10%", 'HTTP (non-video)': "0.20%", 'BitTorrent': "0.30%", 'Video': "0.15%"
     #           },
     #       '10-12': {
     #           'VoIP': "0.10%", 'HTTP (non-video)': "0.20%", 'BitTorrent': "0.30%", 'Video': "0.15%"
     #           },
     #       '12-14': {
     #           'VoIP': "0.05%", 'HTTP (non-video)': "0.02%", 'BitTorrent': "0.20%", 'Video': "0.05%"
     #           },
     #       '14-16': {
     #           'VoIP': "0.05%", 'HTTP (non-video)': "0.00%", 'BitTorrent': "0.00%", 'Video': "0.01%"
     #           },
     #       '16-18': {
     #           'VoIP': "0.03%", 'HTTP (non-video)': "0.04%", 'BitTorrent': "0.04%", 'Video': "0.03%"
     #           },
     #      '18-20': {
     #          'VoIP': "0.05%", 'HTTP (non-video)': "0.02%", 'BitTorrent': "0.17%", 'Video': "0.20%"
     #           },
     #       '20-22': {
     #           'VoIP': "0.05%", 'HTTP (non-video)': "0.10%", 'BitTorrent': "0.30%", 'Video': "0.30%"
     #           },
     #       '22-24': {
     #          'VoIP': "0.10%", 'HTTP (non-video)': "0.05%", 'BitTorrent': "0.10%", 'Video': "0.15%"
     #          },
     #      }
    context = RequestContext(request, {
        'date': "Start Date: " + start_date + "|" + "End Date:" + end_date,
        'traffic_per_timeslot': OrderedDict(sorted(traffic_per_timeslot.items(), key=lambda t: t[0])),
        'tag_list': tag_list,
        'client_id': client_id,
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

def rule_edit(request, client_id):
    bandwidth_total = compute_total_bandwidth(client_id) 

    if request.method == "POST":
        form = RuleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.client = client_id
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

