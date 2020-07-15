from django.contrib import admin
from adminsortable.admin import SortableAdmin
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone
from django.db.models import Count, Q 
from _datetime import timedelta
from .models import InMate, History
import json

@admin.register(InMate)
class InMateAdmin(SortableAdmin):
    #Column displayed
    list_display = ["history_link","inmate_name","inmate_surname","date_of_birth","cell_num","intake_time","edit_link"]
    #Quick Filter
    list_filter = ["inmate_name"]
    #Quick Search
    search_fields = ['inmate_name',"inmate_surname"]
    
    def changelist_view(self, request, extra_context=None):
                  
        # Aggregate new subscribers per day
        chart_data = (
             History.objects.annotate()
            .values("location")
            .annotate(count=Count("id",
                                  filter=Q(time__gte=timezone.now() - timedelta(minutes=30))))
        )           
    
        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

@admin.register(History)
class HistoryAdmin(SortableAdmin):
    list_display = ["get_inmate","location","time"]
    list_filter = ["location","inmate_id"]
    
    def get_inmate(self, obj):
        return str(obj.inmate)
    
    get_inmate.short_description = 'In Mate'
    