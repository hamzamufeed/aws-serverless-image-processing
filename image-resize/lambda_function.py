from PIL import Image
import boto3
import io
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get bucket and object key from event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Only process image files
    if not object_key.lower().endswith(('.png', '.jpg', '.jpeg')):
        print("Not an image file.")
        return

    # Download image from S3
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    image_data = response['Body'].read()

    # Open image
    image = Image.open(io.BytesIO(image_data))

    # Resize image to 300x300
    resized_image = image.resize((300, 300))

    # Save resized image to BytesIO
    buffer = io.BytesIO()
    resized_image.save(buffer, format=image.format)
    
    # Upload to processed-images bucket
    output_bucket = 'processed-images-hamzamufeed'
    s3.put_object(
        Bucket=output_bucket,
        Key=f"resized-{object_key}",
        Body=buffer.getvalue()
    )

    print(f"Image {object_key} resized and saved to {output_bucket}")