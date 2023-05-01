import requests
# url ="http://invoicesappapi-prod.us-east-2.elasticbeanstalk.com/api/Management/UploadPdfFile"
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySUQiOiIzMTFkMWZlOC1lZDQwLTQ2ZDYtODQ4Zi1kYjdkODIyNTliOTMiLCJyb2xlIjoiYWRtaW4iLCJkZXZpY2VUb2tlbiI6InN0cmluZyIsImRldmljZVR5cGUiOiJzdHJpbmciLCJuYmYiOjE2ODI1OTAyODksImV4cCI6MTg0MDQ0MzA4OSwiaWF0IjoxNjgyNTkwMjg5fQ.1nKkJAoyVd_2vo_vP-4Mn2kRBHhLnPIIDOI82WY_B0s"  #/API TOKEN/
url = 'https://staging-api.vivifyhealthcare.com/ImageUpload/DocUpload/' #/use end point for s3 bucket upload/
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwMzcyNTYwLCJqdGkiOiJlOWVjNzM2NDRlMGQ0OGZlYmI4MzY3YTZmZWMyY2JhOSIsInVzZXJfaWQiOjV9.IEQ4Skne9mtyGMuRcrZppmqUJd-JzJ5I1HgbqccACBM"

headers ={
        
        'Authorization': f'Bearer {token}'
    }
data = r'/home/vivify/PDF-Generator-Python/generatepdf/generatepdf/result.html'
dt ={
    "UploadDoc":data
}
x= requests.post(url=url, headers=headers,files=data)
print(x.status_code)
print(x)