import cv2
import numpy as np
import pytesseract
import os
import datetime
import base64

# C:\Program Files\Tesseract-OCR\tesseract.exe
# poppler_path=r'D:\downloads\poppler-0.68.0_x86\poppler-0.68.0\bin'
poppler_path=r'D:\downloads\poppler-0.68.0_x86\poppler-0.68.0\bin'
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\madhu\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

                       # Mongodb
from pymongo import MongoClient

# output_file = r'D:\projects\pytesseract\images'  ## give images folder path
output_file = r'D:\downloads\img'
folder_path = r'D:\downloads\pdf' ## give pdf's folder path
# creation of MongoClient
client = MongoClient()
he = []
import urllib.parse

Username = 'devops_admin'
Password = 'Devops1234'
username = urllib.parse.quote_plus(Username)
password = urllib.parse.quote_plus(Password)
# Connect with the portnumber and host
client = MongoClient('mongodb://localhost:27017/')
# client = MongoClient('mongodb://%s:%s@13.234.70.44:27017' % (username,password))

# Access database
mydatabase = client['Data_conversion']

# Access collection of the database
mycollection = mydatabase['test']
mycollection2 = mydatabase['testimage']
myimage = mydatabase['test2']

# dictionary to be added in the database
rec = {
    'title': 'MongoDB and Python',
    'description': 'MongoDB is no SQL database',
    'tags': ['mongodb', 'database', 'NoSQL'],
    'viewers': 104
}


# Time kosam

dt = datetime.datetime.now()
print(dt)
lis = ["",""]

count = 0
def imgetobase(file):
    global count
    f =f"sample{count}.png"
    import boto3
    b_name = "ivin-pro-data-conversion"
    s3 = boto3.client("s3")
    b_res = s3.list_buckets()
    # for i in b_res['Buckets']:
    #         print(i)
    
    cv2.imshow('Resized', file)
    img = cv2.imwrite(f, file)
    cv2.waitKey(3)
    count=1+count
    with open(f,'rb') as img:
            # s3.upload_fileobj(img,b_name,f)
    return f

# def pagetobase(image):
#     image = open(image, 'rb')
#     image_read = image.read()
#     image_64_encode = base64.encodebytes(image_read) #encodestring also works aswell as decodestring
#     # print('This is the image in base64: ' + str(image_64_encode))
#     return str(image_64_encode)



def page(image):
    text = pytesseract.pytesseract.image_to_string(image)
    # print(text)
    text.replace('Photo', "")
    # print(text)
    f = open('text.txt', 'w')
    f.write(text + "\n")
    f.close()
    fi = open('text.txt', 'r')
    x = fi.readlines()
    for i in x:
        if "Assembly" in i:
            lis.append(i)
        elif "Section" in i:
            lis.append(i)
    fi.close()
# print(lis)



c = 1
def covert(x, y, w, h, im2, img_file):
    # print(h)
    # try:
    width = int(w / 3)
    if h >= 400 and h < 1000:
        # print(h,w)
        width = int(w / 3)
        # print(width,'--------')
        f = open('test.txt', 'a')
        rect = cv2.rectangle(im2, (x, y), (x + width, y + h), (0, 255, 0), 5)

        if x == 0 and y == 0:
            pass
        else:
            cropped = im2[y:y + h, x:x + width]

            # print(cropped)
            # print(w, '----------')
            img = cv2.resize(rect, (1020, 750))
            cv2.imshow('d', cropped)
            cv2.waitKey(3)
            # count=count+1
        

            b = imgetobase(cropped)
            text = pytesseract.image_to_string(cropped)
            f = open('text.txt', 'a')
            f.write(text)
            f.close()
            # cv2.destroyAllWindows()
            # print('data base error')
            
            rec =mycollection2.insert_one({

                'Voter_file_tracker': img_file,
                "Voter_Image": b,})
            rec = mycollection.insert_one({
                                            'Voter_file_tracker': img_file,
                                            "votere_slip":b,
                                           "Assembly Name": lis[0],
                                           "Section": lis[1],
                                           'details': text,
                                           'Created on': dt})

