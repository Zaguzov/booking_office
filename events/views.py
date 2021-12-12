from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.paginator import Paginator

from events.models import Event, Location, EventKind, Artist, Tickets, \
    ShoppingCart
from events.forms import BuyingForm
from booking_office.settings import PAGINATOR_PER_PAGE


User = get_user_model()


def index(request):
    events = Event.objects.select_related('kind')
    paginator = Paginator(events, PAGINATOR_PER_PAGE)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {'page': page, 'paginator': paginator}
    )


def kind_events(request, name):
    kind = get_object_or_404(EventKind, name=name)
    events = kind.events.all()
    paginator = Paginator(events, PAGINATOR_PER_PAGE)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'kind.html',
        {'kind': kind, 'page': page, 'paginator': paginator}
    )


def event_view(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    tickets = get_object_or_404(Tickets, event=event_id)
    form = BuyingForm()
    artists = event.artists.all()
    return render(
        request,
        'event.html',
        {'event': event, 'form': form, 'tickets': tickets, 'artists': artists}
    )


def location_view(request, name):
    location = get_object_or_404(Location, name=name)
    events = location.events.all()
    paginator = Paginator(events, PAGINATOR_PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return  render(
        request,
        'location.html',
        {'location': location, 'page': page, 'paginator': paginator}
    )


def artist_view(request, initials):
    artist = get_object_or_404(Artist, initials=initials)
    events = Event.objects.filter(artists__initials__contains=artist.initials)
    paginator = Paginator(events, PAGINATOR_PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'artist.html', {'artist': artist,
                                           'page': page,
                                           'paginator': paginator})

@login_required
def shopping_cart_view(request):
    shopping_cart = ShoppingCart.objects.filter(user=request.user)
    paginator = Paginator(shopping_cart, PAGINATOR_PER_PAGE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'shopping_cart.html',
                  {'page': page, 'paginator': paginator})


def page_not_found(request, exception):
    return render(
        request,
        'misc/404.html',
        {'path': request.path},
        status=404
    )


def server_error(request):
    return render(request, 'misc/500.html', status=500)


@login_required
def add_to_shopping_cart(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    ticket = get_object_or_404(Tickets, event=event)
    form = BuyingForm(request.POST, ticket=ticket)
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.user = request.user
        new_form.ticket = ticket
        ticket.number_of_available_tickets +=\
            -form.cleaned_data['number_of_purchased_tickets']
        ticket.save()
        new_form.save()
        return redirect('event', event_id)
    messages.error(request, 'Кол-во покупаемых билетов не может '
                   'быть больше кол-ва доступных')
    return render(request,'event.html', {'event': event, 'form': form, 'tickets': ticket})



def kinds_view(request):
    kinds = EventKind.objects.all()
    paginator = Paginator(kinds, PAGINATOR_PER_PAGE)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'event_kinds.html',
                  {'kinds': kinds, 'page': page, 'paginator': paginator})


@login_required
def delete_from_shopping_cart(request, shopping_cart_id):
    ticket_delete = get_object_or_404(ShoppingCart, pk=shopping_cart_id)
    ticket = ticket_delete.ticket
    ticket.number_of_available_tickets += \
        ticket_delete.number_of_purchased_tickets
    ticket.save()
    ticket_delete.delete()
    return redirect('shopping_cart')
