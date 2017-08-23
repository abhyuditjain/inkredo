from rest_framework import serializers

from company_api.models import Company, User

class CompanySerializer(serializers.ModelSerializer):
    """
    Serializing all the Companies
    """
    class Meta:
        model = Company
        fields = ('id', 'company_name', 'created_at', 'updated_at')