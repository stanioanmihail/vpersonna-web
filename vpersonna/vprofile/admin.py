from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(ServiceType)
admin.site.register(Rule)
admin.site.register(Offer)
admin.site.register(SiteAccess)
admin.site.register(ServiceUtilizationStatistics)
admin.site.register(Activity)

