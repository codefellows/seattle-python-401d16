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
    model = Thing
    template_name = "thing_list.html"


class ThingDetailView(DetailView):
    model = Thing
    template_name = "thing_detail.html"


class ThingCreateView(CreateView):
    model = Thing
    template_name = "thing_create.html"
    fields = ["name", "rating", "reviewer"]


class ThingUpdateView(UpdateView):
    model = Thing
    template_name = "thing_update.html"
    fields = ["name", "rating", "reviewer"]


class ThingDeleteView(DeleteView):
    model = Thing
    template_name = "thing_delete.html"
    success_url = reverse_lazy("thing_list")
