from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import LibrarySerializers
from ..models import LibraryBooks

@api_view(['GET','POST'])
def BookInfo(request):
    if request.method == 'GET':
        data = LibraryBooks.objects.all()
        serial = LibrarySerializers(data,many=True)
        return Response(serial.data)
    elif request.method == 'POST':
        serial = LibrarySerializers(data=request.data)
        if serial.is_valid():
            title = serial.data['title']
            author = serial.data['author']
            bid = serial.data['bid']
            date = serial.data['date']
            duedate = serial.data['duedate']
            data = LibraryBooks.objects.create(
                title = title,
                author= author,
                bid =bid,
                date = date,
                duedate = duedate,
            )
            data.save()
            return Response("Successfully borrowed")
        else:
            return Response(serial.errors)
            
