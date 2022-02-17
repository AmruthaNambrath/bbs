from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import staff, bus, booking, karnataka, Punjab, Andra, TamilNadu, Kerala, user
from django.contrib import messages
from django.core.mail import EmailMessage
from django.views.decorators.cache import cache_control


# Create your views here.
def home(request):
    return render(request, 'home.html')


def reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        passwordc = request.POST['passwordc']
        email = request.POST['email']
        number = request.POST['number']
        if user.objects.filter(name=username).exists():
            messages.warning(request, "Username or Password already exist..")
            return render(request, 'register.html')
        elif password != passwordc:
            messages.warning(request, "password and confirm password should be same..")
            return render(request, 'register.html')
        else:
            data = user(name=username, password=password, email=email, number=number)
            data.save()
            return render(request, 'home.html')
    else:
        return render(request, 'register.html')



def userlog(request):
    return render(request, 'home.html')



def login(request):
    a = user.objects.get(name=request.POST['username'])
    if a.password == request.POST['password']:
        request.session['a_id'] = a.id
        return render(request, 'userhome.html')
    elif a.password != request.POST['password']:
        messages.success(request, "Username or Password is wrong..")
        return render(request, 'home.html')
    else:
        return render(request, 'home.html')


def admins(request):
    return render(request, 'adminlogin.html')


def admilog(request):
    a = staff.objects.get(username=request.POST['username'])
    if a.password == request.POST['password']:
        return render(request, 'adminp.html')
    else:
        return render(request, 'adminlogin.html')


def userv(request):
    data = user.objects.all()
    return render(request, 'userv.html', {'std': data})


def user_home(request):
    return render(request, 'userhome.html')


def add(request):
    return render(request, 'root.html')


def root(request):
    a = request.POST['busname']
    b = request.POST['froms']
    c = request.POST['to']
    d = request.POST['date']
    e = request.POST['state']
    # e = request.POST['time']
    f = request.POST['fare']
    g = request.POST['frequency']
    h = request.POST['dur']
    data = bus(busname=a, froms=b, to=c, date=d, fare=f, frequency=g, state=e, duration=h)
    data.save()
    return render(request, 'adminp.html')


def search(request):
    try:
        if request.session['a_id']:
            userid = request.session['a_id']
            uname = user.objects.get(id=userid)
            froms = request.POST['from']
            to = request.POST['to']
            if froms == 'Alappuzha' and to == 'Ernakulam':
                a = Kerala(froms=froms, to=to, passname=uname.name)
                a.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Ernakulam' and to == 'Idukki':
                a = Kerala(froms=froms, to=to, passname=uname.name)
                a.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Idukki' and to == 'Kannur':
                a = Kerala(froms=froms, to=to, passname=uname.name)
                a.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Kannur' and to == 'Kasaragod':
                a = Kerala(froms=froms, to=to, passname=uname.name)
                a.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Kasaragod' and to == 'Kollam':
                a = Kerala(froms=froms, to=to, passname=uname.name)
                a.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Kollam' and to == 'Kottayam':
                a = Kerala(froms=froms, to=to, passname=uname.name)
                a.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Chengalpattu' and to == 'Chennai':
                b = TamilNadu(froms=froms, to=to, passname=uname.name)
                b.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Ariyalur' and to == 'Chengalpattu':
                b = TamilNadu(froms=froms, to=to, passname=uname.name)
                b.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Chennai' and to == 'Coimbatore':
                b = TamilNadu(froms=froms, to=to, passname=uname.name)
                b.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Coimbatore' and to == 'Cuddalore':
                b = TamilNadu(froms=froms, to=to, passname=uname.name)
                b.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Cuddalore' and to == 'Dharmapuri':
                b = TamilNadu(froms=froms, to=to, passname=uname.name)
                b.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Dharmapuri' and to == 'Dindigul':
                b = TamilNadu(froms=froms, to=to, passname=uname.name)
                b.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Parvathipuram' and to == 'Arakkuvalley':
                a = Andra(froms=froms, to=to, passname=uname.name)
                a.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Arakkuvalley' and to == 'Vishakaptnam':
                c = Andra(froms=froms, to=to, passname=uname.name)
                c.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Amritsar' and to == 'Bathinda':
                d = Punjab(froms=froms, to=to, passname=uname.name)
                d.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Bathinda' and to == 'Barnala':
                d = Punjab(froms=froms, to=to, passname=uname.name)
                d.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Bakalkott' and to == 'Ballari':
                e = karnataka(froms=froms, to=to, passname=uname.name)
                e.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
            elif froms == 'Ballari' and to == 'Belagavi':
                e = karnataka(froms=froms, to=to, passname=uname.name)
                e.save()
                buss = bus.objects.filter(froms=froms, to=to)
                return render(request, 'booking.html', {'std': buss})
    except:
        return render(request, 'home.html')


def view(request):
    a = bus.objects.all()
    return render(request, 'view.html', {'std': a})


def book(request, id):
    nos = request.POST['seats']
    try:
        if request.session['a_id']:
            if request.method == "POST":
                rte = bus.objects.filter(id=id)
                num = {nos}
                return render(request, 'book.html', {'rate': rte, 'seats': num})
    except:
        return render(request, 'home.html')


