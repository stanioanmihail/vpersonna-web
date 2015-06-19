from django.contrib import admin
from .models import *

class ServiceUtilizationStatisticsModel(admin.ModelAdmin):
    list_display = ("get_client_name", "get_client_mail", "service", "date", "num_accesses")
    def get_client_name(self, obj):
        return obj.client.name
    get_client_name.short_description = 'Client Name'
    def get_client_mail(self, obj):
        return obj.client.email
    get_client_mail.short_description = 'Client Email'
    def get_client_contract_id(self, obj):
        return obj.client.contract_id
    get_client_contract_id.short_description = 'Client Contract ID'

class RawPacketModel(admin.ModelAdmin):
    list_display = ("id", "ip_src", "port_src", "ip_dst", "port_dst", 
                'host_address' , 'get_transport_protocol', 'traffic_type', 'timestamp_start', 'timestamp_end' )

class IPAllocationModel(admin.ModelAdmin):
    list_display = ("get_client_name", "get_client_mail", "get_client_contract_id","ip_addr")
    def get_client_name(self, obj):
        return obj.client.name
    get_client_name.short_description = 'Client Name'
    def get_client_mail(self, obj):
        return obj.client.email
    get_client_mail.short_description = 'Client Email'
    def get_client_contract_id(self, obj):
        return obj.client.contract_id
    get_client_contract_id.short_description = 'Client Contract ID'

class ClientModel(admin.ModelAdmin):
    list_display = ("name", "email", "contract_id", "username")

class RuleModel(admin.ModelAdmin):
    list_display = ("get_client_name", "type_of_service", "bandwidth_percent", "destination_address")
    def get_client_name(self, obj):
        return obj.client.name
    get_client_name.short_description = 'Client Name'

class OfferModel(admin.ModelAdmin): 
    list_display = ("offer_name", "offer_short_description", "cost_per_min")

class SiteAccessModel(admin.ModelAdmin):
    list_display = ("url", "num_accesses")

class NewsModel(admin.ModelAdmin):
    list_display = ("title", "date", "active")
# Register your models here.
admin.site.register(Client, ClientModel)
admin.site.register(ServiceType)
admin.site.register(Rule, RuleModel)
admin.site.register(Offer, OfferModel)
admin.site.register(SiteAccess, SiteAccessModel)
admin.site.register(ServiceUtilizationStatistics, ServiceUtilizationStatisticsModel)
admin.site.register(Activity)
admin.site.register(RawPacket, RawPacketModel)
admin.site.register(IPAllocation, IPAllocationModel)
admin.site.register(News, NewsModel)

