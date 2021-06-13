from django.shortcuts import render
import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
import numpy as np

@api_view(['GET'])
def index(request):
    return_data = {
        'error': 0,
        'message': 'Success',
    }
    return Response(return_data)

@api_view(['POST'])
def predict(request):
    try:
        image = request.data.get('image',None)
        fields = [image]
        if not None in fields:
            # model_path = 'ml_model/model.pkl'
            # my_model = pickle.load(open(model_path, 'rb'))
            # prediction = my_model.predict([result])[0]
            # conf_score = np.max(my_model.predict_proba([result]))*100
            predictions = {
                'error': '0',
                'message': 'Success',
                # 'prediction': prediction,
                # 'confidence_score': conf_score
            }

        else:
            predictions = {
                'error': '1',
                'message': 'Invalid Parameters'
            }
    except Exception as e:
        predictions = {
            'error': '2',
            'message': str(e)
        }
    return Response(predictions)