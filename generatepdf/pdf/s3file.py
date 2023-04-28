import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOiIzMTFkMWZlOC1lZDQwLTQ2ZDYtODQ4Zi1kYjdkODIyNTliOTMiLCJyb2xlIjoiYWRtaW4iLCJkZXZpY2VUb2tlbiI6InN0cmluZyIsImRldmljZVR5cGUiOiJzdHJpbmciLCJuYmYiOjE2ODI1OTAyODksImV4cCI6MTg0MDQ0MzA4OSwiaWF0IjoxNjgyNTkwMjg5fQ.1nKkJAoyVd_2vo_vP-4Mn2kRBHhLnPIIDOI82WY_B0s"  #/API TOKEN/

# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwMzcyNTYwLCJqdGkiOiJlOWVjNzM2NDRlMGQ0OGZlYmI4MzY3YTZmZWMyY2JhOSIsInVzZXJfaWQiOjV9.IEQ4Skne9mtyGMuRcrZppmqUJd-JzJ5I1HgbqccACBM"

import boto3
def upload_file(image_path):
    url ="http://invoicesappapi-prod.us-east-2.elasticbeanstalk.com/api/Management/UploadPdfFile"
    # url = 'https://staging-api.vivifyhealthcare.com/ImageUpload/DocUpload/' #/use end point for s3 bucket upload/
    # url  = "http://127.0.0.1:8008/pdf/gen/"
    headers =  Imageheaders = {
        'Accept-Language': 'en-US',
        'Authorization': f'Bearer {token}'
    }
    import PyPDF2

    pdfFileObj = open(image_path, 'rb')
    # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    files = {'pdfFile': pdfFileObj}
    response = requests.post(url,files=files,headers=headers)
    print(response.status_code)
    imageurl = response
    for i in imageurl:
        print(i['data'])
    return imageurl
    

    
# image_path = r"D:\projects\New folder (2)\PDF-Generator-Python\generatepdf\Lifeeazy-HealthSummaryl.pdf"
# # image_path = r"D:\projects\New folder (2)\test.txt"
# upload_file(image_path=image_path)




# import boto3
# b_name = "ivin-pro-data-conversion"
# s3 = boto3.client("s3")
# b_res = s3.list_buckets()
# # for i in b_res['Buckets']:
#         # print(i)
# with open(r"C:\Users\anves\Pictures\as.png",'rb') as img:
#         s3.upload_fileobj(img,b_name,"testfile.jpg")
#
# s3.download_file(b_name,"testfile.jpg  ","download.jpg")

# def uploadfile(file):
#     s3 = boto3.client("s3")
#     with open(file,'rb') as f:
#         x=s3.upload_fileobj(f,"ivin-pro-data-conversion",file)
#         print(x)
#         return  x
    

def downloadfile(file):
    s3 = boto3.resource('s3')
    s3.Bucket('ivin-pro-data-conversion').download_file(file, file)
    return  "Success"


# import boto3
# s3 = boto3.resource('s3')
# s3.Bucket('ivin-pro-data-conversion').download_file('Madhutest.pdf', 'Madhutest.pdf')