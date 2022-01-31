from colorsys import ONE_THIRD
from email import charset
from numbers import Integral
import re
from runpy import _ModifiedArgv0
from sqlite3 import Timestamp
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class RunningYear(models.Model):
    academic_year=models.IntegerField()
    description=models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.code}: {self.name}'


class School(models.Model):
    code=models.CharField(max_length=50)
    name=models.CharField(max_length=120)
    head=models.CharField(max_length=100)
    head_number=models.CharField(max_length=80)
    owner_name=models.CharField(max_length=100)
    owner_contact=models.CharField(max_length=80)
    logo=models.CharField(max_length=50,null=True,blank=True)
    address=models.CharField(max_length=250,blank=True,null=True)

    def __str__(self):
        return f'{self.code}: {self.name}'

class AccountRole(models.Model):
    type=models.CharField(max_length=50)
    permissions=models.IntegerField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.type} {self.permissions}'

class AcademicSettings(models.Model):
    type=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.type} {self.description}'

class AcademicYear(models.Model):
    running_year=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    status=models.IntegerField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.running_year}: {self.description}'

class BillingCategory(models.Model):
    code=models.CharField(max_length=50)
    name=models.CharField(max_length=150)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}, {self.code}: {self.name}'

class Admin(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=80)
    phone=models.CharField(max_length=40,blank=True,null=True)
    address=models.CharField(max_length=150,blank=True,null=True)
    owner_status=models.IntegerField()
    username=models.CharField(max_length=50)
    status=models.IntegerField()
    birthday=models.DateField()
    authentication_key=models.CharField(max_length=80)
    gender=models.CharField(max_length=20,choices=(('Male','Male'),('Female','Female')))    
    idcard=models.CharField(max_length=50,blank=True,null=True)
    profession=models.CharField(max_length=50)
    since=models.DateField()
    p_create=models.IntegerField()
    p_edit=models.IntegerField()
    p_view=models.IntegerField()
    p_delete=models.IntegerField()
    userid=models.ForeignKey(User,on_delete=models.CASCADE,related_name='admins')
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}, {self.first_name} {self.last_name}'

class Dormitory(models.Model):
    name=models.CharField(max_length=50)
    number=models.IntegerField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school} {self.name} {self.number}'

class Teacher(models.Model):
    title=models.CharField(max_length=50)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=50)
    address=models.CharField(max_length=250)
    birthday=models.DateField()
    phone=models.CharField(max_length=80)
    email=models.EmailField()
    password=models.CharField(max_length=12)
    idcard=models.CharField(max_length=100)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.CharField(max_length=150)
    date=models.DateField()
    userid=models.ForeignKey(User,on_delete=models.CASCADE,related_name='teachers')
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.school} {self.title}: {self.first_name} {self.last_name}'

class Parent(models.Model):
    title=models.CharField(max_length=50,blank=True,null=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(blank=True,null=True)
    password=models.CharField(max_length=30)
    phone=models.CharField(max_length=40,blank=True,null=True)
    address=models.CharField(max_length=250,blank=True,null=True)
    profession=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    gender=models.CharField(max_length=50,choices=(('Male','Male'),('Female','Female')),blank=True,null=True)
    business=models.CharField(max_length=250,blank=True,null=True)
    idcard=models.CharField(max_length=50,null=True,blank=True)
    business_phone=models.CharField(max_length=40,blank=True,null=True)
    home_phone=models.CharField(max_length=40,blank=True,null=True)
    image=models.CharField(max_length=150,blank=True,null=True)
    date=models.DateField(auto_now_add=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE,related_name='parents')
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.title} {self.first_name} {self.last_name} {self.address}'

class Level(models.Model):
    name=models.CharField(max_length=50)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.name}'

class ClassGroup(models.Model):
    name=models.CharField(max_length=50)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school} {self.name}'

