# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from maintenance.models import MaintenanceRequest
from maintenance.serializers import MaintenanceReadSerializer, MaintenancePostSerializer, MaintenanceUpdateSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

from rest_framework.response import Response

class MaintenanceListView(APIView):

    def get(self, request, apartment_key='0'):
        if (apartment_key == '0'):
            maint_requests = MaintenanceRequest.objects.exclude(status='complete').order_by('date_submitted')
        else:
            maint_requests = MaintenanceRequest.objects.filter(apartment_no=apartment_key).exclude(status='complete').order_by('date_submitted')

        serializer = MaintenanceReadSerializer(maint_requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        this_req = request.data

        this_req['resident'] = 1
        this_req['category'] = 1
        this_req['staff'] = [1]

        serializer = MaintenancePostSerializer(data=this_req)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            #################### END POST RELATED METHODS ####################


class MaintenanceUpdateView(APIView):

    def get(self, request, maint_id='0'):
        if (maint_id != '0'):
            maint_request = MaintenanceRequest.objects.get(id=maint_id)

            serializer = MaintenanceReadSerializer(maint_request)
            return Response(serializer.data)

    def post(self, request, maint_id='0'):
        if (maint_id != '0'):
            this_update = request.data
            this_update['request'] = maint_id

            ## Update the status of maintenance request object
            maint_request = MaintenanceRequest.objects.get(id=maint_id)
            maint_request.status = this_update['update_type']
            maint_request.save()

            serializer = MaintenanceUpdateSerializer(data=this_update)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                #################### END POST RELATED METHODS ####################
