from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Album, Artist, Tracks
from .serializers import ArtistSerializer, AlbumSerializer, TracksSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
class LandingPageApiView(APIView):
    def get(self, request):
        return Response(data={"get api": 'Landing Page'})

    def post(self, request):
        return Response(data={"post api": ' This is post request'})



class ArtistDetailApiView(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumDetailApiView(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer



class TrackDetailApiView(ModelViewSet):
    queryset = Tracks.objects.all()
    serializer_class = TracksSerializer