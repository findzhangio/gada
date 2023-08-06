from os import environ
from qcloud_cos import CosConfig, CosS3Client


class TencentCOS:
    def __init__(self, cos_region, cos_secret_id, cos_secret_key, cos_bucket):
        config = CosConfig(Region=cos_region, SecretId=cos_secret_id, SecretKey=cos_secret_key, Token=None, Scheme="http")
        self.client = CosS3Client(config)
        self.bucket = cos_bucket

    def upload_file(self, local_file, cos_path):
        """上传文件到COS"""
        response = self.client.upload_file(
            Bucket=self.bucket,
            LocalFilePath=local_file,
            Key=cos_path
        )
        return response

    def download_file(self, cos_path, local_path):
        """从COS下载文件"""
        response = self.client.get_object(
            Bucket=self.bucket,
            Key=cos_path
        )
        response['Body'].get_stream_to_file(local_path)

    def delete_file(self, cos_path):
        """删除COS上的文件"""
        response = self.client.delete_object(
            Bucket=self.bucket,
            Key=cos_path
        )
        return response


secret_id = environ.get('COS_SECRET_ID', "AKIDgCXfaGjxUo24yhEXaP1QcZ7SaZLtEMFt")
secret_key = environ.get('COS_SECRET_KEY', "d2LeppiRu9vgLq8C2dz8qKckjW5RaWGm")
region = environ.get('COS_REGION', 'ap-hongkong')
bucket = environ.get('COS_BUCKET', 'image-1255602134')
tencent_cos_image = TencentCOS(cos_region=region, cos_secret_id=secret_id, cos_secret_key=secret_key, cos_bucket=bucket)