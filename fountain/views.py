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

    #This model is for the sub category of the blog
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['second_constructions'] = SecondChurchActivityModel.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = ChurchActivityModel
    template_name = 'fountain/article_detail.html'

    def ArticleDetailView(request, pk):  
        object = get_object_or_404(ChurchActivityModel, pk=pk)
        return render(request, 'article_detail.html', {'detail': object})


class SecondChurchActivityDetailViewArticleDetailView(DetailView):
    model = SecondChurchActivityModel
    template_name = 'josep/second_article_detail.html'
    context_object_name = 'second_construction'

    def SecondChurchActivityDetailViewArticleDetailView(request, pk):  
        object = get_object_or_404(SecondChurchActivityModel, pk=pk)
        return render(request, 'josep/second_article_detail.html', {'second_detail': object})

# The about page
def about (request):
    return render (request,'fountain/about.html' )