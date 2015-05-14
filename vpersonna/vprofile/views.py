from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils.timezone import utc
from collections import OrderedDict
import datetime

# Create your views here.
def dashboard(request):
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
    })
    return HttpResponse(template.render(context))
    #	return render(request, 'profile/dashboard.html', {})


def stats(request):
         
	return render(request, 'profile/advanced_statistics.html', {})
def stats_date(request):
    template = loader.get_template('profile/stats_by_date.html')
    date = request.POST['datepicker'] 
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
    context = RequestContext(request, {
        'date': date,
        'traffic_per_timeslot': OrderedDict(sorted(traffic_per_timeslot.items(), key=lambda t: t[0])),
        'tag_list': tag_list,
    })

    return HttpResponse(template.render(context))
	#return render(request, 'profile/stats_by_date.html', {})
def manage(request):
	return render(request, 'profile/resources_mng.html', {})
def offers(request):
	return render(request, 'profile/offers.html', {})
def transactions(request):
	return render(request, 'profile/transaction_hist.html', {})

