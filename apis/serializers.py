from rest_framework import serializers
from listazadan .models import Zadanie
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    zadanie = serializers.SlugRelatedField(slug_field='title',many=True, queryset=Zadanie.objects.all())
    queryset=Zadanie.objects.all()
    pending_count = serializers.SerializerMethodField()
    def get_pending_count(self, obj):
       
       return Zadanie.objects.filter(status='U').count()
    class Meta:
        model = User
        fields = ['id', 'username','pending_count', 'zadanie']




class ZadanieSerializer(serializers.ModelSerializer):
  
  title = serializers.CharField(max_length=100, required=True)
  description = serializers.CharField(max_length=500, required=True)
  status = serializers.CharField(max_length=1, required=True)
  user = serializers.SlugRelatedField(slug_field='username',queryset=User.objects.all(), required = True)
  deadline = serializers.DateField(required=True)
  '''

  def create(self, validated_data):
    
    return Zadanie.objects.create(
      title=validated_data.get('title'),
      description=validated_data.get('description'),
      status=validated_data.get('status'),
      user=validated_data.get('user'),
      deadline=validated_data.get('deadline')
    )

  def update(self, instance, validated_data):
     
    instance.title = validated_data.get('title', instance.title)
    instance.description = validated_data.get('description', instance.description)
    instance.status = validated_data.get('status', instance.status)
    instance.user = validated_data.get('user', instance.user)
    instance.deadline = validated_data.get('deadline', instance.deadline)
    instance.save()
    return instance
 '''
  class Meta:
     model = Zadanie
     fields = (
       'id',
       'title',
       'description',
       'status',
       'user',
       'deadline'
     )