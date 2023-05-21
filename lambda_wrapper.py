class Lambda_Wrapper:
    def __init__(self, lambda_client, iam_resource):
        self.lambda_client = lambda_client
        self.iam_resource = iam_resource

    def invoke_function(self, function_name, function_params, get_log):
        """
         Invokes a Lambda function.

         :param function_name: The name of the function to invoke.
         :param function_params: The parameters of the function as a dict. This dict
                                 is serialized to JSON before it is sent to Lambda.
         :param get_log: When true, the last 4 KB of the execution log are included in
                         the response.
         :return: The response from the function invocation.
         """
        try:
            response = self.lambda_client.invoke(
                FunctionName=function_name,
                Payload=json.dumps(function_params),
                LogType='Tail' if get_log else 'None')
            logger.info("Invoked function %s.", function_name)
        except ClientError:
            logger.exception("Couldn't invoke function %s.", function_name)
            raise
        return response

    # def get_iam_role(self, iam_role_name):
    #     """
    #     Get an AWS Identity and Access Management (IAM) role.
    #
    #     :param iam_role_name: The name of the role to retrieve.
    #     :return: The IAM role.
    #     """
    #     role = None
    #     try:
    #         temp_role = self.iam_resource.Role(iam_role_name)
    #         temp_role.load()
    #         role = temp_role
    #         logger.info("Got IAM role %s", role.name)
    #     except ClientError as err:
    #         if err.response['Error']['Code'] == 'NoSuchEntity':
    #             logger.info("IAM role %s does not exist.", iam_role_name)
    #         else:
    #             logger.error(
    #                 "Couldn't get IAM role %s. Here's why: %s: %s", iam_role_name,
    #                 err.response['Error']['Code'], err.response['Error']['Message'])
    #             raise
    #     return role
    #
    # def create_iam_role_for_lambda(self, iam_role_name):
    #     """
    #     Creates an IAM role that grants the Lambda function basic permissions. If a
    #     role with the specified name already exists, it is used for the demo.
    #
    #     :param iam_role_name: The name of the role to create.
    #     :return: The role and a value that indicates whether the role is newly created.
    #     """
    #     role = self.get_iam_role(iam_role_name)
    #     if role is not None:
    #         return role, False
    #
    #     lambda_assume_role_policy = {
    #         'Version': '2023-05-21',
    #         'Statement': [
    #             {
    #                 'Effect': 'Allow',
    #                 'Principal': {
    #                     'Service': 'lambda.amazonaws.com'
    #                 },
    #                 'Action': 'sts:AssumeRole'
    #             }
    #         ]
    #     }
    #     policy_arn = 'arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
    #
    #     try:
    #         role = self.iam_resource.create_role(
    #             RoleName=iam_role_name,
    #             AssumeRolePolicyDocument=json.dumps(lambda_assume_role_policy))
    #         logger.info("Created role %s.", role.name)
    #         role.attach_policy(PolicyArn=policy_arn)
    #         logger.info("Attached basic execution policy to role %s.", role.name)
    #     except ClientError as error:
    #         if error.response['Error']['Code'] == 'EntityAlreadyExists':
    #             role = self.iam_resource.Role(iam_role_name)
    #             logger.warning("The role %s already exists. Using it.", iam_role_name)
    #         else:
    #             logger.exception(
    #                 "Couldn't create role %s or attach policy %s.",
    #                 iam_role_name, policy_arn)
    #             raise
    #
    #     return role, True