from github import Github
import json
import os
import boto3
import base64

def lambda_handler(event, context):
    """Lambda function wrapper
    Args:
        event: trigger event dict
        context: lambda methods and properties
    Returns:
        string: greeting response
    """
    print('Starting functions\n---------------------------------------------'

    if event["input"] == "Hello":

        return "World World World"

    else:

        raise

def main():
    """Main function
    Returns:
        string: greeting response
    """
    print('Starting main\n---------------------------------------------')

    return "Hello World"