from datetime import datetime

from django.shortcuts import render


def index(request):
    context = {"current_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
    return render(request, "core/index.html", context)
