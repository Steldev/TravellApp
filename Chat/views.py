from django.shortcuts import render

from django.utils.safestring import mark_safe
import json

def chat_list_page(request):
    """"Чат поиск"""
    return render(request, 'Chat/chat_select')

def chat_page(request, room_name):
    """"Чат"""
    return render(request, 'Chat/chat_room.html',
                  {
                      'room_name_json': mark_safe(json.dumps(room_name))
                  }
                  )
