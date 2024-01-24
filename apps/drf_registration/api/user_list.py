from rest_framework import serializers,generics

from apps.drf_registration.models import CustomUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('id','first_name','username','email','role','is_active')
        
        
class OtherUserListAPIView(generics.ListAPIView):
    """
    This is used to get list of other users.
    """
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['is_active','role']  # Add the fields you want to use for filtering
    search_fields = ['first_name', 'email', 'role']  # Add the fields you want to use for searching
    ordering_fields = ['first_name', 'email', 'role']  # Add the fields you want to use for ordering
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.filter(is_staff=False,is_superuser=False)
    
    def get_queryset(self):
        #exclude role admin and role tutor
        
        return self.queryset.exclude(role__in=['admin','tutor'])
        