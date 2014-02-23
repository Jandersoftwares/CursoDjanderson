# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render

def home(request):
	return render (request, 'index.html', {})