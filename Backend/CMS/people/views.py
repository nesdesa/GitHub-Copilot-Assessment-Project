from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from rest_framework import serializers
from rest_framework import status

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/person',
        'Search by Name': '/?name=name',
        'Search by Email': '/?email=email',
        'Add': '/person',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
 
    return Response(api_urls)

@api_view(['GET','POST'])
def people(request):
    if request.method == 'GET':
        people = Person.objects.all()
        people_serializer = PersonSerializer(people, many=True)
        return Response(people_serializer.data)
    
    elif request.method == 'POST':
        person = PersonSerializer(data=request.data)
    
        # validating for already existing data
        if Person.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This data already exists')
    
        if person.is_valid():
            person.save()
            return Response(person.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET','PUT','DELETE'])
def person(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        person_serializer = PersonSerializer(person)
        return Response(person_serializer.data)
    
    elif request.method == 'PUT':
        person_serializer = PersonSerializer(person, data=request.data)
        if person_serializer.is_valid():
            person_serializer.save()
            return Response(person_serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)