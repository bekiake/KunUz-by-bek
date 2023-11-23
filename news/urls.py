from django.urls import path
from .views import HomePageView, SearchView, AddNewView, MyNewsView, NewsDetailView,\
    NewsUpdateView, NewsDeleteView, CategoryView, TagsView

app_name = 'news'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('add_new/', AddNewView.as_view(), name='add_new'),
    path('my_news/', MyNewsView.as_view(), name='my_news'),
    path('news_detail/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('news_update/<int:pk>', NewsUpdateView.as_view(), name='news_update'),
    path('news_delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete'),
    path('category/<int:pk>', CategoryView.as_view(), name='category'),
    path('tags/<int:pk>', TagsView.as_view(), name='tags'),
]
