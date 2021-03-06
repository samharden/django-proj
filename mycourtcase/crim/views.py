
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

            county = crimform.cleaned_data['county']
            print(county)

            if case_type == 'dui' and county == 'hillsb':
                hillsb_judge = HillsboroughJudges()
                return HttpResponseRedirect('fl/hills/hillsborough-dui.html')

            elif case_type == 'battery' and county == 'hillsb':
                hillsb_judge = HillsboroughJudges()
                return HttpResponseRedirect('fl/hills/hillsborough-battery.html')

            elif case_type == 'marijuanaposs' and county == 'hillsb':
                hillsb_judge = HillsboroughJudges()
                return HttpResponseRedirect('fl/hills/hillsborough-marijuanaposs.html')

            elif case_type == 'petit-theft' and county == 'hillsb':
                hillsb_judge = HillsboroughJudges()
                return HttpResponseRedirect('fl/hills/hillsborough-petit-theft.html')

            elif case_type == 'dwlsr' and county == 'hillsb':
                hillsb_judge = HillsboroughJudges()
                return HttpResponseRedirect('fl/hills/hillsborough-dwlsr.html')

            elif case_type == 'dui' and county == 'pinell':
                pinell_judge = PinellasJudges()
                return HttpResponseRedirect('fl/pinellas/pinellas-dui.html')

            elif case_type == 'marijuanaposs' and county == 'pinell':
                pinell_judge = PinellasJudges()
                return HttpResponseRedirect('fl/pinellas/marijuana-possession.html')
        else:
            crimform = CrimCaseTypeForm()

    # if a GET (or any other method) we'll create a blank form
    else:
        crimform = CrimCaseTypeForm()


    print("Top of index")


    return render(request, 'crim/index.html', {'crimform': crimform})
