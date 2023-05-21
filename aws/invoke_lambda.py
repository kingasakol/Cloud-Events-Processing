import boto3
from lambda_wrapper import Lambda_Wrapper

lambda_client = boto3.client('lambda')

wrapper = Lambda_Wrapper(lambda_client)
wrapper.invoke_function("processImage", "dupa", False)