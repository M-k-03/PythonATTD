# file:features/steps/awsS3Step.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
# from hamcrest import assert_that, equal_to
from blender import Blender


@when('Download files from S3')
def step_when_switch_blender_on(context):
    # context.blender.downloadfile_to_s3()
    print("Downloaded Files from S3")


@when('Upload files to S3')
def step_when_switch_blender_on(context):
    # context.blender.uploadfile_to_s3()
    print("Uploaded Files to S3")

@when('Bucket is Created')
def step_when_switch_blender_on(context):
    # context.blender.createbucket_in_s3()
    print("Bucket Created")