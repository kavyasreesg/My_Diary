from django.shortcuts import render
from .models import ActivityData
from django.http import HttpResponseRedirect


# Create your views here.
def display_activities(request):
    get_form_data = ActivityData.objects.all()
    return render(request, 'index.html', {'form': get_form_data})


def save_form_data(request):
    x = request.POST['content']
    object_new = ActivityData(text_from_user=x)
    object_new.save()
    return HttpResponseRedirect('/add_activity_list/')
