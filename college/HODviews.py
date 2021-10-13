from django.shortcuts import render, redirect
from college.models import Staffs, Courses, Student, Subject, StudentRegno
from django.contrib import messages
import datetime
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def admin_home(request):
    return render(request, 'home_content.html')

def add_staff(request):
    return render(request, 'add_staff_template.html')

def add_staff_save(request):
    if request.method == 'POST':
        idno = request.POST['idno']
        fname = request.POST['first_name']
        mname = request.POST['middle_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        add = request.POST['add']

        try:
            staff = Staffs(id=idno, first_name=fname, middle_name=mname, last_name=lname,email=email, address=add)
            staff.save()
            messages.info(request, "Successfully Added Staff")
            return redirect('/add_staff')
        except:
            messages.info(request, "Failed to Add Staff")
            return redirect('/add_staff')
    else:
        return render(request, 'add_staff_template.html')

def add_course(request):
    return render(request, 'add_course_template.html')

def add_course_save(request):
    if request.method == 'POST':
        cid = request.POST['course_id']
        cname = request.POST['course_name']

        course = Courses(id=cid, course_name=cname)
        course.save()
        messages.info(request, "Successfully Added Course")
        return redirect('/add_course')
    else:
        return render(request, 'add_course_template.html')

def add_student(request):
    courses = Courses.objects.all()
    return render(request, 'add_student_template.html', {'courses': courses})

def add_student_save(request):
    if request.method == 'POST':
        regno = request.POST['regno']
        fname = request.POST['first_name']
        mname = request.POST['middle_name']
        lname = request.POST['last_name']
        gender = request.POST['gender']
        add = request.POST['add']
        course = request.POST['course']
        session_start = request.POST['start']
        session_end = request.POST['end']

        course_obj = Courses.objects.get(id=course)

        #start_date = datetime.datetime.strptime(session_start, '%Y-%m-%d').strftime('%Y-%m-%d')
        #end_date = datetime.datetime.strptime(session_end, '%Y-%m-%d').strftime('%Y-%m-%d')

        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)

        try:
            student = Student(regno=regno, first_name=fname, middle_name=mname, last_name=lname, gender=gender, profile_pic=profile_pic_url, course_id=course_obj, address=add, session_start_year=session_start, session_end_year=session_end)
            student.save()
            messages.info(request, "Successfully Added Student")
            return redirect('/add_student')
        except:
            messages.info(request, "Failed Add Student")
            return redirect('/add_student')
    else:
        return render(request, 'add_student_template.html')

def add_subject(request):
    courses = Courses.objects.all()
    staffs = Staffs.objects.all()
    return render(request, 'add_subject_template.html', {'courses': courses, 'staffs':staffs})

def add_subject_save(request):
    if request.method == 'POST':
        sub_id = request.POST['sub_id']
        sub_name = request.POST['sub_name']
        course = request.POST['course']
        staff = request.POST['staff']

        course_obj = Courses.objects.get(id=course)
        staff_obj = Staffs.objects.get(id=staff)

        try:
            sub = Subject(id=sub_id, subject_name=sub_name, course_id=course_obj, staff_id=staff_obj)
            sub.save()
            messages.info(request, "Successfully Added Subject")
            return redirect('/add_subject')
        except:
            messages.info(request, "Failed to Add Subject")
            return redirect('/add_subject')
    else:
        return render(request, 'add_subject_template.html')

def manage_staff(request):
    staffs = Staffs.objects.all()
    return render(request, 'manage_staff_template.html', {'staffs': staffs})

def delete_staff(request, id):
    staff = Staffs.objects.get(id=id)
    staff.delete()
    return redirect('/manage_staff')

def manage_student(request):
    students = Student.objects.all()
    return render(request, 'manage_student_template.html', {'students': students})

def manage_course(request):
    courses = Courses.objects.all()
    return render(request, 'manage_course_template.html', {'courses': courses})

def delete_course(request, id):
    course = Courses.objects.get(id=id)
    course.delete()
    return redirect('/manage_course')

