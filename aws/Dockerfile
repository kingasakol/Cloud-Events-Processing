FROM public.ecr.aws/lambda/python:3.10

COPY aws/app.py aws/requirements.txt gcp/cloud_function_wrapper.py gcp/config.py gcp/pubsub-publish-key.json  ./

RUN python3.10 -m pip install -r requirements.txt -t .

CMD ["app.lambda_handler"]