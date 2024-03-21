from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scholarships/', include('scholarships.urls')),
      # Include the URLs of the scholarships app
]
