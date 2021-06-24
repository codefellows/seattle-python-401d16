from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Thing


class ThingListView(ListView):
    template_name = "things/thing-list.html"
    model = Thing


class ThingDetailView(DetailView):
    template_name = "things/thing-detail.html"
    model = Thing


class ThingCreateView(CreateView):
    template_name = "things/thing-create.html"
    model = Thing
    fields = ["name", "reviewer", "rating"]


class ThingUpdateView(UpdateView):
    template_name = "things/thing-update.html"
    model = Thing
    fields = ["name", "reviewer", "rating"]


class ThingDeleteView(DeleteView):
    template_name = "things/thing-delete.html"
    model = Thing
    success_url = reverse_lazy("thing_list")
