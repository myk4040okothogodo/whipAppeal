from rest_framework import serializers
from .models import Account
from rest_framework.reverse import reverse
from .user.models import User


class AccountSerializer(serializers.ModelSerializer):
  links = serializers.SerializerMethodField('get_links')
  owner = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, read_only=True)
  class Meta:
    model = Account
    fields = ('id', 'owner','is_premium','is_active', 'account_balance','links',)
  def get_links(self, obj):
    request =self.context['request']
    return { 'self': reverse('account-detail', kwargs={'pk': obj.pk}, request=request),}  
