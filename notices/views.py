from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Notice
from django.core import serializers


# Create your views here.
@csrf_exempt
def notice_list(request):
    notices = Notice.objects.all()
    notices_list = []

    for notice in notices:
        notice_dict = {
            "id": notice.id,
            "title": notice.title,
            "content": notice.content,
            "date_posted": notice.date_posted,
        }
        notices_list.append(notice_dict)

    return JsonResponse({"notices": notices_list})


@csrf_exempt
def add_notice(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print("Received data:", data)  # Log the received data
        title = data.get('title')
        content = data.get('content')
        
        notice = Notice.objects.create(title=title, content=content)
        return JsonResponse({'message': 'Notice added successfully', 'id': notice.id})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def edit_notice(request, id):
    try:
        notice = Notice.objects.get(id=id)
        if request.method == 'PUT':
            data = json.loads(request.body)
            notice.title = data.get('title', notice.title)
            notice.content = data.get('content', notice.content)
            notice.save()
            return JsonResponse({'message': 'Notice updated successfully'})
        else:
            data = {
                "id": notice.id,
                "title": notice.title,
                "content": notice.content,
                
            }
            return JsonResponse(data)
    except Notice.DoesNotExist:
        return JsonResponse({'error': 'Notice not found'}, status=404)

@csrf_exempt
def delete_notice(request, id):
    if request.method == 'DELETE':
        try:
            notice = Notice.objects.get(id=id)
            notice.delete()
            return JsonResponse({'message': 'Notice deleted successfully'})
        except Notice.DoesNotExist:
            return JsonResponse({'error': 'Notice not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
