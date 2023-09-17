from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BlogPost
from .serializers import CreateBlogSerializer, BlogPostSerializer

@api_view(['POST', 'GET'])
def create_blog_post(request):
    if request.method == 'POST':
        serializer = CreateBlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
