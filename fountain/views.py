from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,ListView
from django.contrib.auth.decorators import login_required
from .models import ChurchActivityModel,SecondChurchActivityModel

# Create your views here.
def base (request):
    return render(request,"base.html")
class HomeView(ListView):
    model = ChurchActivityModel
    template_name = 'fountain/home.html'


class ArticleDetailView(DetailView):
    model = ChurchActivityModel
    template_name = 'fountain/article_detail.html'

    def ArticleDetailView(request, pk):  
        object = get_object_or_404(ChurchActivityModel, pk=pk)
        return render(request, 'article_detail.html', {'detail': object})


# The about page
def about (request):
    return render (request,'fountain/about.html' )