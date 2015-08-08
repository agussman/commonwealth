from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from .models import Business
from .serializers import BusinessSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Businesses to be viewed.
    """
    queryset = Business.objects.all().order_by('overall_score')
    serializer_class = BusinessSerializer

    @detail_route()
    def retrieve_by_yelp_id(self, request, pk=None):
        """
        API endpoint that returns a Business by its yelp id.
        """
        queryset = Business.objects.get(yelp_id=pk)
        serializer = BusinessSerializer(queryset)
        return Response(serializer.data)