class Classes(models.Model):
    name=models.CharField(max_length=50)
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE,blank=True,null=True)
    gid=models.ForeignKey(ClassGroup,on_delete=models.CASCADE,related_name='gid')
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.name}'

class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    birthday=models.DateField()
    gender=models.CharField(max_length=10,choices=(('Male','Male'),('Female','Female')))
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=40,blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    password=models.CharField(max_length=30)
    parent_id=models.ForeignKey(Parent,on_delete=models.CASCADE)
    dormitory_id=models.ForeignKey(Dormitory,on_delete=models.CASCADE)
    transport_id=models.BooleanField(blank=True,null=True)
    student_session=models.IntegerField()
    username=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    board=models.IntegerField()
    solvencia=models.IntegerField()
    classes_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    image=models.CharField(max_length=120,null=True,blank=True)
    diseases=models.CharField(max_length=250,null=True,blank=True)
    allergies=models.CharField(max_length=250,null=True,blank=True)
    doctor=models.CharField(max_length=100,null=True,blank=True)
    doctor_phone=models.CharField(max_length=40,blank=True,null=True)
    authorized_person=models.CharField(max_length=100,blank=True,null=True)
    authorized_phone=models.CharField(max_length=40,null=True,blank=True)
    note=models.CharField(max_length=200,null=True,blank=True)
    year=models.IntegerField(null=True,blank=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE,related_name='students')
    school=models.ForeignKey(School,on_delete=models.CASCADE)

class Section(models.Model):
    name=models.CharField(max_length=150)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.name} {self.class_id} {self.teacher_id}'

class Ticket(models.Model):
    title=models.CharField(max_length=150)
    code=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    priority=models.CharField(max_length=50)
    description=models.CharField(max_length=150)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    assigned_staff_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='teacher')
    timestamp=models.DateTimeField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school} {self.title}: {self.code} {self.description}'

class TicketMessage(models.Model):
    ticket_code=models.CharField(max_length=50)
    message=models.CharField(max_length=250)
    file=models.CharField(max_length=150)
    sender_type=models.CharField(max_length=50)
    sender_id=models.CharField(max_length=50)
    timestamp=models.DateTimeField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school} {self.ticket_code}: {self.message}'

class TeacherAttendance(models.Model):
    timestamp=models.DateTimeField()
    year=models.IntegerField()
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    status=models.CharField(max_length=50,null=True,blank=True)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school} {self.timestamp}: {self.year} {self.teacher_id}'

class Subject(models.Model):
    name=models.CharField(max_length=50)
    classes_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    year=models.IntegerField()
    la1=models.CharField(max_length=100,blank=True,null=True)
    la2=models.CharField(max_length=100,blank=True,null=True)
    la3=models.CharField(max_length=100,blank=True,null=True)
    la4=models.CharField(max_length=100,blank=True,null=True)
    la5=models.CharField(max_length=100,blank=True,null=True)
    la6=models.CharField(max_length=100,blank=True,null=True)
    la7=models.CharField(max_length=100,blank=True,null=True)
    la8=models.CharField(max_length=100,blank=True,null=True)
    la9=models.CharField(max_length=100,blank=True,null=True)
    la10=models.CharField(max_length=100,blank=True,null=True)
    type=models.CharField(max_length=50,null=True,blank=True)
    section_id=models.ForeignKey(Section,on_delete=models.CASCADE)
    color=models.CharField(max_length=50)
    icon=models.CharField(max_length=50,blank=True,null=True)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.name} {self.teacher} {self.classes_id}'

class StudentRequest(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    parent_id=models.ForeignKey(Parent,on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    status=models.CharField(max_length=50)
    description=models.CharField(max_length=150)
    title=models.CharField(max_length=100)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.student_id} {self.parent_id} {self.description}'

class settings(models.Model):
    type=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.type} {self.description}'

class Exam(models.Model):
    name=models.CharField(max_length=50)
    start=models.DateTimeField()
    end=models.DateTimeField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.name}'

