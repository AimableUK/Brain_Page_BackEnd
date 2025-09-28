from django.db import models
import uuid

class Book(models.Model):
    title            = models.CharField(max_length=255)
    author           = models.CharField(max_length=255)
    isbn             = models.CharField(max_length=13, unique=True)
    published_date   = models.DateField()
    genre            = models.CharField(max_length=25)
    langauge         = models.CharField(max_length=50)
    description      = models.TextField()
    total_copies     = models.IntegerField()
    available_copies = models.IntegerField()
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title} by {self.author}'
    
    
class Student(models.Model):
    full_name      = models.CharField(max_length=255)
    email          = models.EmailField(blank=True, null=True, unique=True)
    phone          = models.CharField(max_length=15, blank=True, null=True, unique=True)
    student_number = models.CharField(max_length=20, unique=True)
    student_class  = models.CharField(max_length=255)
    address        = models.CharField(max_length=255)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.full_name} - {self.student_number}'
    
    
class User(models.Model):
    full_name  = models.CharField(max_length=255)
    email      = models.EmailField(blank=True, null=True, unique=True)
    phone      = models.CharField(max_length=15, unique=True)
    address    = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.full_name} - Phone: {self.phone}'
    
    
class Borrowing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrowings")
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, related_name="borrowings")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="borrowings")

    borrowed_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ("borrowed", "Borrowed"),
            ("returned", "Returned"),
            ("overdue", "Overdue"),
        ],
        default="borrowed",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        borrower = self.student.full_name if self.student else self.user.full_name if self.user else "Unknown"
        return f"{self.book.title} borrowed by {borrower}"
