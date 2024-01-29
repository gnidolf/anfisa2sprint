from django.shortcuts import render
from django.db.models import Q
from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'

    ice_cream_list = IceCream.objects.values('id', 'title').filter(
        Q(is_published=True), Q(is_on_main=True) | Q(title__contains='пломбир')
        )

    context = {'ice_cream_list': ice_cream_list}
    return render(request, template, context)