class OnlineExam(models.Model):
    code=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    section_id=models.ForeignKey(Section,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
    exam_date=models.DateField()
    time_start=models.TimeField()
    time_end=models.TimeField()
    duration=models.DecimalField(decimal_places=2,max_digits=8)
    minimum_percentage=models.DecimalField(decimal_places=2,max_digits=8)
    instruction=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    running_year=models.IntegerField()
    wall_type=models.CharField(max_length=50)
    publish_date=models.DateTimeField()
    uploader_type=models.CharField(max_length=50)
    uploader_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    upload_date=models.DateField()
    password=models.CharField(max_length=30)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.title} {self.status} {self.uploader_id}'

class Reports(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    user_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=150)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    section_id=models.ForeignKey(Section,on_delete=models.CASCADE)
    priority=models.CharField(max_length=100)
    file=models.CharField(max_length=200)
    status=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    code=models.CharField(max_length=50)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.title} {self.class_id} {self.description}'

class Response(models.Model):
    message=models.CharField(max_length=250)
    date=models.DateField(auto_now_add=True)
    report_code=models.ForeignKey(Reports,on_delete=models.CASCADE)
    sender_type=models.CharField(max_length=50)
    sender_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.message} {self.date} {self.sender_id}'

class Remarks(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    exam_id=models.ForeignKey(Exam,on_delete=models.CASCADE)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    section_id=models.ForeignKey(Section,on_delete=models.CASCADE)
    year=models.IntegerField()
    comment=models.CharField(max_length=250,blank=True,null=True)
    creation=models.DateTimeField(auto_now_add=True)
    user_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    user_type=models.CharField(max_length=50)
    modified=models.CharField(max_length=50,blank=True,null=True)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.exam_id} {self.class_id} {self.section_id} {self.comment}'

class QuestionPaper(models.Model):
    title=models.CharField(max_length=50)
    question_paper=models.CharField(max_length=250)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    exam_id=models.ForeignKey(Exam,on_delete=models.CASCADE)
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.question_paper} {self.class_id} {self.teacher_id}'

class QuestionBank(models.Model):
    online_exam_id=models.ForeignKey(OnlineExam,on_delete=models.CASCADE)
    question_title=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    number_of_options=models.IntegerField()
    options=models.CharField(max_length=250)
    correct_answers=models.CharField(max_length=250)
    mark=models.DecimalField(decimal_places=2,max_digits=8)
    image=models.CharField(max_length=150,blank=True,null=True)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school} {self.online_exam_id}: {self.question_title} {self.type} {self.mark}'

class Polls(models.Model):
    question=models.CharField(max_length=250)
    options=models.CharField(max_length=250)
    date=models.DateField()
    user=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    poll_code=models.CharField(max_length=50)
    satus=models.CharField(max_length=50)
    date2=models.DateField()
    type=models.CharField(max_length=50)
    pulished_date=models.DateField()
    admin_id=models.ForeignKey(User,on_delete=models.CASCADE)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.question} {self.pulished_date} {self.user}'

class PollResponse(models.Model):
    poll_code=models.ForeignKey(Polls,on_delete=models.CASCADE)
    answer=models.CharField(max_length=250)
    date=models.DateField()
    user=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    date2=models.DateField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.answer} {self.date} {self.user}'

class PendingUsers(models.Model):
    user_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    email=models.EmailField(blank=True,null=True)
    phone=models.CharField(max_length=40)
    birthday=models.DateField()
    password=models.CharField(max_length=30)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    section_id=models.ForeignKey(Section,on_delete=models.CASCADE)
    profession=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    parent_id=models.ForeignKey(Parent,on_delete=models.CASCADE)
    type=models.CharField(max_length=50)
    roll=models.CharField(max_length=50)
    date=models.DateField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.first_name} {self.last_name} {self.class_id} {self.class_id}'

