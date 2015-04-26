from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

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
def manage(request):
	return render(request, 'profile/resources_mng.html', {})
def offers(request):
	return render(request, 'profile/offers.html', {})
def transactions(request):
	return render(request, 'profile/transaction_hist.html', {})
