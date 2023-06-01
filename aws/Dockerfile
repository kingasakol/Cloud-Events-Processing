# aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 021698728710.dkr.ecr.us-east-1.amazonaws.com
# in parent main dir: docker build -t lambda-repo -f aws/Dockerfile .
# docker push 021698728710.dkr.ecr.us-east-1.amazonaws.com/lambda-repo:latest

FROM public.ecr.aws/lambda/python:3.10

COPY aws/app.py aws/requirements.txt gcp/cloud_function_wrapper.py gcp/config.py gcp/pubsub-publish-key.json  ./

RUN python3.10 -m pip install -r requirements.txt -t .

CMD ["app.lambda_handler"]