class OnlineUsers(models.Model):
    session=models.CharField(max_length=200)
    time=models.TimeField()
    id_usuario=models.IntegerField()
    type=models.CharField(max_length=100)
    gp=models.CharField(max_length=100)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.time} {self.id_usuario} {self.type}'
    
class Notification(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    user_type=models.CharField(max_length=50)
    date=models.DateField()
    time=models.TimeField()
    status=models.IntegerField()
    notify=models.CharField(max_length=50)
    original_id=models.IntegerField()
    original_type=models.CharField(max_length=50)
    url=models.CharField(max_length=250)
    type=models.CharField(max_length=50)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
    year=models.IntegerField()
    section_id=models.ForeignKey(Section,on_delete=models.CASCADE)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.user_type} {self.status} {self.url}'

class OnlineExamResult(models.Model):
    online_exam_id=models.ForeignKey(OnlineExam,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    answer_script=models.CharField(max_length=100)
    obtained_mark=models.DecimalField(decimal_places=2,max_digits=8)
    status=models.CharField(max_length=50)
    exam_started_time=models.DateTimeField()
    result=models.CharField(max_length=250,blank=True,null=True)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.answer_script} {self.obtained_mark} {self.status}'

class NoticeMessage(models.Model):
    message=models.CharField(max_length=250)
    date=models.DateField()
    user_type=models.CharField(max_length=50)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    message_file_name=models.CharField(max_length=50)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.message} {self.user_type} {self.user_id}'

class News(models.Model):
    code=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    date=models.DateField()
    type=models.CharField(max_length=50)
    date2=models.DateField()
    publish_date=models.DateTimeField()
    admin_id=models.ForeignKey(User,on_delete=models.CASCADE)
    embed=models.CharField(max_length=50,null=True,blank=True)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.code} {self.description} {self.admin_id}'

class MessageThread(models.Model):
    code=models.CharField(max_length=50)
    sender=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='sender')
    reciever=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='thread_reciever')
    last_message_timestamp=models.DateTimeField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.code} {self.description} {self.admin_id}'

class Message(models.Model):
    message_thread_code=models.CharField(max_length=50)
    message=models.CharField(max_length=250)
    sender=models.ForeignKey(Student,on_delete=models.CASCADE)
    timestamp=models.DateTimeField()
    read_status=models.IntegerField()
    file_name=models.CharField(max_length=100)
    reciever=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='reciever')
    file_type=models.CharField(max_length=50)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.message} {self.sender} {self.reciever}'

class Mark(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    section_id=models.ForeignKey(Section,on_delete=models.CASCADE)
    exam_id=models.ForeignKey(Exam,on_delete=models.CASCADE)
    mark_obtained=models.DecimalField(decimal_places=2,max_digits=8)
    mark_total=models.DecimalField(decimal_places=2,max_digits=8)
    comment=models.CharField(max_length=100,blank=True,null=True)
    year=models.IntegerField()
    labone=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    labdtwo=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    labthree=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    labfour=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    labfive=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    labsix=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    labseven=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    labeight=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    labnine=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    labten=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    labtotal=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    final=models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.student_id} {self.mark_obtained} {self.mark_total}'

class Live(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    date=models.DateField()
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    section_id=models.ForeignKey(Section,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
    time=models.TimeField()
    user_type=models.CharField(max_length=50)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    year=models.IntegerField()
    publish_date=models.DateTimeField()
    upload_date=models.DateTimeField()
    room=models.CharField(max_length=50)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.user_id} {self.user_type} {self.description}'

class Librarian(models.Model):
    first_name=models.CharField(max_length=80,null=True,blank=True)
    middle_name=models.CharField(max_length=80,null=True,blank=True)
    last_name=models.CharField(max_length=80,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    password=models.CharField(max_length=40)
    phone=models.CharField(max_length=40,null=True,blank=True)
    address=models.CharField(max_length=250,blank=True,null=True)
    username=models.CharField(max_length=50)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=20,choices=(('Male','Male'),('Female','Female')))
    idcard=models.CharField(max_length=100,null=True,blank=True)
    since=models.DateField()
    birthday=models.DateField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.user_id} {self.first_name} {self.middle_name} {self.last_name}'

