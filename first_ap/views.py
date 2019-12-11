
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from first_ap.models import First_A
from first_ap.forms import First_AForm
	
class IndexTemplateView(TemplateView):
	template_name='first_ap/index.html'
	
class First_ADeleteView(DeleteView):
	model = First_A
	success_url = reverse_lazy('first_ap:first_a_list')

class First_AListView(ListView):
	model = First_A
	
class First_ADetailView(DetailView):
	model = First_A
	
class First_ACreateView(CreateView):
	model = First_A
	form_class = First_AForm
	
class First_AUpdateView(UpdateView):
	model = First_A
	form_class = First_AForm

class First_AMyPageView(TemplateView):
	template_name = 'first_ap/first_a_my_page.html'