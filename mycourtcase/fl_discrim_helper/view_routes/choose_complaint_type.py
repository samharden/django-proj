from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question
from django.http import Http404
from .forms import *


def choose_complaint_type():
    form = complaintform()
    session['what_kind_complaint'] = form.what_kind_complaint.data

    what_kind_complaint = session['what_kind_complaint']

    if what_kind_complaint == 'pub_acc':
        return redirect(url_for('pub_acc_complaint_assistant'))
    elif what_kind_complaint == 'emp':
        return redirect(url_for('workplace_complaint_assistant'))


    return render_template('choose-complaint-type.html',
                           title='Complaint Builder',
                           form=form
                           )
