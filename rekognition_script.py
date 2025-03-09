import boto3
from PIL import Image
import io

def convert_webp_to_jpeg(image_name, bucket_name):
    s3_client = boto3.client('s3', region_name='eu-west-2')
    # Télécharger l'image depuis S3
    s3_object = s3_client.get_object(Bucket=bucket_name, Key=image_name)
    image_data = s3_object['Body'].read()

    # Ouvrir l'image avec Pillow
    image = Image.open(io.BytesIO(image_data))

    # Vérifier si c'est une image webp
    if image.format == 'WEBP':
        # Convertir l'image en JPEG
        jpeg_image = io.BytesIO()
        image.convert('RGB').save(jpeg_image, 'JPEG')
        jpeg_image.seek(0)  # Rewind pour pouvoir le lire à partir du début
        return jpeg_image
    return io.BytesIO(image_data)  # Si déjà en format valide (comme PNG ou JPEG), retourne l'image sans conversion

def analyze_image(bucket_name, image_name):
    rekognition_client = boto3.client('rekognition', region_name='eu-west-2')

    # Convertir l'image au format JPEG si c'est un fichier webp
    image_data = convert_webp_to_jpeg(image_name, bucket_name)

    # Appel à l'API de Rekognition pour détecter les labels
    response = rekognition_client.detect_labels(
        Image={'Bytes': image_data.read()},
        MaxLabels=10,
        MinConfidence=70
    )

    print(f"Résultats pour {image_name}:")
    for label in response['Labels']:
        print(f"Label: {label['Name']}, Confiance: {label['Confidence']}%")

def analyze_all_images(bucket_name):
    s3_client = boto3.client('s3', region_name='eu-west-2')

    response = s3_client.list_objects_v2(Bucket=bucket_name)

    if 'Contents' in response:
        for obj in response['Contents']:
            image_name = obj['Key']
            print(f"Analyse de l'image : {image_name}")
            analyze_image(bucket_name, image_name)
    else:
        print("Aucune image trouvée dans le bucket.")

bucket_name = 'my-first-bucket-rekognition'
analyze_all_images(bucket_name)
