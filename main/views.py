from django.shortcuts import render, redirect
from main.models import Contact
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from main.models import Song, Watchlater, History, Channel
from django.shortcuts import redirect
from django.db.models import Case, When


# Create your views here.
def home(request):
    if request.method=="POST":
        
        nm = request.POST.get('name')
        em = request.POST.get('email')
        pn = request.POST.get('contact')
        mg = request.POST.get('message')
        print("name: ",nm," email: ",em," phone: ",pn," message: ",mg)
        obj = Contact(name=nm, email=em, contact=pn, desc=mg)
        obj.save()
        
        str = 'You have recieved a new request Its details are: \n Name of person: ' +nm+'\n Email Id of person: '+em+'\n Contact No. of Person: '+pn+'\n Message: '+mg 
        ob = send_mail('New Query/Suggestion',str,'arshita2523@gmail.com',['arshita2523@gmail.com'],fail_silently=False)
        
        messages.success(request,"We have recieved your request! Our team will get back to you soon!")
    
    return render(request,'main/index.html',{'show': False})

def about(request):
    return render(request,'main/about.html')

def contact(request):
    if request.method=="POST":
        
        nm = request.POST.get('name')
        em = request.POST.get('email')
        pn = request.POST.get('contact')
        mg = request.POST.get('message')
        print("name: ",nm," email: ",em," phone: ",pn," message: ",mg)
        obj = Contact(name=nm, email=em, contact=pn, desc=mg)
        obj.save()
        
        str = 'You have recieved a new request Its details are: \n Name of person: ' +nm+'\n Email Id of person: '+em+'\n Contact No. of Person: '+pn+'\n Message: '+mg 
        ob = send_mail('New Query/Suggestion',str,'arshita2523@gmail.com',['arshita2523@gmail.com'],fail_silently=False)
        
        messages.success(request,"We have recieved your request! Our team will get back to you soon!")
    return render(request,'main/Contact.html')

def discover(request):
    return render(request,'main/Discover.html')



def usignup(request):
    if(request.method=="POST"):
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pwd1 = request.POST.get('password1')
        pwd2 = request.POST.get('password2')
        small= False
        big = False
        digit = False
        symbol = False
        for chr in pwd1:
            if ord(chr)>=65 and ord(chr)<=90:
                big = True
            elif ord(chr)>=97 and ord(chr)<=122:
                small = True
            elif ord(chr)>=48 and ord(chr)<=57:
                digit = True
            elif chr=='@' or chr=='#' or chr=='&' or chr=='$' or chr=='%' or chr=='*' or chr=='!' or chr=='~' or chr=='^' or chr=='(' or chr==')':
                symbol = True 
            if(digit==True and symbol==True and big==True and small==True):
                break

        
     
        if User.objects.filter(username=uname).exists():
            messages.error(request, 'Username already exists!!!')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!!!')
        elif pwd1 != pwd2:
            messages.error(request,'Password and Confirm Password should be same')
        elif len(pwd1)<8:
            messages.error(request,'Password must contain at least eight characters')
        elif small==False:
            messages.error(request,'Password must contain a small letter')
        elif big==False:
            messages.error(request,'Password must contain a capital letter')
        elif symbol==False:
            messages.error(request,'Password must contain a special symbol')
        elif digit==False:
            messages.error(request,'Password must contain a digit')
        else:
            user2 = User.objects.create_user(uname,email,pwd1)
            channel = Channel(name=uname)
            channel.save()
            messages.success(request,"Registration successfull")
    return redirect('/home/')

def ulogin(request):
    if(request.method=="POST"):
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        if User.objects.filter(username=uname).exists():
            user = authenticate(request,username=uname, password=pwd)
            str = 'Welcome ' 

            if(user is not None):
                login(request, user)
                messages.success(request,'Login Successfull')
                return render(request,'main/index.html',{'welcome':str, 'name':uname, 'show': True})
            
            else:
                messages.error(request,'Incorrect password')
                return redirect('/home/')
        
        else:
            messages.error(request,'No user found with this username')
            return redirect('/home/')
    
    return redirect('/home/')

def ulogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/home/')





def comics(request):
    return render(request, 'main/ReadComics.html')

def novels(request):
    return render(request, 'main/ReadNovels.html')

# views for music working 

def music(request):
    song = Song.objects.all()[0:3]

    if request.user.is_authenticated:
        wl = Watchlater.objects.filter(user=request.user)
        ids = []
        for i in wl:
            ids.append(i.video_id)
        
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
        watch = Song.objects.filter(song_id__in=ids).order_by(preserved) 
        watch = reversed(watch)
    
    else:
        watch = Song.objects.all()

    return render(request, 'main/music.html', {'song': song, 'watch': watch})



def channel(request, channel):
    chan = Channel.objects.filter(name=channel).first()
    video_ids = str(chan.music).split(" ")[1:]

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(video_ids)])
    song = Song.objects.filter(song_id__in=video_ids).order_by(preserved)    

    return render(request, "main/channel.html", {"channel": chan, "song": song})

def upload(request):
    if request.method == "POST":
        name = request.POST['name']
        singer = request.POST['singer']
        tag = request.POST['tag']
        image = request.POST['image']
        movie = request.POST['movie']
        credit = request.POST['credit']
        song1 = request.FILES['file']
        message = "Song uploaded successfully"
        song_model = Song(name=name, singer=singer, tags=tag, image=image, movie=movie, credit=credit, song=song1)
        song_model.save()

        music_id = song_model.song_id
        channel_find = Channel.objects.filter(name=str(request.user))
        print(channel_find)

        for i in channel_find:
            i.music += f" {music_id}"
            i.save()
        return render(request, f"main/upload.html", {"message": message})

    return render(request, "main/upload.html")

def history(request):
    if request.method == "POST":
        user = request.user
        music_id = request.POST['music_id']
        history = History(user=user, music_id=music_id)
        history.save()

        return redirect(f"/main/songs/{music_id}")

    history = History.objects.filter(user=request.user)
    ids = []
    for i in history:
        ids.append(i.music_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, 'main/history.html', {"history": song})

def watchlater(request):
    if request.method == "POST":
        user = request.user
        video_id = request.POST['video_id']

        watch = Watchlater.objects.filter(user=user)
        
        for i in watch:
            if video_id == i.video_id:
                message = "This Song is Already Added"
                break
        else:
            watchlater = Watchlater(user=user, video_id=video_id)
            watchlater.save()
            message = "Your Song is Succesfully Added"

        song = Song.objects.filter(song_id=video_id).first()
        return render(request, f"main/songpost.html", {'song': song, "message": message})

    wl = Watchlater.objects.filter(user=request.user)
    ids = []
    for i in wl:
        ids.append(i.video_id)
    
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)

    return render(request, "main/watchlater.html", {'song': song})

def songs(request):
    song = Song.objects.all()
    return render(request, 'main/songs.html', {'song': song})

def songpost(request, id):
    song = Song.objects.filter(song_id=id).first()
    return render(request, 'main/songpost.html', {'song': song})