class Language(models.Model):
    phrase=models.CharField(max_length=100)
    english=models.CharField(max_length=100,blank=True,null=True)
    portuguese=models.CharField(max_length=100,blank=True,null=True)
    hindi=models.CharField(max_length=100,null=True,blank=True)
    french=models.CharField(max_length=100,null=True,blank=True)
    serbian=models.CharField(max_length=100,null=True,blank=True)
    arabic=models.CharField(max_length=100,null=True,blank=True)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.phrase} {self.english} {self.french} {self.portuguese}'

class HomeWork(models.Model):
    code=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=50,blank=True,null=True)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
    uploader_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='uploader')
    time_end=models.TimeField()
    section_id=models.ForeignKey(Section,on_delete=models.CASCADE)
    uploader_type=models.CharField(max_length=50)
    file_name=models.CharField(max_length=100,blank=True,null=True)
    date_end=models.DateField()
    type=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.IntegerField()
    year=models.CharField(max_length=50)
    wall_type=models.CharField(max_length=50)
    publish_date=models.DateTimeField()
    upload_date=models.DateTimeField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.title} {self.description} {self.class_id} {self.file_name}'

class GroupMessageThread(models.Model):
    code=models.CharField(max_length=50)
    members=models.CharField(max_length=250)
    name=models.CharField(max_length=50)
    last_message_timestamp=models.DateTimeField()
    created_timestamp=models.DateTimeField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.members} {self.name} {self.last_message_timestamp} {self.created_timestamp}'

class GroupMessage(models.Model):
    message_thread_code=models.CharField(max_length=50)
    sender=models.CharField(max_length=50)
    message=models.CharField(max_length=250)
    timestamp=models.DateTimeField()
    read_status=models.IntegerField()
    attached_file_name=models.CharField(max_length=50)
    file_type=models.CharField(max_length=50)
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.school}: {self.message} {self.sender}'

class Grade(models.Model):
    name=models.CharField(max_length=50)
    grade_point=models.CharField(max_length=5)
    mark_from=models.DecimalField(decimal_places=2,max_digits=8)
    mark_upto=models.DecimalField(decimal_places=2,max_digits=8)
    numerical=models.BooleanField()
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.grade_point} {self.mark_from} {self.mark_upto} {self.class_id}'

class ForumMessage(models.Model):
    message=models.CharField(max_length=250)
    date=models.DateTimeField()
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    user_type=models.CharField(max_length=50)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.message} {self.post_id} {self.date} {self.user_type}'

class Forum(models.Model):
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    timestamp=models.DateTimeField()
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50,blank=True,null=True)
    post_code=models.CharField(max_length=50)
    file_name=models.CharField(max_length=50,blank=True,null=True)
    section_id=models.ForeignKey(Section,on_delete=models.CASCADE)
    post_status=models.IntegerField()
    type=models.CharField(max_length=50)
    wall_type=models.CharField(max_length=50)
    publish_date=models.DateTimeField()
    upload_date=models.DateTimeField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.teacher_id} {self.subject_id} {self.class_id} {self.description}'

class Folder(models.Model):
    name=models.CharField(max_length=50)
    user_type=models.CharField(max_length=50)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField()
    token=models.CharField(max_length=150)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.name} {self.user_type} {self.user_id} {self.date}'

class File(models.Model):
    name=models.CharField(max_length=50)
    size=models.CharField(max_length=50)
    date=models.DateTimeField()
    user_type=models.CharField(max_length=50)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    folder_token=models.CharField(max_length=50,blank=True,null=True)
    fileorder=models.DateField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.name} {self.user_type} {self.user_id} {self.date}'



