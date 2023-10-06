from django.shortcuts import render

from django.shortcuts import get_object_or_404


def show_menu(request, name):
    context = {}
    return render(request, 'menu/index.html', context)
