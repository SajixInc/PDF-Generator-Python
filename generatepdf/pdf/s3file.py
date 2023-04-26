import requests
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4OTc4NzY0LCJqdGkiOiJhMWU5ZWE2ODU4Mzc0OWE3YjNiZDFlNjcxN2Q4MDhkNyIsInVzZXJfaWQiOjV9.O9Yyi4lTU8r40pqf8fyjzDLJNbR8S0yUrbRqF0Ww2Mc"

def upload_file(image_path):
    url = 'https://staging-api.vivifyhealthcare.com/ImageUpload/DocUpload/'
    # url  = "http://127.0.0.1:8008/pdf/gen/"
    headers =  Imageheaders = {
        'Accept-Language': 'en-US',
        'Authorization': f'Bearer {token}'
    }
    import PyPDF2

    pdfFileObj = open(image_path, 'rb')
    # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    files = {'UploadDoc': pdfFileObj}
    response = requests.post(url,files=files,headers=headers)
    print(response.status_code)
    imageurl = response.json()['Result']
   
    doc = (imageurl.items())
    for i in doc:
        url = (i[1])
        return url

    
# image_path = r"D:\projects\New folder (2)\PDF-Generator-Python\generatepdf\Lifeeazy-HealthSummaryl.pdf"
# # image_path = r"D:\projects\New folder (2)\test.txt"
# upload_file(image_path=image_path)




import boto3
b_name = "ivin-pro-data-conversion"
s3 = boto3.client("s3")
b_res = s3.list_buckets()
# for i in b_res['Buckets']:
        # print(i)
with open(r"C:\Users\anves\Pictures\as.png",'rb') as img:
        s3.upload_fileobj(img,b_name,"testfile.jpg")
#
# s3.download_file(b_name,"testfile.jpg  ","download.jpg")