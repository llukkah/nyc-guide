from django.shortcuts import render
from .boroughs import boroughs

def city(request):
    if request.method == 'GET':
        return render(request=request, template_name='city.html', context={ 'boroughs': boroughs.keys() })

# /brooklyn
#/staten island
def borough(request, borough):
    if request.method == 'GET':
        return render(request=request, template_name='borough.html', context={ 'borough': borough, 'activities': boroughs[borough].keys() })

# Create your views here.
#/brooklyn/beaches
#/stateisalnd/bridges
def activity(request, borough, activity):
    # pass
    if request.method == 'GET':
        return render(request=request, template_name='activity.html', context={'borough': borough, 'activity': activity, 'activities': boroughs[borough][activity].keys()})
        # [parks, zoo,s beaches]

#statenisland/bridges/verazzano
#brooklyn/parks/prospectpark
def venue(request, borough, activity, venue):
    # pass
    if request.method == 'GET':
        return render(request=request, template_name='venue.html', context={
            #brooklyn
            'borough': borough,
            #parks, zoos
            'activity': activity,
            'venue': venue,
            'description': boroughs[borough][activity][venue].get('description')
        })