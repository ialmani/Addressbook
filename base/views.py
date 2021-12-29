from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Contact
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomRegisterView(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirected_authenticated_users = True
    success_url = reverse_lazy('contacts')

    #redirect the user (created, logged in, and redirected )
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CustomRegisterView, self).form_valid(form)

    #authenticated users can not see the register page and will be redirected to contacts list page
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('contacts')
        return super(CustomRegisterView, self).get(*args, **kwargs)


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('contacts')


class ContactList(LoginRequiredMixin, ListView):
    model = Contact
    context_object_name = 'contacts'

    #user only gets their own data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = context['contacts'].filter(user=self.request.user)
        # context['count'] = context['contacts'].filter(complete=False).count()

        #get search value
        search_input = self.request.GET.get('search') or ''

        if search_input:
            context['contacts'] = context['contacts'].filter(firstname__icontains=search_input ) |\
                                  context['contacts'].filter(lastname__icontains=search_input) |\
                                  context['contacts'].filter(mobile_number__icontains=search_input) |\
                                  context['contacts'].filter(work_number__icontains=search_input) |\
                                  context['contacts'].filter(home_number__icontains=search_input) | context['contacts'].filter(email__icontains=search_input) |\
                                  context['contacts'].filter(address__icontains=search_input)

        #use this in the template
        context['search_input'] = search_input
        return context


class ContactDetail(LoginRequiredMixin, DetailView):
    model = Contact
    context_object_name = 'contact'
    template_name = 'base/contact.html'


class ContactCreate(LoginRequiredMixin, CreateView):
    # post req and create an item
    model = Contact
    fields = ['firstname', 'lastname', 'mobile_number', 'work_number','home_number', 'email', 'address']
    success_url = reverse_lazy('contacts')

    #when user adds a contact, it's added to their profile not everyone elses
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ContactCreate, self).form_valid(form)

class ContactUpdate(LoginRequiredMixin, UpdateView):
    model = Contact
    fields = ['firstname', 'lastname', 'mobile_number', 'work_number','home_number', 'email', 'address']
    success_url = reverse_lazy('contacts')


class ContactDelete(LoginRequiredMixin, DeleteView):
    model = Contact
    context_object_name = 'contact'
    success_url = reverse_lazy('contacts')

