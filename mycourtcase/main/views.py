

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from main.forms import LoginForm
#
# from flask import render_template, flash, redirect, url_for, session, Markup, request, g
# from app import app
# from app import models as mdl

# from flask.ext.login import login_user, logout_user, current_user, login_required


def home_page(request):

    # return HttpResponse("Hello")
    if request.method =='GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            print(name)
            return HttpResponse(name)




    # session['complaint_or_search'] = form.complaint_or_search.data
    #
    # complaint_or_search = session['complaint_or_search']
    #
    # if complaint_or_search == 'search':
    #     return redirect(url_for('search'))
    # elif complaint_or_search == 'complaint':
    #     return redirect(url_for('choose_complaint_type'))

    return render(request, 'main/home.html', {'form':form,})
