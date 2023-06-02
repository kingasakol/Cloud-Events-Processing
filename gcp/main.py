import base64
import zipfile
import io
import requests
import boto3

def compress_image_to_zip(image_data):
    # Tworzenie archiwum ZIP w pamięci
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zipf:
        # Dodawanie obrazka do archiwum
        zipf.writestr('compressed_image.jpg', image_data)

    # Pobranie zawartości archiwum ZIP z bufora
    zip_data = zip_buffer.getvalue()
    return zip_data

def send_zip_via_post(zip_data, url):
    # Ustawienie nagłówka z informacją o typie zawartości
    headers = {'Content-Type': 'application/zip'}

    # Wysłanie zapytania POST z archiwum ZIP
    response = requests.post(url, data=zip_data, headers=headers)

    # Sprawdzenie odpowiedzi
    if response.status_code == 200:
        print("Archiwum ZIP zostało pomyślnie wysłane.")
    else:
        print("Wystąpił błąd podczas wysyłania archiwum ZIP.")


def upload_file_to_s3(file, bucket_name, aws_access_key_id, aws_secret_access_key):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    try:
        s3.upload_fileobj(file, bucket_name, "image.zip")
        print(f"Plik {file_name} został wysłany na Amazon S3 do kubełka {bucket_name}.")
    except Exception as e:
        print(f"Wystąpił błąd podczas wysyłania pliku: {str(e)}")

def process_image(event, context):
    # Pobranie zakodowanego obrazka z pola 'data' w evencie
    image_base64 = event['data']
    # Dekodowanie obrazka z base64
    image_data = base64.b64decode(image_base64)

    aws_access_key_id=ASIAQKDKYKMDJZW7FVHB
    aws_secret_access_key=dy0QAYdxEdRwvN4ij5frxeL+dkjsbQSDWMzmMcjW

    # Kompresowanie obrazka do archiwum ZIP
    zip_data = compress_image_to_zip(image_data)

    # Wysyłanie archiwum ZIP za pomocą AWS SDK
    upload_file_to_s3(zip_data,"bucket",aws_access_key_id,aws_secret_access_key)
