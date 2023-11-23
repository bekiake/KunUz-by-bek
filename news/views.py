from django.shortcuts import render
from typing import Any
from django.views.generic import View, ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import News, Category, Tags
from django.urls import reverse_lazy
from .forms import AddNewForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

# Create your views here.

class HomePageView(View):
    def get(self, request):
        news = News.objects.filter(is_avtive=True).order_by('-create_at')[:4]
        
        context = {
            'news': news
        }
        return render(request, 'home.html', context)

class SearchView(ListView):
    template_name = 'search.html'
    model = News
    
    def get_queryset(self):
       
       query = self.request.GET.get('search')
       object_list = News.objects.filter(
           Q(title__icontains=query) | Q(desc__icontains=query) | Q(body__icontains=query)
           )
       return object_list
   
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
       context = super().get_context_data(**kwargs)
       context["query"] = self.request.GET.get('search')
       return context   

class AddNewView(LoginRequiredMixin, CreateView):
    model = News
    form_class = AddNewForm
    template_name = 'news/add_new.html'
    success_url = reverse_lazy("news:home")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
   
class MyNewsView(LoginRequiredMixin, ListView):
    template_name = "news/my_news.html"
    model = News
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        
        
        context["my_news"] = News.objects.filter(user=self.request.user)
        return context
    

class NewsDetailView(DeleteView):
    def get(self, request, pk):
        new = News.objects.get(id=pk)
        category = News.objects.filter(category=new.category)
        
        
        for x in new.tags.all():
            recom = News.objects.filter(tags = x)
            
       
        context = {
            "new": new,
            'recomendations_category': category,
            'recomendations_tag': recom,
            
        }
        return render(request, "news/new_detail.html", context)
    
    
    
class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    form_class = AddNewForm
    template_name = 'news/add_new.html'
    success_url = reverse_lazy("news:home")
    
    def test_func(self):
        new = self.get_object()
        if self.request.user == new.user or self.request.user.is_superuser:
            return True
        return False    





class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'news/delete.html'
    success_url = reverse_lazy("news:home")
    
    def test_func(self):
        new = self.get_object()
        if self.request.user == new.user or self.request.user.is_superuser:
            return True
        return False    

    
class CategoryView(View):
    
    def get(self, request, pk):
        category = Category.objects.get(id=pk)
        context = {
            'news' : category.news_category.all()
        }
        return render(request, 'home.html', context)


class TagsView(View):
    
    def get(self, request, pk):
        tags = Tags.objects.get(id=pk)
        context = {
            'news' : tags.news_tag.all()
        }
        return render(request, 'home.html', context)
        
    
    
    
    
    
    