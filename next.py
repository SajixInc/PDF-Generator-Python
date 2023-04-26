import boto3

s3 = boto3.client('s3')
# with open(r"D:\projects\New folder (2)\PDF-Generator-Python\sample3.png","rb") as img:
s3.upload_file(r"D:\projects\New folder (2)\PDF-Generator-Python\sample3.png","ivin-pro-data-conversion","sample3.png")