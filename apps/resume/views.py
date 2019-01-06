# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'resume/index.html')

def experience(request):
    return render(request, 'resume/experience.html')

def education(request):
    return render(request, 'resume/education.html')

def contact(request):
    return render(request, 'resume/contact.html')
