import subprocess

from django.shortcuts import HttpResponse, render
from django.http import JsonResponse
from .models import Service


# Create your views here.

def check_status(request, service_name):
    status = subprocess.Popen(['systemctl', 'is-active', service_name],
                              stdout=subprocess.PIPE).communicate()[0].decode().strip('\n')

    return HttpResponse(status)
    # return JsonResponse({'status': status})


def check_status_alternative(request, service_name):
    with  open('status', 'r') as st:
        status = st.read()

    return JsonResponse({'status': status})


def process(process_name):
    cmd = 'ps aux | egrep "python|PID'
    result = subprocess.Popen([])


def dashboard(request):
    services = Service.objects.all()

    return render(request, 'service_checker/dashboard.html', {'services': services})
