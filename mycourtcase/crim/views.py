
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from crim.forms import *
from crim.templates import *
# from crim.templates.crim.fl.hills.battery import hillsborough_battery

# Create your views here.


def index(request):
    crimform = CrimCaseTypeForm(request.POST)

    if request.method == 'POST':
        print("Hello")
        crimform = CrimCaseTypeForm(request.POST)

        if crimform.is_valid():
            print("Valid index")
            case_type = crimform.cleaned_data['case_type']
            print(case_type)
            state = crimform.cleaned_data['state']
            print(state)
            county = crimform.cleaned_data['county']
            print(county)

            if case_type == 'dui' and county == 'hillsb':
                hillsb_judge = HillsboroughJudges()
                return HttpResponseRedirect('hillsborough-dui.html')

            elif case_type == 'battery' and county == 'hillsb':
                hillsb_judge = HillsboroughJudges()
                return HttpResponseRedirect('fl/hills/hillsborough-battery.html')
                # return hillsborough_battery(request, hillsb_judge)

            elif case_type == 'dui' and county == 'pinell':
                pinell_judge = PinellasJudges(request.POST)
                return render(request, 'crim/pinellas.html', {'pinell_judge': pinell_judge})
        else:
            crimform = CrimCaseTypeForm()

    # if a GET (or any other method) we'll create a blank form
    else:
        crimform = CrimCaseTypeForm()


    print("Top of index")


    return render(request, 'crim/index.html', {'crimform': crimform})

def pinellas(request):
    pinell_judge = PinellasJudges(request.POST)
    print("Pinellas Page")
    if request.method == 'POST':
        print("Hello")
        pinell_judge = PinellasJudges(request.POST)
        if crimform.is_valid():
            print("Valid")
            pinell_judge = PinellasJudges(request.POST)
            print(judge)
    else:
        pinell_judge = PinellasJudges()

    return render(request, 'crim/pinellas.html', {'pinell_judge': pinell_judge})

def hillsborough_dui(request):
    hillsb_judge = HillsboroughJudges(request)
    crim_desc = CrimDesc(request)
    print("Hillsborough Page")
    if request.method == 'POST':
        print("Hello")
        hillsb_judge = HillsboroughJudges(request.POST)
        crim_desc = CrimDesc(request.POST)

        if hillsb_judge.is_valid():
            print("Valid Hello there")
            judge = hillsb_judge.cleaned_data['hillsb_judge']
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

    return render(request, 'crim/hillsborough-dui.html', {'hillsb_judge': hillsb_judge})

def hillsborough_battery(request):
    hillsb_judge = HillsboroughJudges(request)
    crim_desc = CrimDesc(request)
    print("Hillsborough Battery Page")
    if request.method == 'POST':
        print("Hello")
        hillsb_judge = HillsboroughJudges(request.POST)
        crim_desc = CrimDesc(request.POST)

        if hillsb_judge.is_valid():
            print("Valid Hello there")
            judge = hillsb_judge.cleaned_data['hillsb_judge']
            print(judge)
            if judge == 'farr':
                #return render(hills_dui_farr(request), 'hills_dui_farr')
                return render(request, 'crim/fl/hills/battery/farrbattery.html')
            elif judge == 'greco':
                return render(request, 'crim/fl/hills/battery/grecobattery.html')
            elif judge == 'jeske':
                return render(request, 'crim/fl/hills/battery/jeskebattery.html')
            elif judge == 'lefler':
                return render(request, 'crim/fl/hills/battery/leflerbattery.html')
            elif judge == 'mcneil':
                return render(request, 'crim/fl/hills/battery/mcneilbattery.html')
            elif judge == 'myers':
                return render(request, 'crim/fl/hills/battery/myersbattery.html')
            elif judge == 'taylor':
                return render(request, 'crim/fl/hills/battery/taylorbattery.html')
            elif judge == 'notsure':
                return render(request, 'crim/fl/hills/battery/battery.html')

    else:
        hillsb_judge = HillsboroughJudges()

    return render(request, 'crim/fl/hills/hillsborough-battery.html', {'hillsb_judge': hillsb_judge})


# def hills_dui_farr(request):
#
#     return render(request, 'crim/farrdui.html')
