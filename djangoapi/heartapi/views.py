from rest_framework.response import Response
from rest_framework import generics
from .models import PredResults
from . serializers import PredSerializer
import pandas as pd

class PostsView(generics.ListAPIView):
    
    def get(self, request, *args, **kwargs):

        #For variable significance, check the dataset repo
        A = float(self.request.GET.get('A'))
        B = float(self.request.GET.get('B'))
        C = float(self.request.GET.get('C'))
        D = float(self.request.GET.get('D'))
        E = float(self.request.GET.get('E'))
        F = float(self.request.GET.get('F'))
        G = float(self.request.GET.get('G'))
        H = float(self.request.GET.get('H'))
        I = float(self.request.GET.get('I'))
        J = float(self.request.GET.get('J'))
        K = float(self.request.GET.get('K'))
        L = float(self.request.GET.get('L'))
        M = float(self.request.GET.get('M'))

        model = pd.read_pickle(r"/home/omen/Desktop/DjangoProjects/Heart/Heart-Disease-Predictor/ML/new_model.pickle")
        result = model.predict(
            [[A, B, C, D, E, F, G, H, I, J, K, L, M]])
            
        Y = result[0]

        serializer = PredSerializer(data=self.request.GET)
        if serializer.is_valid():
            serializer.save()
            return Response(result[0])

        return Response(serializer.errors, status=400)
