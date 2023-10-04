import json
import sagemaker
import base64
from sagemaker.serializers import IdentitySerializer

# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2023-10-04-12-01-09-219'

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])

    # Instantiate a Predictor
    predictor = sagemaker.Predictor(ENDPOINT)

    # For this model the IdentitySerializer needs to be "image/png"
    predictor.serializer = IdentitySerializer("image/png")
    
    # Make a prediction:
    inferences = predictor.predict(image, initial_args={'ContentType': 'image/png'})

    # We return the data back to the Step Function    
    event['body']["inferences"] = inferences.decode('utf-8')
    return {
        'statusCode': 200,
        'body': event['body']
    }

