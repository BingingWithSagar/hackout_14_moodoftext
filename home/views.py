from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import post
from .forms import postform
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth import logout
import paralleldots
import json

# Create your views here.
from django.http import HttpResponse

def home(request):
	form = UserCreationForm()
	context ={'form':form}
	return render(request,'home/home.html',context)
@login_required(login_url = '/login')
def journal(request):
	form = postform()
	usernm = request.user.username
	print(usernm)
	if usernm == "psych":
		return redirect('/psych')
	entries = post.objects.filter(user = usernm)
	lis=[]
	for ent in entries:
		lis.append(ent.entry[:40]+"........")
	print(lis)
	
	entries = zip (entries,lis)
	context ={'entries' : entries,
			
				}
	return render(request,'home/journal.html',context)

@login_required(login_url = '/login')
def journalEntry(request):
	if request.method == "POST":
		entry = postform(request.POST)
		if entry.is_valid():
			thisEntry = entry.save(commit=False)
			thisEntry.user = request.user.username
			thisEntry.date = datetime.now()
			data = paralleldots.emotion(thisEntry.entry)
			dick = data['emotion']
			thisEntry.happiness_index = dick['Happy']
			thisEntry.angry_index = dick['Angry']
			thisEntry.bored_index = dick['Bored']
			thisEntry.sad_index = dick['Sad']
			thisEntry.fear_index = dick['Fear']
			thisEntry.excited_index = dick['Excited']
			lis=[0.7,-0.2,-0.2,-0.5,0.1,0.3]
			entries = post.objects.filter(user=request.user.username)
			dep=0
			for entry in entries:
				dep+= entry.happiness_index*lis[0]+entry.angry_index*lis[1]+entry.bored_index*lis[2]+entry.sad_index*lis[3]+entry.fear_index*lis[4]+entry.exited_index*lis[5]
			if(len(entries)!=0):
				dep = dep/len(entries)
			thisEntry.dep = dep
			thisEntry.save()
		
		lis=[]
		entries = zip (entries,lis)
		for ent in entries:
			lis.append(ent.entry)
	

		context ={'entries':entries}
		return render(request,'home/journal.html',context)


	form = postform()
	context ={'form':form}
	return render(request,'home/entry.html',context)


def logout_view(request):
    logout(request)
    return redirect('/login')

def psych_view(request):
	if request.method == "POST":
		name = request.POST.get("name")
		entries = post.objects.filter(user = name)
		context ={'entries':entries}
		lis1 =[]
		for entry in entries:
			lis1.append(entry.happiness_index)
		lis2 =[]
		for entry in entries:
			lis2.append(entry.angry_index)
		lis3 =[]
		for entry in entries:
			lis3.append(entry.bored_index)
		lis4 =[]
		for entry in entries:
			lis4.append(entry.sad_index)
		lis5 =[]
		for entry in entries:
			lis5.append(entry.fear_index)
		lis6 =[]
		for entry in entries:
			lis6.append(entry.exited_index)
		lis7 = []
		for entry in entries:
			lis7.append(entry.dep)

		context={
		'happy':lis1,
		'angry':lis2,
		'bored':lis3,
		'sad':lis4,
		'fear':lis5,
		'excited':lis6,
		'dep':lis7,
		'flag':1
		

		}
		return render(request,'home/psych.html',context)



	return render(request,'home/psych.html',{'flag' : 0})

def single_view(request):
	if request.method == "POST":
		pk1 = request.POST.get("title")
		entries = post.objects.filter(pk=pk1)
		context ={'entries':entries}
		return render(request,'home/single.html',context)
def result_view(request):
	if request.method == "POST":
		pk1 = request.POST.get("title")
		entry = post.objects.filter(pk=pk1)
		entry=entry[0]
		name = request.user.username
		all_entries = post.objects.filter(user = name)
		lis=[]
		for ent in all_entries:
			lis.append(ent.happiness_index)

		maxi=entry.happiness_index
		k=1
		if entry.angry_index>=maxi:
			maxi=entry.angry_index
			k=2
		if entry.bored_index>=maxi:
			maxi=entry.bored_index
			k=3
		if entry.sad_index>=maxi:
			maxi=entry.sad_index
			k=4
		if entry.fear_index>=maxi:
			maxi=entry.fear_index
			k=5
		if entry.exited_index>=maxi:
			maxi=entry.exited_index
			k=6

		if k==1:
		   str_happy="The given input seems to be of a happy tone"
		elif k==2:
		   str_happy="The given input seems to be of a angry tone"
		elif k==3:
		   str_happy="The given input seems to be of a bored tone"
		elif k==4:
		   str_happy="The given input seems to be of a sad tone"
		elif k==5:
		   str_happy="The given input seems to be of a fearful tone"
		elif k==6:
		   str_happy="The given input seems to be of a excited tone"

		context ={'text1':str_happy,
					'list' : lis,
					'k':k}
		return render(request,'home/result.html',context)

def psychentries(request):
	form = postform()
	name = request.POST.get("name")
	entries = post.objects.filter(user = name)
	lis=[]
	for ent in entries:
		lis.append(ent.entry)
	print(lis)
	flag=0
	if request.user.username == "psych":
		flag = 1
	entries = zip (entries,lis)
	context ={'entries':entries,
				'flag' : flag ,
				}
	return render(request,'home/journal.html',context)

def test(request):
	paralleldots.set_api_key( "M4rTJatLfpK0pp1AjE5pZ8ciHa4hW2KTOeq65fUIoEk" )
	text = "i wanna die"
	data = paralleldots.emotion(text)
	dick = data['emotion']
	print(dick['Angry'])
	return render(request,'home/test.html')



