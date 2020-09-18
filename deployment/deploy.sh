#!/bin/bash

# env=$3
aws cloudformation create-stack --stack-name test-serverless \
    --capabilities CAPABILITY_IAM \
    --template-body file://template.yml \
    --parameters ParameterKey=githubtoken,ParameterValue=$githubtoken
