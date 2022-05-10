from asyncio import events
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import views, serializers, status
from rest_framework.response import Response
from .models import Contact, Event

# Create your views here.
class EventListApi(views.APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Event
            fields = ('id',
                      'type', 
                      'name', 
                      'description', 
                      'reg_fee', 
                      'rules')


    def get(self, request):
        events = Event.objects.all()
        data = self.OutputSerializer(instance=events, many=True).data
        return Response(data)


class EventTypeListApi(views.APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Event
            fields = ('id',
                      'type', 
                      'name', 
                      'description', 
                      'reg_fee', 
                      'rules')


    def get(self, request, type):
        events = Event.objects.filter(type=type)
        data = self.OutputSerializer(instance=events, many=True).data
        return Response(data)


class EventDetailApi(views.APIView):
    class ContactSerializer(serializers.ModelSerializer):
        class Meta:
            model = Contact
            fields = ('id', 'name', 'phone')

    contacts = ContactSerializer(many=True)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Event
            fields = ('type', 
                      'name', 
                      'description', 
                      'reg_fee', 
                      'rules')
                    
    def get(self, request, pk):
        event = None
        try:
            event = Event.objects.get(id=pk)
        except (Event.DoesNotExist) as e:
            return Response({"Error": "Event does not exist!"}, status=status.HTTP_400_BAD_REQUEST)
        contacts = event.contacts.all()
        event_data = self.OutputSerializer(instance=event).data 
        contact_data = self.ContactSerializer(instance=contacts, many=True).data
        event_data['contacts'] = contact_data
        return Response(event_data)