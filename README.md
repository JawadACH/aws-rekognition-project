# AWS Rekognition Image Labelling Project

This project utilizes Amazon Rekognition, a powerful service provided by AWS, to analyze and label images stored in an S3 bucket. The project processes multiple images and extracts meaningful labels (such as objects, scenes, and activities) based on AWS Rekognition's capabilities.

## Features:
- Image analysis using AWS Rekognition to detect labels in images.
- Batch processing of multiple images stored in an S3 bucket.
- Identification of objects, people, animals, scenes, and more.

## Prerequisites:
Before you begin, ensure that you have the following:
- AWS Account with Rekognition and S3 services enabled.
- AWS CLI installed and configured on your local machine.
- Python 3.x installed along with the `boto3` library.

## Setup:

1. Clone this repository:
   git clone https://github.com/yourusername/aws-rekognition-image-labelling.git
2. Install dependencies:
  pip install boto3 pillow
3. Configure AWS CLI:
    _Run the command:
   aws configure
    _Provide your AWS Access Key ID, Secret Access Key, region (e.g., eu-west-2), and output format.
4. Ensure your images are uploaded to an S3 bucket
   _Run the Python script to analyze all images in your specified S3 bucket:
  python rekognition_script.py
