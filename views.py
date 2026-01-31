from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import numpy as np
import joblib
import os
from .serializers import InsuranceSerializer

model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','Model','InsuranceCostPredictor.pkl')
model = joblib.load(model_path)

@api_view(['POST'])
def predict(request):
    if request.method == 'POST':
        serializer = InsuranceSerializer(data = request.data)
        if serializer.is_valid():
            input_data = tuple(serializer.validated_data.values())
            input_data_as_numpy_array = np.asarray(input_data)
            input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
            
            print(input_data_reshaped)

        prediction = model.predict(input_data_reshaped)

        return Response(prediction)

# @api_view(['GET','POST'])
# def predict(request):
#     serializer = InsuranceSerializer(data=request.data)
    
#     if serializer.is_valid():
#         input_data = tuple(serializer.validated_data.values())
#         input_data = np.asarray(input_data).reshape(1, -1)

#         prediction = model.predict(input_data)

#         return Response({
#             "prediction": float(prediction[0])
#         })

#     return Response(serializer.errors, status=400)


    
       

        

     


