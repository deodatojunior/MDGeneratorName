from django.contrib import auth as autent
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import connections
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import os
import datetime
import requests
import names

def index(request):
    type
    if request.method == 'POST':
        abc = [{'name': names.get_first_name(gender='female')}]
    else:
        abc = [{'name': 'no name'}]
    return render(request, 'index.html', {'lista': abc})

