# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib import auth
from django.shortcuts import render


# Create your views here.


def logout(request):
    auth.logout(request)
    return redirect('/')
