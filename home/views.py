from django.http import FileResponse, HttpResponse
from django.shortcuts import render
import pandas as pd
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
import io
import xlsxwriter
class FileConvertView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            #file_serializer.save()
            input = request.data
            input = input['file']
            try:
                df = pd.read_csv(input)
                output = df.to_excel('media/output.xlsx', index=False, header=True)
                file = open('media/output.xlsx', 'rb')
                data = file.read()
                response = HttpResponse(
                data,
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
                response['Content-Disposition'] = 'attachment; filename=output.xlsx'
                return response
            except:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)