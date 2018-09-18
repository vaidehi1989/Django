from django.urls import path
from . import views

urlpatterns = [
    # path('', views.listposts, name = "listposts"),
    path('', views.ListPosts.as_view(), name='listposts'),

    path('post/<int:pk>/', views.detailPost, name='detailview'),
    # path('post/<int:pk>/', views.DetailPost,as_view(), name='detailview'),

    path('post/<int:pk>/delete', views.deletePost, name='deletepost'),

    path('post/<int:pk>/edit', views.postEditView, name='editpost'),

    path('post/new', views.postAddView, name='newpost'),

]
