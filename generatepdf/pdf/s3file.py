import requests

import boto3
def upload_file(image_path,url,token):  
    try: 
        url = url
        headers =  Imageheaders = {
            'Accept-Language': 'en-US',
            'Authorization': token,
        }
        import PyPDF2
        print(url)

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
    except Exception:
        return "please check your api "

    
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