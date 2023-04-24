# url = 'https://staging-api.vivifyhealthcare.com/ImageUpload/DocUpload/'
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4OTc4NzY0LCJqdGkiOiJhMWU5ZWE2ODU4Mzc0OWE3YjNiZDFlNjcxN2Q4MDhkNyIsInVzZXJfaWQiOjV9.O9Yyi4lTU8r40pqf8fyjzDLJNbR8S0yUrbRqF0Ww2Mc"
import requests
url  = "http://127.0.0.1:8008/pdf/gen/"
headers =  Imageheaders = {
'Accept-Language': 'en-US',
'Authorization': f'Bearer {token}'
}
import PyPDF2

pdfFileObj = open(r"D:\projects\New folder (2)\PDF-Generator-Python\generatepdf\generatepdf\result.html", 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
files = {'UploadDoc': pdfFileObj}
response = requests.post(url,files=files,    )
print(response.status_code)