# except:
#     print('convert function exception')
def covert2(x, y, w, h, im2, img_file):
    if h >= 400 and h < 1000 and w > 400:
        # print(h,w)
        width2 = int(w / 3)
        # print(width,'--------')

        f = open('test.txt', 'a')
        rect = cv2.rectangle(im2, (x, y), (x + width2, y + h), (0, 255, 255), 3)
        # print(h,width)
        if x == 0 and y == 0:
            pass
        else:
            cropped = im2[y:y + h, x:x + width2]
            b = imgetobase(cropped)
            # print(w,'----------')
            img = cv2.resize(rect, (1020, 750))
            cv2.imshow('d', cropped)
            cv2.waitKey(3)
            # cv2.destroyWindow()
            text = pytesseract.image_to_string(cropped)
            f = open('text.txt', 'a')
            f.write(text)
            f.close()
            # cv2.destroyAllWindows()
            # if len(lis)>1:

        

            rec = mycollection2.insert_one({
                'Voter_file_tracker': img_file,
                "Voter_Image": b, })
            rec = mycollection.insert_one({
                                           'Voter_file_tracker': img_file,
                                            "votere_slip":b,
                                           "Assembly Name": lis[0],
                                           "Section": lis[1],
                                           'details': text,
                                           'Created on': dt})


def covert3(x, y, w, h, im2, img_file):
    if h >= 400 and h < 1000 and w > 400:
        # print(h,w)
        width1 = int(w / 3)
        # print(width,'--------')
        f = open('test.txt', 'a')
        rect = cv2.rectangle(im2, (x, y), (x + width1, y + h), (255, 255, 255), 3)
        # print(h,width)
        if x == 0 and y == 0:
            pass
        else:
            cropped = im2[y:y + h, x:x + width1]
           
            # #print(w,'----------')
            img = cv2.resize(rect, (1020, 750))
            cv2.imshow('d', cropped)
            cv2.waitKey(3)
            cv2.imwrite("cropped.png", im2)
            b = imgetobase(cropped)
            # cv2.destroyWindow()
            text = pytesseract.image_to_string(cropped)
            f = open('text.txt', 'a')
            f.write(text)
            f.close()

         

            rec = mycollection2.insert_one({
                'Voter_file_tracker': img_file,
                "Voter_Image": b, })
            rec = mycollection.insert_one({
                                           'Voter_file_tracker': img_file,
                                            "votere_slip":b,
                                           "Assembly Name": lis[0],
                                           "Section": lis[1],
                                           'details': text,
                                           'Created on': dt})



def ima(x, y, w, h, im2, img_file):
    
    # #print(x,y)
    im2 = cv2.imread(im2)
    cv2.putText(im2, 'Rectangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    # rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 5)
    # img = cv2.resize(rect, (1020, 750))
    # cv2.imshow('d', img)
    #print(x, y)
    covert(x, y, w, h, im2, img_file)
    W = int(w / 3)
    covert(x + W, y, w, h, im2, img_file)
    covert(x + W + W, y, w, h, im2, img_file)



area = []
value = []


# def img_detect(img_path, img_file):
#     lis.clear()
    # page(img_path)
#     
def img_detect(img_path, img_file):
    
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 50, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)
    for cnt in contours:
        x1, y1 = cnt[0][0]
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(cnt)

            ratio = float(w) / h
            if ratio >= 0.9 and ratio <= 1.1:
                pass
            else:
                area.append((h * w))
                value.append((h, w, x, y))
                he.append(h)
    for i in range(len(area)):
        # if value[i][1]>=0 and value[i][1]>100:
        xa = value[i][2]
        ya = value[i][3]
        l = value[i][0]
        w = value[i][1]
        # cv2.rectangle(img, (xa, ya), (xa + w, ya + l), (0, 255, 0), 2)
        ima(x=xa, y=ya, w=w, h=l, im2=img_path, img_file=img_file)


import os


def image_upload(image_file):
    print("count of images :",len(os.listdir(folder_path)))
    l = os.listdir(image_file)
    path = image_file
    for k in range(len(l)):
        print(k, 'started')
        area.clear()
        value.clear()
        he.clear()
        img_detect(img_path=f"{path}\{l[k]}", img_file=l[k])
        # os.remove(f"{path}\{l[k]}")
        print(k, 'done')


def converting_pdftoimg(pdf_path):
    from pdf2image import convert_from_path
    # print(pdf_path)
    images = convert_from_path(pdf_path, 500, poppler_path=poppler_path)
    name = pdf_path.split("\\")
    print(name)
    for i, image in enumerate(images):
        print(i, 'is pdf converting into images')
        fname = f'{name[-1]}' + str(i) + '.png'
        # print(fname)
        image.save(f"{output_file}\{fname}", "PNG")



l = os.listdir(folder_path)
print(l)
# for i in range(len(l)):
#    print(l[i])
#    converting_pdftoimg(pdf_path=f'{folder_path}\{l[i]}')
# yesy()
    
image_upload(f'{output_file}')


# dt  = datetime.datetime.now()