from django.urls import path

from . import views

# Class - based
# urlpatterns = [
#     path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
#     path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
#     path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
#     path('', views.BlogListView.as_view(), name='viewblogs'),
#     path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
# ]

# Function - based
urlpatterns = [
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('', views.blogListView, name='viewblogs'),
    path('post/<int:pk>/', views.blogDetailView, name='post_detail'),
]

