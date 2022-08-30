from unicodedata import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.db.models import *
from django.contrib.auth.models import Group
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # add this
# Create your views here.


@login_required
def profile(request):
    return render(request, 'profile.html')


def registeratsiya(request):
    return render(request, 'registeratsiya.html')


class HisobotListView(ListView):
    template_name = 'index.html'
    context_object_name = 'Hisobot'

    def get_queryset(self):
        url_data = self.request.GET
        q = Hisobot.objects.all()

        if 'project' in url_data and url_data['project']:
            q = q.filter(project__icontains=url_data['project'])

        return q


class HisobotCreateView(CreateView):
    queryset = Hisobot.objects.all()
    template_name = 'add.html'
    fields = "__all__"
    success_url = '/'


class CategoryListView(ListView):
    template_name = 'index.html'
    context_object_name = 'Category'

    def get_queryset(self):
        url_data = self.request.GET
        q = Category.objects.all()

        if 'title' in url_data and url_data['title']:
            q = q.filter(title__icontains=url_data['title'])

        return q


class CategoryCreateView(CreateView):
    queryset = Category.objects.all()
    template_name = 'add.html'
    fields = "__all__"
    success_url = '/'


class CategoryUpdateView(UpdateView):
    queryset = Category.objects.all()
    template_name = 'Category-add.html'
    fields = "__all__"
    context_object_name = 'Category'
    success_url = '/'


class CategoryDeleteView(DeleteView):
    queryset = Category.objects.all()
    template_name = 'Category-delete.html'
    fields = "__all__"

    success_url = '/'


class HisobotDetailView(DetailView):
    template_name = 'report_detail.html'
    model = Hisobot

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        daromat = Daromad.objects.filter(hisobot=self.kwargs['pk'])
        xarajatlar = Xarajatlar.objects.filter(hisobot=self.kwargs['pk'])
        context = {'daromad': daromat, 'xarajatlar': xarajatlar}
        return context


class DarmadCreateView(CreateView):
    queryset = Daromad.objects.all()
    template_name = 'revenue_add.html'
    fields = "__all__"
    success_url = '/'


class XarajatlarCreateView(CreateView):
    queryset = Xarajatlar.objects.all()
    template_name = 'expense_add.html'
    fields = "__all__"
    success_url = '/'


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("Hisobot-main")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("Hisobot-main")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


@login_required
def profile(request):
    return render(request, 'profile.html')


class DrektorListView(ListView):
    template_name = 'vc_index.html'
    context_object_name = 'Category'
    queryset = Category.objects.all()


class DrektorCreateView(CreateView):
    queryset = Drektor.objects.all()
    template_name = 'drektor-add.html'
    fields = "__all__"
    success_url = '/'
