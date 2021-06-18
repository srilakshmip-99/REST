from django.db import models
from django.db.models import fields
from ..models import LibraryBooks
from rest_framework import serializers

class LibrarySerializers(serializers.ModelSerializer):
    class Meta:
        model = LibraryBooks
        fields = ['id','title','author','bid','date','duedate']