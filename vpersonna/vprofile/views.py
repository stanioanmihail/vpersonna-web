from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages

#database imports
from vprofile.models import *
from django.db.models import Sum
from .forms import *
from collections import OrderedDict
from django.contrib.auth.models import User

#time imports
from django.utils.timezone import utc
import datetime
from dateutil.relativedelta import relativedelta

#authentication imports
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

######################### TIME FUNCTIONS ########################
def first_day_of_month(d):
    return datetime.date(d.year, d.month, 1)

def get_today():
    #[CHANGE] change the value here - hardcoded 3-06-2015 22:30
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
####################################################################

######################### AUTHENTICATION ###########################
# login_decorator which requires authentication for each view that it uses it
def user_login_required(f):
    def wrap(request, *args, **kwargs):
        if 'userid' not in request.session.keys():
            return redirect('login')
        return f(request, *args, **kwargs)
    wrap.__doc__ = f.__doc__
    wrap.__name__= f.__name__
    return wrap
            
# login interface        
def auth_method_login(request):
    template = loader.get_template('profile/auth.html')
    username = '';
    password = '';
    state = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                request.session['userid'] = user.id #used for login require decorator
                if user.is_superuser:
                    return redirect('client_mng')
                else:
                    client = Client.objects.get(user=user)
                    return redirect('dashboard')
                
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    context = RequestContext(request, {
     'state': state, 
     'username': username,
    })
    return HttpResponse(template.render(context))

#logout view
def auth_method_logout(request):
    logout(request)
    return redirect('login')

