import base64


def process_image(event, context):

    decoded_data = base64.b64decode(event['data']).decode('utf-8')
    print(f'Data: {decoded_data}')
    attributes = event['attributes']
    print(f'Attributes: {attributes}')
