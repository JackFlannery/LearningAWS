import boto3
import uuid

client = boto3.client('stepfunctions')

def lambda_handler(event, context):
	transactionId = str(uuid.uuid1())

	response = client.start_execution(
		stateMachineArn='arn:aws:states:us-east-2:724746613050:stateMachine:LambdaChainTest',
		name=transactionId,
		)
