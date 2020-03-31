from rest_framework.views import APIView
from rest_framework import status
from eva.serializers import WorkSerializer, PageSerializer, WordSerializer, RadicalSerializer
from eva.models import Work, Page, Word, Radical
from rest_framework.response import Response
from django.http import Http404


class WorkView(APIView):
    def get(self, request, format=None):
        """return all works"""
        works = Work.objects.all()
        print(works)
        serializer = WorkSerializer(works, many=True)
        json = {
            'works': serializer.data,
            'count': works.count(),
            'status': status.HTTP_200_OK,
        }
        return Response(json)


class WorkDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Work.objects.get(pk=pk)
        except Work.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        work = self.get_object(pk)
        serializer = WorkSerializer(work)
        json = serializer.data
        json['status'] = status.HTTP_200_OK
        return Response(json)


class PageView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        """return all works"""
        try:
            workId = request.query_params.get("workId")

            if workId is None:
                pages = Page.objects.all()
                workId = 0
                stats = status.HTTP_200_OK
            else:
                pages = Page.objects.filter(workId=workId)
                if pages.count() == 0:
                    stats = status.HTTP_404_NOT_FOUND
                else:
                    stats = status.HTTP_200_OK
        except ValueError:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'invalid pageId',
            })

        serializer = PageSerializer(pages, many=True)

        json = {
            'pages': serializer.data,
            'count': pages.count(),
            'workId': workId,
            'status': stats,
        }
        return Response(json)


class PageDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Page.objects.get(pk=pk)
        except Page.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        work = self.get_object(pk)
        serializer = PageSerializer(work)
        json = serializer.data
        json['status'] = status.HTTP_200_OK
        return Response(json)


class WordView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        """return all works"""
        pageId = request.query_params.get("pageId")
        try:
            if pageId is None:
                words = Word.objects.all()
                pageId = 0
                stats = status.HTTP_200_OK
            else:
                words = Word.objects.filter(pageId=pageId)
                if words.count() == 0:
                    stats = status.HTTP_404_NOT_FOUND
                else:
                    stats = status.HTTP_200_OK
        except ValueError:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'invalid pageId',
            })
        serializer = WordSerializer(words, many=True)

        json = {
            'words': serializer.data,
            'count': words.count(),
            'pageId': pageId,
            'status': stats,
        }
        return Response(json)


class WordDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Word.objects.get(pk=pk)
        except Word.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        word = self.get_object(pk)
        serializer = WordSerializer(word)
        json = serializer.data
        json['status'] = status.HTTP_200_OK
        return Response(json)


class RadicalView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        """return all works"""
        wordId = request.query_params.get("wordId")
        try:
            if wordId is None:
                radicals = Radical.objects.all()
                wordId = 0
                stats = status.HTTP_200_OK
            else:
                radicals = Radical.objects.filter(wordId=wordId)
                if radicals.count() == 0:
                    stats = status.HTTP_404_NOT_FOUND
                else:
                    stats = status.HTTP_200_OK
        except ValueError:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'invalid pageId',
            })
        serializer = RadicalSerializer(radicals, many=True)

        json = {
            'words': serializer.data,
            'count': radicals.count(),
            'wordId': wordId,
            'status': stats,
        }
        return Response(json)


class RadicalDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Radical.objects.get(pk=pk)
        except Word.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        radical = self.get_object(pk)
        serializer = RadicalSerializer(radical)
        json = serializer.data
        json['status'] = status.HTTP_200_OK
        return Response(json)

