from django.urls import path,re_path
from . import views
app_name='blog'
urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    #re_path(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/',views.ArchivesView.as_view(),name='archives'),
    path('category/<int:pk>/',views.CategoryView.as_view(),name='category'),
    path('tag/<int:pk>/',views.TagView.as_view(),name='tag'),
    path('about/',views.about,name='about'),
    #path('search/$',views.search,name='search')

]