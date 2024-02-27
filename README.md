# Entelligentsia

## Prerequisites
Before proceeding with this project, ensure the following prerequisites are met:

Python 3 Installation: Python 3 should be installed on your system. You can download and install Python from the official Python website.

AWS Account Setup: You need an AWS account to utilize AWS services such as DynamoDB and AWS Lambda functions. If you don't have an AWS account, you can sign up for one here.

Serverless Framework Installation: Serverless framework should be installed and configured with your AWS account. You can install it via npm:

````bash
npm install -g serverless
````

After installation, configure your AWS credentials using serverless config credentials.

DynamoDB Tables Setup: Set up the necessary DynamoDB tables as required by the project. Ensure they are properly configured according to the schema defined in the project.

Postman Installation: Postman is a popular API testing tool. You can download and install it from the official Postman website. This will allow you to test the APIs developed in this project.

## Overview
This project is a demonstration of a Python-based application utilizing AWS services such as DynamoDB, AWS Lambda functions, JWT authentication, and Serverless framework. The project consists of several APIs designed to showcase different functionalities.

## Setup
To set up the project locally, follow these steps:

Clone the repository from GitHub:

````bash
https://github.com/SiddhantDembi/Entelligentsia.git
````

Install dependencies:

````bash
cd project_name
pip install -r requirements.txt
````

Set up AWS credentials and configure the AWS CLI if you haven't already.

Configure your AWS DynamoDB tables according to the schema defined in the project.

## Deploy
````bash
cd project_directory
serverless deploy
````
