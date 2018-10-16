from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from UserProfile.forms import *

from UserProfile.forms import *

from Lib.FileFormats import check_files_formats

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


def post_create_page(request):
    user = request.user

    if request.method == 'POST':
        form_note = NoteForm(request.POST)
        form_attach = AttachmentForm(request.POST, request.FILES)

        if form_note.is_valid() and form_attach.is_valid():

            files = request.FILES.getlist('files')
            exts = []
            for file in files:
                exts.append(file.name.split('.')[-1])

            types_files = check_files_formats(exts)
            itr = iter(types_files)

            if types_files:

                new_post = form_note.save(commit=False)
                new_post.user = user
                new_post.save()

                for file in files:
                    new_attachment = Attachment(note=new_post, file=file, type=next(itr))
                    new_attachment.save()

                return HttpResponseRedirect('/user/%s/' % request.user.pk)

            else:
                error = "dont support file extension"
                return render(request,
                              'UserProfile/create_post.html',
                              {'form_note': form_note,
                               'form_attach': form_attach,
                               'error': error,
                               })

    else:
        form_note = NoteForm()
        form_attach = AttachmentForm()

    return render(request,
                  'UserProfile/create_post.html',
                  {'form_note': form_note,
                   'form_attach': form_attach
                   })
