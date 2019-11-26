"""Houston views"""

from django.http import HttpResponse

#Utilities
from datetime import datetime
import json

def hello_world(request):
  """Return a greating"""
  now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
  return HttpResponse('Oh, hi! Current server time is {now}'.format(
    now=now
  ))

def sort_integers(request):
  """Hi"""
  #import pdb; pdb.set_trace()
  numbers = [int(i) for i in request.GET['numbers'].split(',')]
  sorted_ints = sorted(numbers)
  data = {
    'status': 'ok',
    'numbers': sorted_ints,
    'message': 'Ahuevo!'
  }
  return HttpResponse(
    json.dumps(data), 
    content_type='application/json'
  )

def say_hi(request, name, age):
  """return a greating"""
  if age < 12:
    message = 'Sorry {}, you are not allowed here'.format(name)
  else:
    message = 'Hello {}, welcome to my world'.format(name)
  return HttpResponse(message)
  