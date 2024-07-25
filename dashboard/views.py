from django.shortcuts import render
from . import models


def main(request):
    return render(request, 'index.html')
