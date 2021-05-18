from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.utils.html import format_html

from django.views import generic
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm


# Create your views here.

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadListView(generic.ListView):
    template_name = 'leads/lead_list.html'
    queryset= Lead.objects.all()
    context_object_name = 'leads'


class LeadDetailView(generic.DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


class LeadCreateView(generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class= LeadModelForm  

    def get_success_url(self):
        return reverse('leads:lead-list')

class LeadUpdateView(generic.UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')


class LeadDeleteView(generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')


def landing_page(request):
    return render(request, 'landing.html')


def lead_list(request):
    leads = Lead.objects.all()
    context ={
        'leads': leads
    }

    return render(request, 'leads/lead_list.html', context)


def lead_detail(request, pk):
    lead= Lead.objects.get(id= pk)
    context ={
        'lead': lead
    }
    return render(request, "leads/lead_detail.html", context)



def lead_create(request):
    form = LeadModelForm()
    # form = LeadForm()
    if request.method == "POST":
        print('Receiving a post request')
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            print('lead has been created')
            return redirect('/leads')

    context={
        'form': LeadModelForm()
    }

    return render(request, "leads/lead_create.html", context)




def lead_update(request, pk):
    lead = Lead.objects.get(id= pk)
    form = LeadModelForm(instance = lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance = lead)
        if form.is_valid():
            form.save()
            return redirect('/leads')
    
    context ={
        'form': form,
        'lead': lead
    }

    return render(request, 'leads/lead_update.html', context)


def lead_delete(request, pk):
    lead = Lead.objects.get(id= pk)
    lead.delete()
    return redirect('/leads')

    



# def lead_create(request):
#     form = LeadModelForm()
#     # form = LeadForm()
#     if request.method == "POST":
#         print('Receiving a post request')
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             print('the form is valid')
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 age = age,
#                 agent = agent
#             )
#             print('lead has been created')
#             return redirect('/leads')

#     context={
#         'form': LeadForm()
#     }

#     return render(request, "leads/lead_create.html", context)


# def lead_update(request, pk):
#     lead = Lead.objects.get(id = pk)
#     form = LeadForm()
#     # form = LeadForm()
#     if request.method == "POST":
#         print('Receiving a post request')
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             print('the form is valid')
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             print('lead has been created')
#             return redirect('/leads')

#     context={
#         'form': form,
#         'lead': lead
#     }
#     return render(request, "leads/lead_update.html", context)

