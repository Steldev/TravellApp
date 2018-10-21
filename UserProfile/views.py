from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from UserProfile.forms import *

from UserProfile.forms import *

from Lib.FileFormats import check_files_formats

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

    posts = user.note_set.all().order_by('-date_public')

    data = {
        'user': user,
            'status': status,
            'is_owner': False,
        'posts': posts,
            }

    if user_id == request.user.pk:
        data['is_owner'] = True

    return render(request, "UserProfile/home.html", data)


@login_required
def post_create_page(request):
    user = request.user

    if request.method == 'POST':
        form_note = NoteForm(request.POST)
        form_attach = AttachmentForm(request.POST, request.FILES)
        errors_file_type = []
        if form_note.is_valid():

            files = request.FILES.getlist('images')
            for file in files:
                if not check_files_formats(file.name, 'IM'):
                    errors_file_type.append("don`t support this file extension for image file")

            files = request.FILES.getlist('video')
            for file in files:
                if not check_files_formats(file.name, 'VD'):
                    errors_file_type.append("don`t support this file extension for video file")

            files = request.FILES.getlist('audio')
            for file in files:
                if not check_files_formats(file.name, 'AU'):
                    errors_file_type.append("don`t support this file extension for audio file")

            files = request.FILES.getlist('file')
            for file in files:
                if not check_files_formats(file.name, 'FL'):
                    errors_file_type.append("don`t support this file extension")

            if not errors_file_type:
                new_post = form_note.save(commit=False)
                new_post.user = user
                new_post.save()

                files = request.FILES.getlist('images')
                for file in files:
                    new_attachment = Attachment(note=new_post, file=file, type='IM')
                    new_attachment.save()

                files = request.FILES.getlist('video')
                for file in files:
                    new_attachment = Attachment(note=new_post, file=file, type='VD')
                    new_attachment.save()

                files = request.FILES.getlist('audio')
                for file in files:
                    new_attachment = Attachment(note=new_post, file=file, type='AU')
                    new_attachment.save()

                files = request.FILES.getlist('file')
                for file in files:
                    new_attachment = Attachment(note=new_post, file=file, type='FL')
                    new_attachment.save()

                return HttpResponseRedirect('/user/%s/' % request.user.pk)
        else:
            return render(request,
                          'UserProfile/create_post.html',
                          {'form_note': form_note,
                           'form_attach': form_attach,
                           'errors_type': errors_file_type,
                           })
    else:
        form_note = NoteForm()
        form_attach = AttachmentForm()

    return render(request,
                  'UserProfile/create_post.html',
                  {'form_note': form_note,
                   'form_attach': form_attach
                   })
