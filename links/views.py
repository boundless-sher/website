from django.shortcuts import render
from .models import Link

# Create your views here.
def link_list(request):
  links = Link.objects.all()
  return render(request, 'links/links.html', {'links': links})