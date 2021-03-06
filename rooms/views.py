from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from . import models


# Create your views here.


class HomeView(ListView):

    model = models.Room
    paginate_orphans = 5
    paginate_by = 10
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()
