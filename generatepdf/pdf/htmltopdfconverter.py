from django.http import HttpResponse, StreamingHttpResponse
from wsgiref.util import FileWrapper
from .s3file import *
from .serializers import htmltopdfserializer
import pdfkit
import os
from .models import MyModel
from rest_framework import generics
from rest_framework.response import Response

# path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"   # give path of the wkhtmltopdf for windows#

# config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)




class htmltopdfview(generics.GenericAPIView):
    serializer_class = htmltopdfserializer
    
    def post(self,request):
        """ for windows
        path_to_file = 'responses.html'
        path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
        for Ubuntu/Debian
        sudo apt-get install wkhtmltopdf """
        htmlfile =  request.FILES['image_url']
        title = request.data.get('title')
        description = request.data.get('description')
        #if filename and details needed to be saved in database uncomment belwo lines# 
        ## from here
        a= MyModel()
        a.title = title 
        a.description = description
        a.image_url=htmlfile
        a.save()
        id = a.id
        queryset = MyModel.objects.get(id = id)
        x = queryset.image_url
        htmlResp = queryset.image_url
        print("--------------------------",htmlfile)
        ## upto here

        htmlResp = x
        global pdfname
        pdfname = f'Madhutest.pdf'
        # pdfkit.from_file(open(f'{htmlResp}'), output_path=f'{pdfname}', configuration=config, options={"enable-local-file-access": ""})
        pdfkit.from_file(open(f'{htmlResp}'), output_path=f'{pdfname}', options={"enable-local-file-access": ""})
        # import base64
        # with open(pdfname, "rb") as pdf_file:
        #     encoded_string = base64.b64encode(pdf_file.read())
        #     print(encoded_string)        
        x=upload_file(pdfname)       
        return Response({"url" :x})


class DocumentRE(generics.GenericAPIView):
    serializer_class = htmltopdfserializer
    queryset = MyModel.objects.all()

    def get(self, request, id, format=None):
            queryset = MyModel.objects.get(id=id)
            file_handle =queryset  
            response = StreamingHttpResponse(FileWrapper(file_handle),
                                    content_type='application/zip; charset=utf-8')
            response['Content-Disposition'] = 'attachment; filename={}'.format(file_handle)
            return response


from django.shortcuts import render
from .forms import Profile_Form
from .models import User_Profile

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def create_profile(request):
    form = Profile_Form()
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
           
            user_pr.save()
            return render(request, 'details.html', {'user_pr': user_pr})
    context = {"form": form,}
    return render(request, 'create.html', context)