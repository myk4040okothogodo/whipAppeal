from whippAPI.user.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  links = serializers.SerializerMethodField('get_links')
  class Meta:
    model = User
    fields = ['id', 'username','email', 'is_active', 'date_joined','links',]
    read_only_field = ['is_active', 'date_joined']
    
  def get_links(self, obj):
    request = self.context['request']
    username = obj.get_username()
    return {
      'self': reverse('user-detail',
      kwargs={User.USERNAME_FIELD: username}, request=request),
      }  
  
  """
  def update(self, instance, validated_data):
    Performs an update on a User.
    
    passwords shouldnt be handled with 'setattr', unlike other fields,Django provides
    a function that handles hashing and salting of passwords.That means we need to remove
    the password field from validated data before iterating over it.
    
    password = validated_data.pop('password', None)
    for (key, value) in validated_data.items():
      #for the keys remaining in 'validated_data', we will set them on the current current
      #'User' instance one at a time.
      setattr(instance, key, value)
      
    if password is not None:
      # '.set_password()' handles all
      # of the security stuff we shouldnt be concerned with
      instance.set_password(password)
    #After everything has been updated we must explicitly save the model
    #'.set_password()' deosnt save the model
    instance.save()
    return instance
  """
  
