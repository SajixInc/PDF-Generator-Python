import requests
import pdfkit
from django.http import HttpResponse
from django.template.loader import get_template
import codecs
from datetime import datetime
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import os
from rest_framework import generics
from .serializers import PdfGenerationSerializer

Lifeeazy_Url = 'https://.........'
token = 'mention your bearer token'

from django.shortcuts import render, redirect
from .models import Image
from .form import Imageform 
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = Imageform(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            output = form.instance
            return render(request, 'index.html', {'output': output})
    else:
        form = Imageform()
    img = Image.objects.all()
    return render(request, 'index.html', {'img': img, 'form': form})


# def index1(request):
#     if request.POST.get('nameofimage') and request.POST.get('photo') :
#         saverecord = Image()
#         saverecord.id = request.POST.get('nameofimage')
#         saverecord.firstname = request.POST.get('photo')
#         saverecord.save()
#         messages.success(request, 'record inserted successfully')
#         # return redirect(request,'index.html')
#     return render(request, 'index.html')

def read(request):
    a = Image.objects.all()
    return render(request, 'read.html', {"Image": a})

from .htmltopdfconverter import htmltopdfview
htmltopdfview()

def getSummary(id):
    summaryapi = Lifeeazy_Url + 'User/GetAllUserSummary/{}'.format(id)
    assementapi = Lifeeazy_Url + 'UserAssessment/GetAllSessionScoreAssessmentViewV2/{}'.format(id)
    immunizationapi = Lifeeazy_Url + 'Immunization/ImmunizationGetUserId/{}'.format(id)
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer ' + token}

    summaryResponse = requests.get(url=summaryapi, headers=headers)
    assementResponse = requests.get(url=assementapi, headers=headers)
    immunizationResponse = requests.get(url=immunizationapi, headers=headers)
    overall_immunizationsRes = requests.get(url=immunizationapi, headers=headers)
    summaryData = summaryResponse.json()['Result']
    assesmentData = assementResponse.json()['Result']
    immunizationData = immunizationResponse.json()['Result']
    overall_immunizations = overall_immunizationsRes.json()['Result']
    return summaryData, assesmentData, immunizationData, overall_immunizations


html = r"D:\projects\New folder (2)\PDF-Generator-Python\generatepdf\pdf\result.html"

def htmltopdf(self):
    """ for windows
    path_to_file = 'responses.html'
    path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

    for Ubuntu/Debian
    sudo apt-get install wkhtmltopdf """

    path_to_wkhtmltopdf = r"C:\Users\madhu\Downloads\vasu\wkhtmltoimage.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

    now = datetime.now()
    global pdftime, htmlResp
    pdftime = now.strftime("%Y%m%d%H%M%S")
    htmlResp = r'D:\projects\New folder (2)\PDF-Generator-Python\generatepdf\pdf\result.html'
    global pdfname
    pdfname = f'outpdf.pdf'
    filesss = codecs.open(f'{htmlResp}', "w", "utf-8")
    filesss.write(html)
    filesss.close()

    pdfkit.from_file(open(f'{htmlResp}'), output_path=f'{pdfname}', configuration=config, options={"enable-local-file-access": ""})
    # pdfkit.from_file(open(f'{htmlResp}'), output_path=f'{pdfname}', options={"enable-local-file-access": ""})
    # global pdfpath
    pdfpath = os.path.abspath(pdfname)


def healthchart(scores_list, labels, colours):
    fig, ax = plt.subplots()
    plt.rcParams['font.size'] = 10
    if len(scores_list) > 1:
        ax.pie(scores_list, labels=labels,
               colors=colours,
               autopct=lambda p: '{:,.0f}'.format(p * sum(scores_list) / 100),
               startangle=180
               )
        plt.title("LifeStyle Scoring Chart", fontsize=10)
    else:
        ax.pie(scores_list, labels=labels,
               colors=colours,
               autopct=lambda p: ''.format(p * sum(scores_list) / 100),
               startangle=180
               )
        plt.title("No Assessment Taken", fontsize=12)

    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    img_src = 'data:image/png;base64,{}'.format(encoded)
    return img_src


def assessmentgetData(assesmentData):
    overall_sections_list = []
    risk_to_depression = assesmentData.get('Risk to Depression')
    diabetes = assesmentData.get('Risk to Diabities')
    if not risk_to_depression:
        risk_to_depression = ["---"]
    if not diabetes:
        diabetes = ["---"]

    lifestyleScoringData = assesmentData.get('Life Style Scoring')
    if lifestyleScoringData:
        dispalayName = "userAssessment"
        connectednessSection = lifestyleScoringData['ConnectednessDomainTotal']
        movementSection = lifestyleScoringData['MovementDomainTotal']
        nutritionSection = lifestyleScoringData['NutritionDomainTotal']
        recoverySection = lifestyleScoringData['RecoveryDomainTotal']
        substanceSection = lifestyleScoringData['SubstanceUseDomainTotal']
        overallLifestyle = lifestyleScoringData['Overall_Lifestyle']
        overall_Score_list = overallLifestyle
        overall_sections_list.append(connectednessSection)
        overall_sections_list.append(movementSection)
        overall_sections_list.append(nutritionSection)
        overall_sections_list.append(recoverySection)
        overall_sections_list.append(substanceSection)
        comments_list = []
        scores_list = []
        for each in overall_sections_list:
            scores_list.append(each[0])
            comments_list.append(each[1])
        colours = ['#8254d1', 'r', '#0a942a', '#3595f0', 'y']
        labels = ['Connectedness', 'Movement', 'Nutrition', 'Recovery', 'Substance']
        individual_comments_list = zip(labels, comments_list)
        overall_list = dict(sorted(individual_comments_list, key=lambda val: val[1], reverse=True))
        img_src = healthchart(scores_list, labels, colours)
    else:
        dispalayName = "userNoTakenAssessment"
        overall_Score_list = ["---", "---"]
        overall_list = [""]
        scores_list = [100]
        colours = ["#839696"]
        labels = [""]
        img_src = healthchart(scores_list, labels, colours)

    return overall_sections_list, overall_Score_list, risk_to_depression, diabetes, overall_list, img_src, dispalayName


def Get_Byid(id):
    data = getSummary(id)
    summarydata = data[0]
    assesmentData = data[1]
    immunizationData = data[2]
    all_immunizations = data[3]
    immu_list = []
    for each in all_immunizations:
        immu_list.append(each['Vaccine'])
    immunization = []
    for each in immunizationData:
        new_dict = dict()
        find_immunization = each['immunization_id']

        if len(find_immunization) != 0:
            for i in find_immunization:
                if i['FamilyId'] is None and i['UserId']:
                    new_dict['vaccine'] = each['Vaccine']
                    dates = datetime.strptime(i['Date_Of_Immunization'], '%Y-%m-%d')
                    dob = dates.strftime('%d-%b-%Y')
                    new_dict['date'] = str(dob)
                    if i['Dose_Taken']:
                        new_dict['status'] = "Completed"
                    else:
                        new_dict['status'] = "Not Completed"
                    immunization.append(new_dict)
                    break
                else:
                    new_dict['vaccine'] = each['Vaccine']
                    new_dict['date'] = "---"
                    new_dict['status'] = "---"
                    immunization.append(new_dict)
        else:
            new_dict['vaccine'] = each['Vaccine']
            new_dict['date'] = "---"
            new_dict['status'] = "---"
            immunization.append(new_dict)
    if assesmentData:
        all_assement = assessmentgetData(assesmentData)
        overall_sections_list = all_assement[0]
        overall_Score_list = all_assement[1]
        risk_to_depression = all_assement[2]
        diabetes = all_assement[3]
        overall_list = all_assement[4]
        img_src = all_assement[5]
        dispalayName = all_assement[6]
    else:
        dispalayName = "noAssessment"
        overall_Score_list = ["---", "---"]
        overall_list = [""]
        risk_to_depression = [""]
        diabetes = [""]
        scores_list = [100]
        colours = ["#839696"]
        labels = [""]
        img_src = healthchart(scores_list, labels, colours)

    profile_list = []
    firstname = ""
    email = ""
    mobilenumber = ""
    vitals_list = []
    allergies_list = []
    anthropometrics_list = []
    appointments_list = []
    dob = ""
    firstname = summarydata['Firstname']
    email = summarydata['Email']
    number = summarydata['MobileNumber']
    if len(number) == 10:
        mobilenumber = "+91 " + number[0:4] + "-" + number[4:7] + "-" + number[7:10]
    else:
        mobilenumber = number[0:3] + " " + number[3:7] + "-" + number[7:10] + "-" + number[10:13]
    a = summarydata['Profile']
    if a is None:
        my_dict = dict.fromkeys(['Gender', 'DOB', 'MartialStatus', 'BloodGroup'], "---")
        profile_list.append(my_dict)
    else:
        date = a['DOB']
        datem = datetime.strptime(date, '%Y-%m-%d')
        dob = datem.strftime('%d-%b-%Y')
        profile_list.append(summarydata['Profile'])
        vitals_list = summarydata['VitalsUserId']
        allergies_list = summarydata['AlergiesUsername']
        anthropometrics_list = summarydata['Anthropometrics']
        appointments = summarydata['appointment']
        for j in appointments:
            appointment_dict = dict()
            appointment_dict['doctorname'] = j['DoctorId']['Firstname'] + j['DoctorId']['Lastname']
            if not j['symptoms']:
                appointment_dict['symptoms'] = "None"
            else:
                appointment_dict['symptoms'] = j['symptoms']['Symptom']
            date = datetime.strptime(j['Date'], '%Y-%m-%d')
            appointment_dict['date'] = date.strftime('%d-%b-%Y')
            time = datetime.strptime(j['Time'], '%H:%M:%S')
            appointment_dict['time'] = time.strftime('%H:%M %p')
            appointment_dict['specialization'] = j['Specialization']
            appointments_list.append(appointment_dict)
    if profile_list == None:
        my_dict = dict.fromkeys(['Gender', 'DOB', 'MartialStatus', 'BloodGroup'], "---")
        profile_list.append(my_dict)
    if len(vitals_list) == 0:
        my_dict = dict.fromkeys(['Temperature', 'BP', 'Height', 'Weight', 'BMI', 'Spo2', 'Pulse'], "---")
        vitals_list.append(my_dict)

    if len(anthropometrics_list) == 0:
        my_dict = dict.fromkeys(['Height', 'Weight', 'Age', 'Gender'], "---")
        anthropometrics_list.append(my_dict)

    if len(allergies_list) == 0:
        my_dict = dict.fromkeys(['AlergiesType', 'Reactions', 'Comments'], "---")
        allergies_list.append(my_dict)

    if len(appointments_list) == 0:
        my_dict = dict.fromkeys(['date', 'time', 'doctorname', 'specialization', 'symptoms'], "---")
        appointments_list.append(my_dict)

    immunization1 = immunization[0:11]
    immunization2 = immunization[11:23]

    return firstname, email, mobilenumber, profile_list, vitals_list, anthropometrics_list, allergies_list, \
           appointments_list, dob, img_src, \
           overall_Score_list[0], overall_list, overall_Score_list[1], \
           risk_to_depression, diabetes, immunization1, immunization2, dispalayName


class Generatepdf(generics.GenericAPIView):
    serializer_class = PdfGenerationSerializer

    def post(self, request):
        id = 27
        all_data = Get_Byid(id)
        template = get_template('healthsummary.html')
        con = {'name': all_data[0], 'email': all_data[1], 'mobilenumber': all_data[2], 'profile': all_data[3][0],
               'vitals': all_data[4][0], 'anthro': all_data[5][0],
               'allergies': all_data[6][0], 'appointments': all_data[7], 'dob': all_data[8], 'imageee': all_data[9],
               'overall_Score': all_data[10],
               'overall_list': all_data[11], 'overall_lifestyle': all_data[12], 'depression': all_data[13][0],
               'diabetes': all_data[14][0], 'immunization1': all_data[15], 'immunization2': all_data[16],
               "dispalayName": all_data[17]}
        html = template.render(con)
        htmltopdf(html, id)

        imageupload = Lifeeazy_Url + "ImageUpload/DocUpload/"
        f = open(pdfpath, 'rb')

        payload = {}
        image = [
            # ('UploadDoc', (Mobile+'.pdf', open(Mobile+'.pdf', 'rb'), 'image/jpeg/pdf'))
            ('UploadDoc', (pdfname, f, 'image/jpeg/pdf'))
        ]
        Imageheaders = {
            'Accept-Language': 'en-US',
            'Authorization': f'Bearer {token}'
        }
        r = requests.request("POST", imageupload, headers=Imageheaders, data=payload, files=image)
        imageurl = r.json()['Result']
        f.close()
        doc = (imageurl.items())
        for i in doc:
            url = (i[1])

        os.remove(pdfname)
        os.remove(htmlResp)
        return HttpResponse(url)
