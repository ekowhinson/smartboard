from django.db.models import fields
from rest_framework import serializers
from .models import MenuGroup

class MenuGroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','code','name','description','date',)
        model=MenuGroup