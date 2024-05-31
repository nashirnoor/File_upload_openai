from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
import openai
import chardet
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UploadedFile
from .serializers import UploadedFileSerializer


class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = UploadedFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

openai.api_key = settings.OPENAI_API_KEY


@api_view(['POST'])
def chat_query(request):
    query = request.data.get('query', '')
    if not query:
        return Response({'error': 'Query is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        uploaded_files = UploadedFile.objects.all()
        file_content = ''
        for uploaded_file in uploaded_files:
            with uploaded_file.file.open('rb') as file:
                raw_data = file.read()
                result = chardet.detect(raw_data)
                encoding = result['encoding']
                if encoding is None:
                    encoding = 'utf-8' 
                file_content += raw_data.decode(encoding) + '\n'

        prompt = file_content + query

        response = openai.Completion.create(
            model="davinci-002",  
            prompt=prompt,
            max_tokens=150
        )

        return Response({'response': response.choices[0].text.strip()}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)