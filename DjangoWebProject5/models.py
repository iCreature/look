"""
Definition of models.
"""

from django.db import models

#lecture informaton
class admin_info(models.Model):
    id = models.AutoField(primary_key=True)
    fname= models.CharField(max_length=50)
    surname= models.CharField(max_length=50)
    email= models.CharField(max_length=255)
    lecture_id= models.CharField(max_length=255)
    title= models.CharField(max_length=50)
    ad_type= models.CharField(max_length=50)
    password= models.CharField(max_length=255)
    def __str__(self):
        return self.email

#student information
class student_info(models.Model):
    id = models.AutoField(primary_key=True)
    fname= models.CharField(max_length=50,null=True)
    surname= models.CharField(max_length=50,null=True)
    email= models.CharField(max_length=255,null=True)
    course= models.CharField(max_length=255,null=True)
    year= models.CharField(max_length=255,null=True)
    course_id=models.CharField(max_length=255,null=True)
    student_no= models.CharField(max_length=255,null=True)
    #face_image= models.BinaryField(upload_to='media/',null=True,verbose_name="")
    password= models.CharField(max_length=255,null=True)
    type= models.CharField(max_length=255,null=True)
    status= models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.student_no

#exams and test questions
class test_info(models.Model):
    id = models.AutoField(primary_key=True)
    module= models.CharField(max_length=50,null=True)
    course_id=models.CharField(max_length=50,null=True)
    type = models.CharField(max_length=50,null=True)
    test_id = models.CharField(max_length=50,null=True)
    examiner=models.CharField(max_length=255,null=True)
    date=models.DateField(null=True)
    mark_tot=models.CharField(max_length=50,null=True)
    time= models.TimeField(null=True)
    duration=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.test_id
#exams/test
class exams(models.Model):
    id = models.AutoField(primary_key=True)
    test_id= models.CharField(max_length=50,null=True)
    question = models.CharField(max_length=255,null=True)
   
    #mark= models.CharField(max_length=50 ,null=True)
    
    def __str__(self):
        return self.test_id
     

#submitted exams or test
class submitted(models.Model):
    id = models.AutoField(primary_key=True)   
    student_no=models.CharField(max_length=255,null=True)
    date = models.DateField(auto_now_add=True,null=True)
    time = models.TimeField(auto_now=True,null=True)
    paper=models.FileField(upload_to='submitted/pdfs',null=True)

    def __str__(self):
        return self.student_no

class courses(models.Model):
    id = models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=255)
    course_id=models.CharField(max_length=255)
    year=models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.course_id


class subject_list(models.Model):
    id = models.AutoField(primary_key=True)
    course_id=models.CharField(max_length=255)
    module=models.CharField(max_length=255)   
    def __str__(self):
        return self.course_id


