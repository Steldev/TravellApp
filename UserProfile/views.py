from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from UserProfile.forms import *
from django.template.loader import render_to_string

from UserProfile.forms import *
from UserProfile.models import save_attach

import datetime

from Lib.FileFormats import handle_uploaded_file



# Create your views here.


def home(request, user_id):

    user = get_object_or_404(User, pk=user_id)

    try:
        user_info = UserInfo.objects.get(pk=user.pk)
    except UserInfo.DoesNotExist:
        user_info = None

    status = 'none'
    if user_info:
        status = user.userinfo.STATUS_TYPE[request.user.userinfo.status]

    notes = Note.note_objects.get_latest_note(user.pk)


    data = {
        'user': user,
        'status': status,
        'is_owner': False,
        'notes': notes,
            }

    if user_id == request.user.pk:
        data['is_owner'] = True

    return render(request, "UserProfile/home.html", data)


def load_notes(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.is_ajax():
        notes = Note.note_objects.get_latest_note(user.pk)

        data = {
            'notes': notes,
        }
        page = render_to_string('UserProfile/notes_list.html', data)
        response = {'html': page}
        return JsonResponse(response)

    return Http404


@login_required
def note_page(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    is_owner = (request.user == note.user)
    data = {
        'note': note,
        'is_owner': is_owner,

    }
    return render(request, 'UserProfile/note_page.html', data)


@login_required
def note_create_page(request):
    user = request.user
    errors_file_type = []

    if request.method == 'POST':
        form_note = NoteForm(request.POST)
        form_attach = AttachmentForm(request.POST, request.FILES)

        if form_note.is_valid() and form_attach.is_valid():

            errors_file_type = handle_uploaded_file(request.FILES)

            if not errors_file_type:
                new_note = form_note.save(commit=False)
                new_note.user = user
                new_note.save()

                save_attach(request.FILES, new_note)

                return HttpResponseRedirect('/user/%s/' % request.user.pk)
    else:
        form_note = NoteForm()
        form_attach = AttachmentForm()

    return render(request,
                  'UserProfile/create_note.html',
                  {'form_note': form_note,
                   'form_attach': form_attach,
                   'errors_type': errors_file_type,
                   })


@login_required
def note_edit_page(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.user != note.user:
        return Http404

    form_note = NoteForm(instance=note)

    return render(request,
                  'UserProfile/edit_note.html',
                  {'form_note': form_note,
                   'note': note,
                   })
