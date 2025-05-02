import boto3

url = 'http://commoncrawl.org/the-data/get-started/'
key = 'crawl-data/CC-MAIN-2022-05/wet.paths.gz'
bucket_name = 'commoncrawl'

def main():
    # your code here
    s3_client = boto3.client('s3')

    bucket = s3_client.get_object(Bucket = bucket_name, Key=key)

    for obj in bucket.objects.all():
        print(obj.key)



if __name__ == "__main__":
    main()
