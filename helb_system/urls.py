from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>🏦 HELB Payment System</h1>
        <p>🚀 Your Django app is running!</p>
        <ul>
            <li><a href="/admin/">📋 Admin Panel</a></li>
            <li><a href="/api/">📡 API</a></li>
        </ul>
        <hr>
        <p style="color: green;">✅ Deployed successfully!</p>
    """)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
]
