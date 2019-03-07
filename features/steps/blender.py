# file:features/steps/blender.py
# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------
import boto3
class Blender(object):

    s3_client = boto3.client('s3')
    def __init__(self):
        print('...Initialize...')

    @classmethod
    def uploadfile_to_s3(self):
        s3 = boto3.resource('s3')
        s3.meta.client.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')

    def downloadfile_to_s3(self):
        s3 = boto3.resource('s3')
        s3.meta.client.download_file('BucketName', 'hello.txt', '/tmp/hello.txt')

    def createbucket_in_s3(self):
        s3_client = boto3.client('s3')
        response = s3_client.create_bucket(ACL = 'public-read-write',Bucket = "MyBucketName",CreateBucketConfiguration = {'LocationConstraint': 'EU'},ObjectLockEnabledForBucket = False)
        print(response)
