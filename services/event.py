import uuid
from config import Settings
from boto3 import client


# Faz o upload para o bucket da s3
def s3_image_upload(file):
    s3 = client('s3', aws_access_key_id=Settings().AWS_ACCESS_KEY_ID,
                aws_secret_access_key=Settings().AWS_SECRET_ACCESS_KEY)

    uuid_code = str(uuid.uuid4())
    filename = f'tuning_meets/{uuid_code}-{file.filename.strip()}'
    s3.upload_fileobj(file.file, Settings().AWS_BUCKET_NAME, filename)
    url = f"{Settings().AWS_S3_CUSTOM_DOMAIN}/{filename}"
    return url
