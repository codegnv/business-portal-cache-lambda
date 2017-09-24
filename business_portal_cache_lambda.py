import logging
import os
import urllib.request
from os.path import join

import boto3

# Map from `filename to cache as` -> `location of file`
URLS_TO_CACHE = {
    'business_types.json': 'https://data.cityofgainesville.org/resource/i9px-haju.json',
    'business_permits.json': 'https://data.cityofgainesville.org/resource/mfe4-6q3g.json'
}

BUCKET = os.environ['S3_BUCKET']
PREFIX = os.environ['S3_PREFIX']


def lambda_handler(event, context):
    main()


def main():
    setup_logging()

    for filename, url in URLS_TO_CACHE.items():
        cache_file(filename, url)


def setup_logging():
    logging.getLogger('botocore').setLevel(logging.WARNING)
    logging.getLogger().setLevel(logging.INFO)


def cache_file(filename, url):
    data = get_bytes(url)
    logging.info('Downloaded {}'.format(url))

    s3_path = save_bytes_to_s3(data, filename)
    logging.info('Uploaded {} to {}'.format(url, s3_path))

    return s3_path


def get_bytes(url):
    with urllib.request.urlopen(url) as resp:
        data = resp.read()
    return data


def save_bytes_to_s3(data, filename):
    key = join(PREFIX, filename)
    bucket = boto3.resource('s3').Bucket(BUCKET)
    bucket.put_object(Key=key, Body=data)
    s3_path = 's3://{}/{}'.format(BUCKET, key)
    return s3_path


if __name__ == '__main__':
    main()