def manage_subject(request):
    subjects = Subject.objects.all()
    return render(request, 'manage_subject_template.html', {'subjects': subjects})

def delete_subject(request, id):
    subject = Subject.objects.get(id=id)
    subject.delete()
    return redirect('/manage_subject')

def edit_staff(request, id):
    staff = Staffs.objects.get(id=id)
    return render(request, 'edit_staff_template.html', {'staff':staff})

def edit_student(request, id):
    student = Student.objects.get(id=id)
    courses = Courses.objects.all()
    return render(request, 'edit_student_template.html', {'student':student, 'courses':courses})

def edit_course(request, id):
    course = Courses.objects.get(id=id)
    return render(request, 'edit_course_template.html', {'course': course})

def edit_subject(request, id):
    subject = Subject.objects.get(id=id)
    courses = Courses.objects.all()
    staffs = Staffs.objects.all()
    return render(request, 'edit_subject_template.html', {'subject': subject, 'courses':courses, 'staffs':staffs})

def edit_staff_save(request):
    if request.method == 'POST':
        staff_id = request.POST['idno']
        fname = request.POST['first_name']
        mname = request.POST['middle_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        add = request.POST['add']
        
        try:
            staffs = Staffs.objects.get(id=staff_id)
            staffs.id = staff_id
            staffs.first_name = fname
            staffs.middle_name = mname
            staffs.last_name = lname
            staffs.email = email
            staffs.address = add
            staffs.save()

            messages.info(request, "Successfully Edited Staff")
            return redirect('/edit_staff/'+staff_id)
        except:
            messages.info(request, "Failed to Edit Staff")
            return redirect('/edit_staff/'+staff_id)
    else:
        return render(request, 'edit_staff_template.html')

def edit_student_save(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        regno = request.POST['regno']
        fname = request.POST['first_name']
        mname = request.POST['middle_name']
        lname = request.POST['last_name']
        gender = request.POST['gender']
        add = request.POST['add']
        course = request.POST['course']
        session_start = request.POST['start']
        session_end = request.POST['end']

        course_obj = Courses.objects.get(id=course)

        if request.FILES['profile_pic']:
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None

        try:
            student = Student.objects.get(id=student_id)
            student.id = student_id
            student.regno = regno
            student.first_name = fname
            student.middle_name = mname
            student.last_name = lname
            student.gender = gender
            if profile_pic_url != None:
                student.profile_pic = profile_pic_url
            student.course_id = course_obj
            student.address = add
            student.session_start_year = session_start
            student.session_end_year = session_end
            student.save()

            messages.info(request, "Successfully Edited Student")
            return redirect('/edit_student/'+student_id)
        except:
            messages.info(request, "Failed to Edit Student")
            return redirect('/edit_student/'+student_id)
    else:
        return render(request, 'edit_student_template.htm')

def edit_course_save(request):
    if request.method == 'POST':
        course_id = request.POST['course_id']
        course_name = request.POST['course_name']

        try:
            course = Courses.objects.get(id=course_id)
            course.id = course_id
            course.course_name = course_name
            course.save()

            messages.info(request, "Successfully Edited Course")
            return redirect('/edit_course/'+course_id)
        except:
            messages.info(request, "Failed to Edit Course")
            return redirect('/edit_course/'+course_id)
    else:
        return render(request, 'edit_course_template.html')

def edit_subject_save(request):
    if request.method == 'POST':
        sub_id = request.POST['sub_id']
        sub_name = request.POST['sub_name']
        course = request.POST['course']
        staff = request.POST['staff']

        course_obj = Courses.objects.get(id=course)
        staff_obj = Staffs.objects.get(id=staff)

        try:
            sub = Subject.objects.get(id=sub_id)
            sub.id = sub_id
            sub.subject_name = sub_name
            sub.course_id = course_obj
            sub.staff_id = staff_obj
            sub.save()

            messages.info(request, "Successfully Edited Subject")
            return redirect('/edit_subject/'+sub_id)
        except:
            messages.info(request, "Failed to Edit Subject")
            return redirect('/edit_subject/'+sub_id)
    else: 
        return render(request, 'edit_subject_template.html')
    