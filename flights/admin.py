from django.contrib import admin
from .models import Airport, Flight, Passenger

class AirportAdmin(admin.ModelAdmin):
  date_hierarchy = 'created_at'
  search_fields = ['code', 'city']
  list_display = ['code', 'city', 'created_at', 'updated_at']
  class Meta:
    model = Airport

class FlightAdmin(admin.ModelAdmin):
  date_hierarchy = 'created_at'
  search_fields = ['origin', 'destination']
  list_display = ['origin', 'destination', 'created_at', 'updated_at']
  class Meta:
    model = Flight

admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger)
