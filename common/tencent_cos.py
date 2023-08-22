from os import environ
from qcloud_cos import CosConfig, CosS3Client


class TencentCOS:
    def __init__(self, cos_region, cos_secret_id, cos_secret_key, cos_bucket):
        config = CosConfig(Region=cos_region,
                           SecretId=cos_secret_id,
                           SecretKey=cos_secret_key,
                           Token=None,
                           Scheme="http",
                           EnableInternalDomain=False,
                           )
        self.client = CosS3Client(config, retry=5)
        self.bucket = cos_bucket

    def upload_file(self, local_file, cos_path):
        """上传文件到COS"""
        response = self.client.upload_file(
            Bucket=self.bucket,
            LocalFilePath=local_file,
            Key=cos_path,
            PartSize=5,
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


secret_id = environ.get('COS_SECRET_ID', None)
secret_key = environ.get('COS_SECRET_KEY', None)
region = environ.get('COS_REGION', None)
bucket = environ.get('COS_BUCKET', None)
tencent_cos_client = TencentCOS(cos_region=region, cos_secret_id=secret_id, cos_secret_key=secret_key, cos_bucket=bucket)