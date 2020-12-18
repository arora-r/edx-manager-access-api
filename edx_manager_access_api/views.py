import json
from django.http import HttpResponse
from decorators import basicauth
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@basicauth
def enable(request):
    """
    enable a manager to have studio and django access
    """
    # Need to find the user
    # If found then set acess to true and return success
    # If not found then return failed status


@csrf_exempt
@basicauth
def disable(request):
    """
    removes a manager from having studio and django access
    """
    # Find user
    # If found then set access to false and return success
    # If not found then return failed status