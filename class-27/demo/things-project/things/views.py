from django.views.generic import TemplateView, ListView, DetailView
from .models import Thing


class HomeView(TemplateView):
    template_name = "home.html"


class AboutView(TemplateView):
    template_name = "about.html"


class ThingListView(ListView):
    template_name = "thing_list.html"
    model = Thing


class ThingDetailView(DetailView):
    template_name = "thing_detail.html"
    model = Thing
