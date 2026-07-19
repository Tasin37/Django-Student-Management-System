from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class timestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Department(timestampedModel):
    name = models.CharField(max_length=50)
    building = models.CharField(max_length=100)
    mission = models.TextField()
    established_on = models.DateField()

    def __str__(self):
        return self.name
    
class Teacher(timestampedModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ManyToManyField(Department, related_name='teachers')

    def __str__(self):
        return self.name
    

class Student(timestampedModel):
    name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name
    
class Result(timestampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    subject_code = models.CharField(max_length=10)
    marks = models.FloatField(validators=[MinValueValidator(0,message="Marks must be 0 or higher"), MaxValueValidator(100,message="Marks must be 100 or lower")])

    class Meta:
        unique_together = ('student', 'subject_code')

    def __str__(self):
        return f"{self.student.name}_{self.subject_code}"
    
class DepartmentHead(timestampedModel):
    department = models.OneToOneField(Department, on_delete=models.CASCADE, related_name='head')
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, related_name='head_of_department')

