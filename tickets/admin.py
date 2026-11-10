from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'subject',
        'customer_name',
        'status',
        'priority',
        'created_at',
    )

    list_filter = ('status', 'priority', 'created_at')

    search_fields = (
        'subject',
        'customer_name',
        'customer_email',
    )

    readonly_fields = ('created_at', 'updated_at')
