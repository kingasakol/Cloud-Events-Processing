from botocore.exceptions import ClientError
import json
import logging


logger = logging.getLogger(__name__)

class Lambda_Wrapper:
    def __init__(self, lambda_client):
        self.lambda_client = lambda_client

    def invoke_function(self, function_name, function_params, get_log):
        try:
            response = self.lambda_client.invoke(
                FunctionName=function_name,
                Payload=json.dumps(function_params),
                LogType='None')
            logger.info("Invoked function %s.", function_name)
        except ClientError:
            logger.exception("Couldn't invoke function %s.", function_name)
            raise
        return response
