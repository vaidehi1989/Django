from django.urls import path

from . import views

urlpatterns = [
    path('', views.postListView, name='listposts'),
    path('post/<int:pk>/', views.postDetailView, name='detailview'),
    path('post/<int:pk>/delete', views.postDeleteView, name='deletepost'),
    path('post/<int:pk>/edit', views.postEditView, name='editpost'),
    path('post/new', views.postAddView, name='newpost'),
]
