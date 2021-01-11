from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from .models import Note

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/note-list/',
        'Detail View': '/note-detail/<str:pk>/',
        'Create': '/note-create/',
        'Update': '/note-update/<str:pk/',
        'Delete': '/note-delete/<str:pk/',
    }

    return Response(api_urls)

@api_view(['GET'])
def note_list(request):
    notes = Note.objects.all().order_by('-id')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_note(request):
    serializer = NoteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def note_detail(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note)
    return Response(serializer.data)

@api_view(['POST'])
def update_note(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(data=request.data, instance=note)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()

    return Response('Item Deleted')