class ExpenseCategory(models.Model):
    name=models.CharField(max_length=100)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.name}'

class Events(models.Model):
    title=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    start=models.DateTimeField()
    end=models.DateTimeField()
    type=models.CharField(max_length=50)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school} {self.title}'

class Enroll(models.Model):
    enroll_code=models.CharField(max_length=50)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    section_id=models.ForeignKey(Section,on_delete=models.CASCADE)
    roll=models.CharField(max_length=50)
    date_added=models.DateField()
    year=models.IntegerField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school} {self.student_id} {self.student_id} {self.class_id} {self.section_id}'


class Document(models.Model):
    title=models.CharField(max_length=50,blank=True,null=True)
    description=models.CharField(max_length=100,blank=True,null=True)
    file_name=models.CharField(max_length=100)
    file_type=models.CharField(max_length=50)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    timestamp=models.DateTimeField()
    subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
    type=models.CharField(max_length=50)
    year=models.IntegerField()
    filesize=models.CharField(max_length=50)
    wall_type=models.CharField(max_length=50)
    publish_date=models.DateTimeField()
    upload_date=models.DateTimeField()
    section_id=models.ForeignKey(Section,on_delete=models.CASCADE)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school} {self.title} {self.description}'

class Deliveries(models.Model):
    homework_code=models.CharField(max_length=50)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    date=models.DateTimeField()
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    section_id=models.ForeignKey(Section,on_delete=models.CASCADE)
    file_name=models.CharField(max_length=100)
    student_comment=models.CharField(max_length=250)
    teacher_comment=models.CharField(max_length=250)
    subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
    status=models.IntegerField()
    homework_reply=models.CharField(max_length=50,blank=True,null=True)
    mark=models.DecimalField(decimal_places=2,max_digits=8)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school} {self.homework_code} {self.student_id} {self.subject_id}'

class ClassRoutine(models.Model):
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    section_id=models.ForeignKey(Section,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
    time_start=models.TimeField()
    time_end=models.TimeField()
    time_start_min=models.TimeField()
    time_end_min=models.TimeField()
    day=models.CharField(max_length=50,choices=(('Monday','Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thursday','Thursday'),('Friday','Friday'),('Saturday','Saturday'),('Sunday','Sunday')))
    year=models.IntegerField()
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    amend=models.CharField(max_length=50,choices=(('AM','AM'),('PM','PM')))
    amstart=models.CharField(max_length=50,choices=(('AM','AM'),('PM','PM')))
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school} {self.class_id} {self.section_id} {self.time_start} {self.time_end}'

class Book(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=150)
    author=models.CharField(max_length=150)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    status=models.IntegerField()
    type=models.CharField(max_length=50)
    file_name=models.CharField(max_length=100)
    year=models.IntegerField()
    total_copies=models.IntegerField()
    issued_copies=models.IntegerField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school} {self.class_id} {self.price} {self.name} {self.description}'

class Attendance(models.Model):
    timestamp=models.DateTimeField()
    year=models.IntegerField()
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    section_id=models.ForeignKey(Section,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    status=models.IntegerField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.year} {self.timestamp} {self.class_id} {self.section_id} {self.student_id} {self.status}'


class BookRequest(models.Model):
    book_id=models.ForeignKey(Book,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    issue_start_date=models.DateTimeField()
    issue_end_date=models.DateTimeField()
    status=models.CharField(max_length=50)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school} {self.book_id} {self.student_id}'

class FeeGroup(models.Model):
    name=models.CharField(max_length=100)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.name}'

class Fees(models.Model):
    fee_group_id=models.ForeignKey(FeeGroup,on_delete=models.CASCADE)
    academic_year=models.IntegerField()
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    fee_name=models.CharField(max_length=50)
    amount=models.DecimalField(decimal_places=2,max_digits=8)
    description=models.CharField(max_length=50)
    created=models.DateTimeField()
    modified=models.DateTimeField()
    class_group_id=models.ForeignKey(ClassGroup,on_delete=models.CASCADE)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.fee_name} {self.description} {self.amount}'

