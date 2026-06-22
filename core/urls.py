from django.urls import path
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({
        'message': 'HELB API is working!',
        'status': 'success',
        'endpoints': ['/api/requests/', '/api/departments/']
    })

urlpatterns = [
    path('', api_home, name='api-home'),
]
