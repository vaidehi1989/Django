from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='listposts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detailview'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='deletepost'),
    path('post/<int:pk>/edit', views.PostEditView.as_view(), name='editpost'),
    path('post/new', views.PostAddView.as_view(), name='newpost'),
]


# urlpatterns = [
#     path('', views.postListView, name='listposts'),
#     path('post/<int:pk>/', views.postDetailView, name='detailview'),
#     path('post/<int:pk>/delete', views.postDeleteView, name='deletepost'),
#     path('post/<int:pk>/edit', views.postEditView, name='editpost'),
#     path('post/new', views.postAddView, name='newpost'),
# ]