class Invoice(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    title=models.ForeignKey(BillingCategory,on_delete=models.CASCADE)
    amount=models.DecimalField(decimal_places=2,max_digits=8)
    invoice_type=models.CharField(max_length=50,choices=(('Income','Income'),('Expenditure','Expenditure')))
    creation_date=models.DateTimeField()
    status=models.CharField(max_length=50,choices=(('Partial','Partial'),('Paid','Paid'),('Pending','Pending')))
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    fees_id=models.ForeignKey(Fees,on_delete=models.CASCADE)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.student_id} {self.title} {self.amount} {self.creation_date}'

class PaymentMethod(models.Model):
    name=models.CharField(max_length=50)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.name}'

class PaymentCategory(models.Model):
    name=models.CharField(max_length=50)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.name}'

class Payment(models.Model):
    expense_category_id=models.ForeignKey(ExpenseCategory,on_delete=models.CASCADE)
    title=models.ForeignKey(PaymentCategory,on_delete=models.CASCADE)
    payment_type=models.CharField(max_length=50,choices=(('Income','Income'),('Ependiture','Expenditure')))
    invoice_id=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    method=models.ForeignKey(PaymentMethod,on_delete=models.CASCADE)
    amount=models.DecimalField(decimal_places=2,max_digits=8)
    timestamp=models.DateTimeField(auto_now_add=True)
    year=models.IntegerField()
    month=models.CharField(max_length=50)
    notes=models.CharField(max_length=50,blank=True,null=True)
    modified=models.DateTimeField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.title} {self.student_id} {self.amount}'

class Ledger(models.Model):
    invoice_no=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    transaction_Type=models.CharField(max_length=50,choices=(('Invoice','Invoice'),('Payment','Payment')))
    ledger_type=models.CharField(max_length=50,choices=(('Income','Income'),('Ependiture','Expenditure')))
    transaction_id=models.IntegerField()
    amount=models.DecimalField(decimal_places=2,max_digits=8)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.transaction_Type} {self.transaction_id} {self.amount}'

class LedgerSummary(models.Model):
    invoice_id=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    invoice_amount=models.DecimalField(decimal_places=2,max_digits=8)
    total_paid=models.DecimalField(decimal_places=2,max_digits=8)
    total_outstanding=models.DecimalField(decimal_places=2,max_digits=8)
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.school}: {self.invoice_id} {self.invoice_amount} {self.total_paid} {self.total_outstanding}'

class ClassSubject(models.Model):
    subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    class_id=models.ForeignKey(Classes,on_delete=models.CASCADE)
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    year=models.IntegerField()
    la1=models.CharField(max_length=50,blank=True,null=True)
    la2=models.CharField(max_length=50,blank=True,null=True)
    la3=models.CharField(max_length=50,blank=True,null=True)
    la4=models.CharField(max_length=50,blank=True,null=True)
    la5=models.CharField(max_length=50,blank=True,null=True)
    la6=models.CharField(max_length=50,blank=True,null=True)
    la7=models.CharField(max_length=50,blank=True,null=True)
    la8=models.CharField(max_length=50,blank=True,null=True)
    la9=models.CharField(max_length=50,blank=True,null=True)
    la10=models.CharField(max_length=50,blank=True,null=True)
    section_id=models.ForeignKey(Section,on_delete=models.CASCADE)
    exam_id=models.ForeignKey(Exam,on_delete=models.CASCADE)
    color=models.CharField(max_length=50,blank=True,null=True)
    icon=models.CharField(max_length=50,blank=True,null=True)
    school=models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.school}: {self.name} {self.subject_id} {self.class_id} {self.section_id}'