def total(request, id):
    try:
        if request.session['a_id']:
            rate = bus.objects.get(id=id)
            fare = rate.fare
            date = rate.date
            # seats = request.POST['seats']
            n = request.POST['pass1']
            b = request.POST['pass2']
            m = request.POST['pass3']
            z = request.POST['pass4']
            y = request.POST['pass5']
            # d = request.POST['date']
            # e = request.POST['u_id']
            # f = request.POST['b_id']
            # a = seats
            # b = rate
            ss = request.session['a_id']
            if n != None and b == '' and m == '' and z == '' and y == '':
                c = int(fare) * 1
                data = booking(pass1=n, rate=c, u_id=ss, date=date, b_id=rate.id)
                data.save()
                disp = booking.objects.filter(u_id=ss).latest('date_now')
                dispp = booking.objects.filter(date_now=disp.date_now)
                return render(request, 'payment.html', {'disp': dispp})
            elif n != None and b != None and m == '' and z == '' and y == '':
                c = int(fare) * 2
                data = booking(pass1=n, pass2=b, rate=c, u_id=ss, date=date, b_id=rate.id)
                data.save()
                disp = booking.objects.filter(u_id=ss).latest('date_now')
                dispp = booking.objects.filter(date_now=disp.date_now)
                return render(request, 'payment.html', {'disp': dispp})
            elif n != None and b != None and m != None and z == '' and y == '':
                c = int(fare) * 3
                data = booking(pass1=n, pass2=b, pass3=m, rate=c, u_id=ss, date=date, b_id=rate.id)
                data.save()
                disp = booking.objects.filter(u_id=ss).latest('date_now')
                dispp = booking.objects.filter(date_now=disp.date_now)
                return render(request, 'payment.html', {'disp': dispp})
            elif n != None and b != None and m != None and z != None and y == '':
                c = int(fare) * 4
                data = booking(pass1=n, pass2=b, pass3=m, pass4=z, rate=c, u_id=ss, date=date, b_id=rate.id)
                data.save()
                disp = booking.objects.filter(u_id=ss).latest('date_now')
                dispp = booking.objects.filter(date_now=disp.date_now)
                return render(request, 'payment.html', {'disp': dispp})
            elif n != None and b != None and m != None and z != None and y != None:
                c = int(fare) * 5
                data = booking(pass1=n, pass2=b, pass3=m, pass4=z, pass5=y, rate=c, u_id=ss, date=date, b_id=rate.id)
                data.save()
                disp = booking.objects.filter(u_id=ss).latest('date_now')
                dispp = booking.objects.filter(date_now=disp.date_now)
                return render(request, 'payment.html', {'disp': dispp})
            else:
                pass
    except:
        pass
        # return render(request, 'last.html')


def history(request):
    history = booking.objects.all()
    users = user.objects.all()
    b = bus.objects.all()
    return render(request, 'history.html', {'history': history, 'users': users, 'b': b})


def states(request):
    try:
        if request.session['a_id']:
            state = request.POST['state']
            if state == 'karnataka':
                return render(request, 'karnataka.html')
            elif state == 'Punjab':
                return render(request, 'punjab.html')
            elif state == 'Andra Pradesh':
                return render(request, 'andra.html')
            elif state == 'TamilNadu':
                return render(request, 'tamilnadu.html')
            elif state == 'Kerala':
                return render(request, 'kerala.html')
            else:
                pass
    except:
        return render(request, 'home.html')


def payment(request):
    return render(request, 'payment.html')



def logout(request):
    if request.session['a_id']:
        del request.session['a_id']
        return render(request, 'home.html')


def success(request):
    return render(request, 'last.html')


def userh(request):
    if request.session['a_id']:
        userid = request.session['a_id']
        history = booking.objects.filter(u_id=userid)
        users = user.objects.all()
        b = bus.objects.all()
        return render(request, 'userhistory.html', {'history': history, 'users': users, 'b': b})



def mail_check(request):
    if request.method == 'POST':
        mail = request.POST['email']
        if user.objects.filter(email=mail).exists():
            email = EmailMessage('forgot password', 'http://127.0.0.1:8000/reset', to=[mail])
            email.send()
            return redirect('home')
        else:
            messages.error(request, 'Invalid E-mail ID!!')
            return redirect('home')
    else:
        return redirect('home')



def reset(request):
    return render(request, 'change.html')



def change(request):
    mail = request.POST['email']
    new = request.POST['new']
    user.objects.filter(email=mail).update(password=new)
    return render(request, 'home.html')


def alogout(request):
    return render(request, 'home.html')

def edit(request):
    return render(request,'edit.html')
def editbus(request):
    froms = request.POST['froms']
    date = request.POST['date']
    bus.objects.filter(froms=froms).update(date=date)
    return render(request,'adminp.html')
def back1(request):
    return render(request,'home.html')
def back2(request):
    return render(request,'userhome.html')
def back3(request):
    return render(request,'userhome.html')
def back3(request):
    return render(request,'userhome.html')
