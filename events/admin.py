from django.contrib import admin

from .models import Event, Location, EventKind, Artist, Tickets, ShoppingCart


class TicketsInline(admin.TabularInline):
    model = Tickets


class EventAdmin(admin.ModelAdmin):
    inlines = [TicketsInline,]
    list_display = ('pk', 'name', 'kind', 'location', 'start_date')
    list_filter = ('start_date',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'address')
    search_fields = ('name', 'address')


class EventKindAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('pk', 'initials')


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')


admin.site.register(Event, EventAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(EventKind, EventKindAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
