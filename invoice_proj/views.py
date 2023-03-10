from django.http import HttpResponse
from invoices.models import Invoice
from django.shortcuts import render


def hello_world_view(request):
    obj = Invoice.objects.get(id=1)
    # print(obj.get_tags())
    # print(obj.get_positions())
    qs = Invoice.objects.all()
    # print(obj.__dict__)
    # print('********')
    # print(qs.query)
    context = {
        'obj_': obj,
        'qs': qs    # by default it is set to object list
    }
    return render(request, 'home.html', context)
    # return HttpResponse("Hello World")
