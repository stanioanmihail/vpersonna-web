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
    context = RequestContext(request, {
        'dashboard_dict':dashboard_dict,
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
