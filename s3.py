import boto3

client = boto3.client(
    's3',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id='',
    aws_secret_access_key=''
)
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

data = open('test.txt', 'rb')
s3.Bucket('rajiv-test007-private').put_object(Key='test.txt', Body=data)
