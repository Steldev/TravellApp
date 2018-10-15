from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


from UserProfile.forms import *

# Create your views here.


def home(request, user_id):

    user = get_object_or_404(User, pk=user_id)

    status = user.userinfo.STATUS_TYPE[request.user.userinfo.status]

    data = {'user': user,
            'status': status,
            'is_owner': False,
            }

    if user_id == request.user.pk:
        data['is_owner'] = True

    return render(request, "UserProfile/home.html", data)


def registration_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/user/')
    else:
        form = RegistrationForm()
    return render(request, 'Registration/registration_page.html', {'form': form})
