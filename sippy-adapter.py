from fastapi import FastAPI
from datetime import datetime, timedelta
import boto3
import os

app = FastAPI()

# Configure AWS credentials and S3 client
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
bucket_name = 'your-s3-bucket-name'

# Store the timestamp of the last check
last_check_timestamp = datetime.now()

@app.on_event("startup")
async def check_s3_bucket():
    # Run the check_s3_bucket function every minute
    while True:
        await check_s3_bucket()
        await asyncio.sleep(60)

async def check_s3_bucket():
    global last_check_timestamp

    # Get the list of objects in the S3 bucket
    response = s3.list_objects_v2(Bucket=bucket_name)

    # Filter the objects based on the last check timestamp
    new_objects = [obj['Key'] for obj in response.get('Contents', []) if obj['LastModified'] > last_check_timestamp]

    # Update the last check timestamp
    last_check_timestamp = datetime.now()

    # Print the new objects on the console
    if new_objects:
        print(f"New objects found in S3 bucket {bucket_name}:")
        for obj in new_objects:
            print(obj)
    else:
        print("No new objects found in S3 bucket.")

@app.get("/")
async def root():
    return {"message": "S3 bucket monitoring application"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)