from rest_framework.views import APIView
from rest_framework import status
from eva.serializers import UserSerializer, UserInfoSerializer, ChangePasswordSerializer, FileSerializer, UserRecordSerializer
from eva.models import UserRecord
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response


class UserRegister(APIView):
    """
    Creates the user.
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            json = serializer.data
            json['status'] = status.HTTP_201_CREATED
            json['token'] = token.key
            if user:
                return Response(json, status=status.HTTP_201_CREATED)
        else:
            json = serializer.errors
            json['status'] = status.HTTP_400_BAD_REQUEST
            return Response(json, status=status.HTTP_400_BAD_REQUEST)


class UserManage(APIView):
    """
    get: user information
    post: modify user information
    """

    permission_classes = [permissions.IsAuthenticated]


    def get(self, request, format='json'):
        user = request.user
        serializer = UserInfoSerializer(user)
        json = serializer.data
        json['status'] = status.HTTP_200_OK
        return Response(json, status=status.HTTP_200_OK)

    def post(self, request, format='json'):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not user.check_password(serializer.data.get("old_password")):
                return Response({
                    "message": "invalid old password",
                    "status": status.HTTP_400_BAD_REQUEST
                }, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hash the password to the db
            user.set_password(serializer.data.get("new_password"))
            user.save()
            response = {
                'status': status.HTTP_200_OK,
                'message': 'Password updated successfully',
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileUpload(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRecordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format='json'):
        records = UserRecord.objects.filter(userId=request.user)
        serializer = UserRecordSerializer(records, many=True)
        json = {
            'records': serializer.data,
            'status': status.HTTP_200_OK,
        }
        return Response(json, status=status.HTTP_200_OK)
