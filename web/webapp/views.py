from django.shortcuts import render
from .models import report

# Create your views here.

def home(req):
    return render(req, 'index.html')


def progress(req):
    return render(req, 'progress.html')


def insertData(req):
    return render(req, 'insert_data.html')


def insert(req):
    course = req.POST['course']
    studentId = req.POST['studentId']
    studentName = req.POST['studentName']
    status = req.POST['status']
    edu = req.POST['edu']
    advisor = req.POST['adviser']
    work = req.POST['work']
    public = req.POST['public']
    journal = req.POST['journal']
    implement = req.POST['implement']
    meeting = req.POST['meeting']
    from_date = req.POST['from_date']
    to_date = req.POST['to_date']
    year = req.POST['year']
    report_instance = report.objects.create(course=course, student_id=studentId, name=studentName, status=status, edu=edu, advisor=advisor,
                                            work=work, public=public, journal=journal, implemment=implement, meeting=meeting, from_date=from_date, to_date=to_date, year=year)
    return render(req, 'insert_data.html')


def stdPub(req):
    studentId = req.POST['sid']
    all_data = report.objects.all().filter(student_id=studentId).values()
    return render(req, 'std_pub.html', {'data': all_data})


def inYear(req):
    course = req.POST['course']
    status = req.POST['status']
    year = req.POST['year']
    public = req.POST['public']
    journal = req.POST['journal']
    all_data = report.objects.all().filter(course=course).values()
    all_data = all_data.all().filter(status=status).values()
    all_data = all_data.all().filter(year=year).values()
    all_data = all_data.all().filter(public=public).values()
    data = all_data.all().filter(journal=journal).values()
    return render(req, 'in_year.html', {'data': data})


def reportSearch(req):
    course = req.POST['course']
    status = req.POST['status']
    from_year = int(req.POST['from_year'])
    to_year = int(req.POST['to_year'])
    years = []
    total = []
    grandTotal = []
    ddata1 = []
    ddata2 = []
    ddata3 = []
    ddata4 = []
    ddata5 = []
    ddata6 = []
    ddata7 = []
    ddata8 = []
    ddata9 = []
    ddata10 = []
    ddata11 = []

    all_data = report.objects.all().filter(course=course).values()
    all_data = all_data.filter(status=status).values()

    f1 = all_data.filter(public=2).values()
    f2 = all_data.filter(public=3).values()
    f3 = all_data.filter(public=4).values()
    journal = all_data.filter(public=1).values()
    f4 = journal.filter(journal=3).values()
    f5 = journal.filter(journal=6).values()
    f6 = journal.filter(journal=2).values()
    f7 = journal.filter(journal=5).values()
    f8 = journal.filter(journal=4).values()
    f9 = journal.filter(journal=7).values()
    f10 = journal.filter(journal=1).values()
    f11 = journal.filter(journal=8).values()

    for i in range(from_year, to_year + 1):
        year1 = f1.filter(year=i).values().count()
        year2 = f2.filter(year=i).values().count()
        year3 = f3.filter(year=i).values().count()
        year4 = f4.filter(year=i).values().count()
        year5 = f5.filter(year=i).values().count()
        year6 = f6.filter(year=i).values().count()
        year7 = f7.filter(year=i).values().count()
        year8 = f8.filter(year=i).values().count()
        year9 = f9.filter(year=i).values().count()
        year10 = f10.filter(year=i).values().count()
        year11 = f11.filter(year=i).values().count()
        years.append(i)
        ddata1.append(year1)
        ddata2.append(year2)
        ddata3.append(year3)
        ddata4.append(year4)
        ddata5.append(year5)
        ddata6.append(year6)
        ddata7.append(year7)
        ddata8.append(year8)
        ddata9.append(year9)
        ddata10.append(year10)
        ddata11.append(year11)

    total.append(sum(ddata1))
    total.append(sum(ddata2))
    total.append(sum(ddata3))
    total.append(sum(ddata4))
    total.append(sum(ddata5))
    total.append(sum(ddata6))
    total.append(sum(ddata7))
    total.append(sum(ddata8))
    total.append(sum(ddata9))
    total.append(sum(ddata10))
    total.append(sum(ddata11))

    for i in range(len(years)):
        grandTotal.append((ddata1[i] + ddata2[i] +ddata3[i] +ddata4[i] +ddata5[i] +ddata6[i] +ddata7[i] +ddata8[i] +ddata9[i] +ddata10[i] +ddata11[i]))

    data1 = zip(ddata1 , years)
    data2 = zip(ddata2 , years)
    data3 = zip(ddata3 , years)
    data4 = zip(ddata4 , years)
    data5 = zip(ddata5 , years)
    data6 = zip(ddata6 , years)
    data7 = zip(ddata7 , years)
    data8 = zip(ddata8 , years)
    data9 = zip(ddata9 , years)
    data10 = zip(ddata10 , years)
    data11 = zip(ddata11 , years)

    totalPie = total

    total.append(sum(grandTotal))
    return render(req, 'report_search.html', {'ddata1': ddata1, 'ddata2': ddata2, 'ddata3': ddata3, 
                                              'ddata4': ddata4, 'ddata5': ddata5, 'ddata6': ddata6, 
                                              'ddata7': ddata7, 'ddata8': ddata8, 'ddata9': ddata9, 
                                              'ddata10': ddata10, 'ddata11': ddata11, 'from_year': from_year,
                                              'to_year': to_year, 'data1': data1, 'data2': data2, 'data3': data3,
                                                'data4': data4, 'data5': data5, 'data6': data6, 'data7': data7, 
                                                'data8': data8, 'data9': data9, 'data10': data10, 'data11': data11, 
                                                  'years': years, 'course': course, 'status': status, 'total': total,
                                                    'totalPie': totalPie[:-1], 'grandTotal': grandTotal})


def progressSearch(req):
    course = req.POST['course']
    status = req.POST['status']
    from_year = req.POST['from_year']
    to_year = req.POST['to_year']
    all_data = report.objects.all().filter(course=course).values()
    all_data = all_data.all().filter(status=status).values()
    data = all_data.all().filter(year__range=[from_year, to_year]).values()
    return render(req, 'progress_search.html', {'data': data})
