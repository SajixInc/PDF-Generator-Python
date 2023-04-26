import boto3
from botocore.exceptions import NoCredentialsError

# locations = "Asia Pacific ap-south-1"
ACCESS_KEY = '*****'  #replace * with your s3 bucket access key#
SECRET_KEY = '*****'  #replace * with your s3 bucket secret key#

import logging
import boto3
from botocore.exceptions import ClientError
import os


import logging
import boto3
from botocore.exceptions import ClientError
import os



import boto3
import os


def upload_files(path):
    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name='ap-southeast-1'
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket('')

    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                bucket.put_object(Key=full_path[len(path) + 1:], Body=data)


if __name__ == "__main__":
    d = upload_files(r'D:\projects\New folder (2)\PDF-Generator-Python\generatepdf\Madhutest.pdf')
    print(d)

