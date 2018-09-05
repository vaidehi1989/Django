from django.contrib import admin
from django.urls import include, path
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('blog/', views.blogListView, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),  # new

]
