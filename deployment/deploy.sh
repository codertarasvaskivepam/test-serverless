#!/bin/bash

action=$1
if [[ $action = "update" ]];then

aws cloudformation update-stack --stack-name codebuild-serverless \
    --capabilities CAPABILITY_IAM \
    --template-body file://template.yml \
    --parameters ParameterKey=githubtoken,ParameterValue=$githubtoken ParameterKey=stackName,ParameterValue=test_serverless

else

aws cloudformation create-stack --stack-name codebuild-serverless \
    --capabilities CAPABILITY_IAM \
    --template-body file://template.yml \
    --parameters ParameterKey=githubtoken,ParameterValue=$githubtoken ParameterKey=stackName,ParameterValue=test_serverless
fi;
