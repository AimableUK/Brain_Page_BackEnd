from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BookSerializer, MemberSerializer, LendSerializer, ReturnBookSerializer
from .models import Book, Member, Lend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.utils.timezone import now


class Books(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['author']
    

class BookDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'pk'
    

class Members(ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        total_members = Member.objects.count()
        members_with_books = (
            Lend.objects.filter(status=False)
            .values('member')
            .distinct()
            .count()
        )
        members_overdue = (
            Lend.objects.filter(status=False, return_date__lt=now().date())
            .values('member')
            .distinct()
            .count()
        )
        start_of_month = now().replace(day=1)
        new_members = Member.objects.filter(created_at__gte=start_of_month).count()

        return Response({
            "members": serializer.data,
            "stats": {
                "total_members": total_members,
                "members_with_books": members_with_books,
                "members_overdue": members_overdue,
                "new_members": new_members,
            }
        }, status=status.HTTP_200_OK)
    
    
class MemberDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    lookup_field = 'pk'
    
    
class Lends(ListCreateAPIView):
    serializer_class = LendSerializer
    queryset = Lend.objects.all()
    filter_backends = [OrderingFilter, SearchFilter]
    filterset_fields = ['member', 'book']
    search_fields = ['member', 'book']
    
    
class LendDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = LendSerializer
    queryset = Lend.objects.all()
    lookup_field = 'pk'
    
    
class ReturnBook(APIView):
    def post(self, request, pk):
        try:
            lend = Lend.objects.get(pk=pk)
        except Lend.DoesNotExist:
            return Response({"detail": "Lend not found."}, status=status.HTTP_404_NOT_FOUND)

        if lend.status:
            return Response({"detail": "Book already returned."}, status=status.HTTP_400_BAD_REQUEST)

        lend.status = True
        lend.returned_at = timezone.now()
        lend.save()
        
        book = lend.book
        if book.available_copies is None:
            book.available_copies = 0
        book.available_copies += 1
        
        available = book.available_copies or 0
        if available > 0:
            book.status = True
    
        book.save()

        serializer = ReturnBookSerializer(lend)
        return Response(serializer.data, status=status.HTTP_200_OK)   
        
        