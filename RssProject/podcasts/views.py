from django.shortcuts import render
from .parsers import save_apology_line_feed_to_db
from django.http import HttpResponse
# Create your views here.

def save_to_db(request):
    save_apology_line_feed_to_db()
    return HttpResponse('OK')