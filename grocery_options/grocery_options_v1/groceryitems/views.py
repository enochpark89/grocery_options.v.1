from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Groceryitems


def index(request):
  items = Groceryitems.objects.all().values()
  template = loader.get_template('index.html')
  # Create an object that contain data.
  context = {
    'items': items,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  post_date = request.POST['post_date']
  company_name = request.POST['company_name']
  price = request.POST['price']
  condition = request.POST['condition']
  brand_name = request.POST['brand_name']
  item_name = request.POST['item_name']
  item = Groceryitems(
    post_date=post_date, 
    company_name=company_name, 
    price=price, 
    condition=condition, 
    brand_name=brand_name, 
    item_name=item_name)
  item.save()
  return HttpResponseRedirect(reverse('index'))