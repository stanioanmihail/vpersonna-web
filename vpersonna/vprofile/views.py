from django.shortcuts import render

# Create your views here.
def dashboard(request):
	return render(request, 'profile/dashboard.html', {})
def stats(request):
	return render(request, 'profile/advanced_statistics.html', {})
def manage(request):
	return render(request, 'profile/resources_mng.html', {})
def offers(request):
	return render(request, 'profile/offers.html', {})
def transactions(request):
	return render(request, 'profile/transaction_hist.html', {})
