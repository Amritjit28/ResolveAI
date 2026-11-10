
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

from .models import Ticket


@staff_member_required(login_url='/admin/login/')
def dashboard(request):

    tickets = Ticket.objects.order_by('-created_at')[:25]

    total_tickets = Ticket.objects.count()

    open_tickets = Ticket.objects.filter(
        status='open'
    ).count()

    in_progress_tickets = Ticket.objects.filter(
        status='in_progress'
    ).count()

    resolved_tickets = Ticket.objects.filter(
        status='resolved'
    ).count()

    context = {
        'tickets': tickets,
        'total_tickets': total_tickets,
        'open_tickets': open_tickets,
        'in_progress_tickets': in_progress_tickets,
        'resolved_tickets': resolved_tickets,
    }

    return render(request, 'tickets/dashboard.html', context)
