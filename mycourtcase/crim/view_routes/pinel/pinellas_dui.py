
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from crim.forms import *
from crim.templates import *

def pinellas_dui(request):
    pinell_judge = PinellasJudges(request)
    crim_desc = CrimDesc(request)
    print("Pinellas DUI Page")
    if request.method == 'POST':
        print("Hello")
        pinell_judge = PinellasJudges(request.POST)
        crim_desc = CrimDesc(request.POST)

        if pinell_judge.is_valid():
            print("Valid Hello there")
            judge = pinell_judge.cleaned_data['pinell_judge']
            print(judge)
            if judge == 'farr':
                #return render(hills_dui_farr(request), 'hills_dui_farr')
                return render(request, 'crim/fl/hills/dui/farrdui.html')
            elif judge == 'greco':
                return render(request, 'crim/fl/hills/dui/grecodui.html')
            elif judge == 'jeske':
                return render(request, 'crim/fl/hills/dui/jeskedui.html')
            elif judge == 'lefler':
                return render(request, 'crim/fl/hills/dui/leflerdui.html')
            elif judge == 'mcneil':
                return render(request, 'crim/fl/hills/dui/mcneildui.html')
            elif judge == 'myers':
                return render(request, 'crim/fl/hills/dui/myersdui.html')
            elif judge == 'taylor':
                return render(request, 'crim/fl/hills/dui/taylordui.html')
            elif judge == 'notsure':
                return render(request, 'crim/fl/hills/dui/dui.html')

    else:
        hillsb_judge = HillsboroughJudges()

    return render(request, 'crim/fl/hills/hillsborough-dui.html', {'hillsb_judge': hillsb_judge})
