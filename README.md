# Build-a-ML-Workflow-For-Scones-Unlimited-On-Amazon-SageMaker
## Project Overview

- Image Classifiers are used in the field of computer vision to identify the content of an image and it is used across a broad variety of industries, from advanced technologies like autonomous vehicles and augmented reality, to eCommerce platforms, and even in diagnostic medicine.

- You are hired as a Machine Learning Engineer for a scone-delivery-focused logistics company, Scones Unlimited, and you’re working to ship an Image Classification model. The image classification model can help the team in a variety of ways in their operating environment: detecting people and vehicles in video feeds from roadways, better support routing for their engagement on social media, detecting defects in their scones, and many more!

- In this project, you'll be building an image classification model that can automatically detect which kind of vehicle delivery drivers have, in order to route them to the correct loading bay and orders. Assigning delivery professionals who have a bicycle to nearby orders and giving motorcyclists orders that are farther can help Scones Unlimited optimize their operations.

- As an MLE, your goal is to ship a scalable and safe model. Once your model becomes available to other teams on-demand, it’s important that your model can scale to meet demand, and that safeguards are in place to monitor and control for drift or degraded performance.

- In this project, you’ll use AWS Sagemaker to build an image classification model that can tell bicycles apart from motorcycles. You'll deploy your model, use AWS Lambda functions to build supporting services, and AWS Step Functions to compose your model and services into an event-driven application. At the end of this project, you will have created a portfolio-ready demo that showcases your ability to build and compose scalable, ML-enabled, AWS applications.
  
## Project Steps Overview
   - Step 1: Data staging
   - Step 2: Model training and deployment
   - Step 3: Lambdas and step function workflow
      - You're going to write and deploy three Lambda functions, and then use the Step Functions visual editor to chain them together!
      - The first lambda function is responsible for data generation. The second one is responsible for image classification. And the third function is responsible for filtering out low-confidence inferences.
   - Step 4: Testing and evaluation
   - Step 5: Optional challenge
   - Step 6: Cleanup cloud resources
## Project Environment
- Sagemaker Studio
   - Click through the AWS console to Amazon Sagemaker.
   - Click through the main Sagemaker page to Amazon Sagemaker Studio from the left hand toolbar.
   - If a user does not exist already in the Sagemaker Studio Control Panel, Add user.
   - Select an execution role that has full Sagemaker Access, otherwise you can create a new role.
   - Create a role and proceed with creating the user.
- Lambda Functions
   - You need the Lambda service to complete the project. At this point, you should have already created and deployed a few lambda functions at this point.
   - In case you want to test it again:
      - Proceed to open up the AWS console from the AWS Gateway.
      - Click through the AWS console to Amazon Lambda.
      - Click to create a lambda function.
      - Test the lambda function is working
- Step Function Visual Editor
   - You should have access to the step function visual editor. If you want to double-check:
     - Proceed to open up the AWS console from the AWS Gateway.
     - Click through the AWS console to Step Function.
     - Click to create a state machine.
     - Choose to design your workflow visually
     - Create a simple Step function