def change_password(request):
    
    template = loader.get_template('profile/change_password_form.html')
    state = ''
    if request.method == "POST":
        form = ChangePassword(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            new_conf_password = form.cleaned_data['new_confirm_password']
            client = Client.objects.get(user=request.user)
            if old_password == client.password:
                if new_password == new_conf_password:
                    client.user.set_password(new_password)
                    client.password = new_password
                    client.user.save()
                    client.save()
                    return redirect('login')
                else:
                    state='New password and confirmation password differ'
                    messages.add_message(request, messages.INFO, state)
                    return redirect('change_passwd')
                    #return HttpResponseRedirect(reverse('change_passwd', kwargs={'state': state}))



            else:
                state="The old password doesn' match"
                messages.add_message(request, messages.INFO, state)
                return redirect('change_passwd')
                #return HttpResponseRedirect(reverse('change_passwd', kwargs={'state': state}))
    else:
        form = ChangePassword()

    context = RequestContext(request, {
     'state': state, 
     'form': form,
    })
    return HttpResponse(template.render(context))


##################################################################################

############################## ADMIN INTERFACE (superuser) #######################    

#Superuser interface: client management
@user_login_required 
@user_passes_test(lambda u: u.is_superuser)
def client_management(request):
    clients = Client.objects.all()
    template = loader.get_template('profile/admin/clients.html')
    context = RequestContext(request, {
        'clients': clients,
        })
    return HttpResponse(template.render(context))

@user_login_required 
@user_passes_test(lambda u: u.is_superuser)
def new_client_admin_method(request):

    if request.method == "POST":
        form = NewClientForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.user =  User.objects.create_user(username=post.username, email=post.username, password=post.password)  
            post.save()
            return redirect('client_mng')
    else:
        form = NewClientForm()
    return render(request, 'profile/admin/new_client_form.html', {'form':form})

@user_login_required 
@user_passes_test(lambda u: u.is_superuser)
def update_client_admin_method(request, pk):

    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = UpdateClientForm(request.POST, instance=client)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            new_password = form.cleaned_data['password_field']
            if new_password != "":
                client.user.set_password(new_password)
                client.user.save()
                client.password = new_password
                client.save()
            post.save()
            return redirect('client_mng')
    else:
        form = UpdateClientForm(instance=client)
    return render(request, 'profile/admin/new_client_form.html', {'form':form})

@user_login_required 
@user_passes_test(lambda u: u.is_superuser)
def delete_client_admin_method(request, pk):

    client = get_object_or_404(Client, pk=pk)
    client.user.delete()
    client.delete()
    return redirect('client_mng')

#Superuser interface: news management
@user_login_required 
@user_passes_test(lambda u: u.is_superuser)
def news_management(request):
    news = News.objects.order_by('-date')
    template = loader.get_template('profile/admin/news.html')
    context = RequestContext(request, {
        'news': news,
        })
    return HttpResponse(template.render(context))



@user_login_required 
@user_passes_test(lambda u: u.is_superuser)
def new_post_admin_method(request):

    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('news_mng')
    else:
        form = NewsForm()
    return render(request, 'profile/admin/new_post_form.html', {'form':form})

@user_login_required 
@user_passes_test(lambda u: u.is_superuser)
def update_post_admin_method(request, pk):

    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('news_mng')
    else:
        form = NewsForm(instance=news)
    return render(request, 'profile/admin/new_post_form.html', {'form':form})

@user_login_required 
@user_passes_test(lambda u: u.is_superuser)
def delete_post_admin_method(request, pk):

    news = get_object_or_404(News, pk=pk)
    news.delete()
    return redirect('news_mng')


#Superuser interface: ip allocation
@user_login_required 
@user_passes_test(lambda u: u.is_superuser)
def ipalloc_management(request):
    ipalloc_list = IPAllocation.objects.all()
    template = loader.get_template('profile/admin/ipalloc.html')
    context = RequestContext(request, {
        'ip_alloc_list': ipalloc_list,
        })
    return HttpResponse(template.render(context))


@user_login_required 
@user_passes_test(lambda u: u.is_superuser)
def new_ipalloc_admin_method(request):

    if request.method == "POST":
        form = NewAllocationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('ip_alloc_mng')
    else:
        form = NewAllocationForm()
    return render(request, 'profile/admin/new_allocation_form.html', {'form':form})

@user_login_required 
@user_passes_test(lambda u: u.is_superuser)
def update_ipalloc_admin_method(request, pk):

    alloc = get_object_or_404(IPAllocation, pk=pk)
    if request.method == "POST":
        form = NewAllocationForm(request.POST, instance=alloc)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('ip_alloc_mng')
    else:
        form = NewAllocationForm(instance=alloc)
    return render(request, 'profile/admin/new_allocation_form.html', {'form':form})

@user_login_required 
@user_passes_test(lambda u: u.is_superuser)
def delete_ipalloc_admin_method(request, pk):

    news = get_object_or_404(IPAllocation, pk=pk)
    news.delete()
    return redirect('ip_alloc_mng')

##################################################################

########################## CLIENT INTERFACE ######################
def home(request):
    return redirect('login')

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

# the total amount of resources is idetified by 100% (percent)
# the allocation of n% bandwidth for a type of service means
# that remains 100% - n% bandwidth available
def compute_total_bandwidth(request):
    client = Client.objects.get(user = request.user)
    rules_list = Rule.objects.filter(client = client.id) 
    bandwidth_total = 0
    
    for rule in rules_list: 
        bandwidth_total = bandwidth_total + rule.bandwidth_percent
    return bandwidth_total

@user_login_required 
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
@user_login_required 
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

@user_login_required 
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

@user_login_required 
def rule_delete(request, pk):
    client = Client.objects.get(user = request.user)
    rule = get_object_or_404(Rule, pk=pk)
    rule.delete()
    return redirect('manage')

@user_login_required 
def offers(request):
    client = Client.objects.get(user = request.user)
    offers_list = Offer.objects.all() 
    template = loader.get_template('profile/offers.html')
    context = RequestContext(request, {
        'offers_list': offers_list,
        })
    return HttpResponse(template.render(context))

@user_login_required 
def transactions(request):
    client = Client.objects.get(user = request.user)
    template = loader.get_template('profile/transaction_hist.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))

