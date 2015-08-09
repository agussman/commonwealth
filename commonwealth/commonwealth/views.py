from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from .models import Business
from .serializers import BusinessSerializer
from rest_framework import status

class BusinessViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Businesses to be viewed.
    """
    queryset = Business.objects.all().order_by('coin_score')
    serializer_class = BusinessSerializer

    @detail_route()
    def retrieve_by_yelp_id(self, request, pk=None):
        """
        API endpoint that returns a Business by its yelp id.
        """
        queryset = Business.objects.get(yelp_id=pk)
        serializer = BusinessSerializer(queryset)
        return Response(serializer.data)

    @detail_route(methods=['put'])
    def update_by_yelp_id(self, request, pk=None):
        queryset = Business.objects.get(yelp_id=pk)
        print(repr(request.data))
        print(queryset.yelp_id)
        serializer = BusinessSerializer(queryset, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
