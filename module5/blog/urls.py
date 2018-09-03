from django.urls import path

from . import views

# Class - based
urlpatterns = [
 path('', views.BlogListView.as_view(), name='viewblogs'),
 path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
]

# Function - based
# urlpatterns = [
#     path('', views.blogListView, name='viewblogs'),
#     path('post/<int:pk>/', views.blogDetailView, name='post_detail'),
# ]
