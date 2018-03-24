# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
class HomeView(TemplateView):
    template_name = 'index.html'

from Main import testOpen

def buttonTest(request):
    if request.method == 'POST':
        testOpen("test_data")