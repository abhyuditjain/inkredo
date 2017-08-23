# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from company_api.models import Company
from company_api.serializers import CompanySerializer
from rest_framework import viewsets

class CompanyView(viewsets.ModelViewSet):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer
