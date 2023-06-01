import boto3
import sys
import base64

from aws.lambda_wrapper import Lambda_Wrapper


def file_to_base64(file_path):
    try:
        with open(file_path, "rb") as file:
            contents = file.read()
            base64_data = base64.b64encode(contents)
            return base64_data.decode('utf-8')
    except IOError:
        print("Error: Unable to open the file.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_client.py <file_path>")
    else:
        file_path = sys.argv[1]
        base64_data = file_to_base64(file_path)
        if base64_data:
            lambda_client = boto3.client('lambda')

            wrapper = Lambda_Wrapper(lambda_client)
            wrapper.invoke_function("processImage", { "payload": base64_data }, False)