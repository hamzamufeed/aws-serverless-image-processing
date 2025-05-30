# Serverless Image Processing with S3 and Lambda

This project demonstrates how to automatically resize images uploaded to Amazon S3 using AWS Lambda.

## 🧩 Solution Overview

When an image is uploaded to the `original-images-hamzamufeed` S3 bucket, an AWS Lambda function is triggered that resizes the image to 300x300 pixels and saves it to the `processed-images` bucket.

## 🏗️ Architecture

[Architecture Diagram]

## ✅ AWS Services Used

- **Amazon S3**: Store original and processed images.
- **AWS Lambda**: Resize images using Pillow (Python).
- **IAM**: Define permissions for Lambda to access S3.
- **AWS SAM**: Infrastructure as Code (IaC) for deployment automation.

## 🧑‍💻 Technologies

- Python 3.9
- Pillow (image processing library)
- AWS SAM CLI

## 📦 Files Included

- `lambda_function.py`: Main Lambda handler
- `requirements.txt`: Pillow dependency
- `template.yaml`: AWS SAM template
- `README.md`: Project documentation

## 🚀 Deployment Steps

### 1. Prerequisites

- AWS Account
- [AWS CLI](https://aws.amazon.com/cli/ )
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html )

### 2. Folder Structure

serverless-image-resize/
│
├── template.yaml
└── image-resize/
├── lambda_function.py
└── requirements.txt


### 3. Build and Deploy

```bash
# Build the package
sam build

# Deploy the stack
sam deploy --guided

```

## 📝 Author

Hamza Barabrah  
LinkedIn: https://www.linkedin.com/in/hamza-barabrah/
Email: hamzamufeed@email.com