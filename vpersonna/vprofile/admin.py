from django.contrib import admin
from .models import *

class ServiceUtilizationStatisticsModel(admin.ModelAdmin):
    list_display = ("client", "service", "date", "num_accesses")

class BrutePacketModel(admin.ModelAdmin):
    list_display = ("id", "ip_src", "port_src", "ip_dst", "port_dst", 'host_address' , 'get_transport_protocol', 'traffic_type', 'timestamp' )
class IPAllocationModel(admin.ModelAdmin):
    list_display = ("client", "ip_addr")
# Register your models here.
admin.site.register(Client)
admin.site.register(ServiceType)
admin.site.register(Rule)
admin.site.register(Offer)
admin.site.register(SiteAccess)
admin.site.register(ServiceUtilizationStatistics, ServiceUtilizationStatisticsModel)
admin.site.register(Activity)
admin.site.register(BrutePacket, BrutePacketModel)
admin.site.register(IPAllocation, IPAllocationModel)

