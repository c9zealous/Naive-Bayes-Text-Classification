import glob
import re
import collections
from collections import Counter
from nltk.stem import WordNetLemmatizer
file_name="stoplist.txt"
stoplist=[]
stoplist1={}
temp=[]
bayes={}
bayesone=[]
bayestwo=[]
bayesthree=[]
bayesfour={}
vocabulary={}
arxiv={}
jdm={}
plos={}
lemmatiser=WordNetLemmatizer()
classlabel1="arxiv"
classlabel2="jdm"
classlabel3="plos"

def createtestmat(vocabulary1,classlabel):
	count=0
	for f in glob.glob("./articles/"+classlabel+"/*.txt"):
		if count>149:
			with open(f,'r',encoding='cp437') as file:
				temp=file.read()
				t1=re.findall(r'\w+',str(temp))
				tdict={}
				for j in range(0,len(t1)):
					t1[j]=re.sub(r'[^a-zA-Z0-9 ]',r'',str(t1[j])).lower()
					if t1[j] in vocabulary1:
						if t1[j] not in tdict:
							tdict[t1[j]]=1
						else:
							tdict[t1[j]]+=1
				bayesfour[f]=tdict
		count+=1

def addallval(x,y,z):
	a=Counter(x)
	b=Counter(y)
	c=Counter(z)
	return a+b+c

def matrixarxiv(bays):
	newarxiv={}
	for key in bays:
		if bays[key]['classlabel']=="arxiv":
			for key,val in bays[key].items():
				if val==1:
					if key not in newarxiv:
						newarxiv[key]=1
					else:
						newarxiv[key]+=1
	return newarxiv

def matrixjdm(bays):
	newjdm={}
	for key in bays:
		if bays[key]['classlabel']=="jdm":
			for key,val in bays[key].items():
				if val==1:
					if key not in newjdm:
						newjdm[key]=1
					else:
						newjdm[key]+=1
	return newjdm

def matrixplos(bays):
	newplos={}
	for key in bays:
		if bays[key]['classlabel']=="plos":
			for key,val in bays[key].items():
				if val==1:
					if key not in newplos:
						newplos[key]=1
					else:
						newplos[key]+=1
	return newplos

def calculatebayesprobability(bay1,a,j,p,t):
	freqincount=0
	freqincount1=0
	freqincount2=0
	freqincount3=0
	c1=0
	c2=0
	c3=0
	for key,val in bay1.items():
		probability1=1.0
		probability2=1.0
		probability3=1.0
		for key1,value1 in bay1[key].items():
			if key1 in a:
				probability1*=(float)(value1*a[key1]/t[key1])
			if key1 in j:
				probability2*=(float)(value1*j[key1]/t[key1])
			if key1 in p:
				probability3*=(float)(value1*p[key1]/t[key1])
		final=max(probability1,probability2,probability3)
		key1=key.split("/")
		key2=key1[2].split("\\")
		actual=key2[0]
		if final==probability1:
			print("------------------------------------------------------")
			print("Actual class: "+actual.upper())
			print("Classified class: ARXIV")
			if actual=="arxiv":
				freqincount1+=1
				freqincount+=1
			c1+=1
		elif final==probability2:
			print("------------------------------------------------------")
			print("Actual class: "+actual.upper())
			print("Classified class: JDM")
			if actual=="jdm":
				freqincount2+=1
				freqincount+=1
			c2+=1
		else:
			print("------------------------------------------------------")
			print("Actual class: "+actual.upper())
			print("Classified class: PLOS")
			if actual=="plos":
				freqincount3+=1
				freqincount+=1
			c3+=1
	print("------------------------------------------------------")
	print("Accuracy of Bayes Classifier is: "+str((float)(freqincount/len(bay1))*100)+"%")
	print("Accuracy of Bayes Classifier for arxiv is: "+str((float)(freqincount1/c1)*100)+"%")
	print("Accuracy of Bayes Classifier for jdm is: "+str((float)(freqincount2/c2)*100)+"%")
	print("Accuracy of Bayes Classifier for plos is: "+str((float)(freqincount3/c3)*100)+"%")

def createfeaturematrix(vocabulary1,classlabel):
	count=0
	for f in glob.glob("./articles/"+classlabel+"/*.txt"):
		tdict={}
		if count==splithalf:
			break
		with open(f,'r',encoding='cp437') as file:
			temp=file.read()
			featurevocab={}
			tempmat=re.sub(r'[^a-zA-Z0-9 ]',r'',str(temp)).lower()
			for key in vocabulary1:
				if key in temp:
					featurevocab[key]=1
				else:
					featurevocab[key]=0
			featurevocab.update({'classlabel':classlabel})
			bayes[f]=featurevocab
			file.close()
		count+=1

def createvocabulary(train1):
	for i in range(0,len(train1)):
		tdict={}
		temp=re.findall(r'\w+',str(train1[i]))
		for j in range(0,len(temp)):
			temp[j]=temp[j].lower()
			temp[j]=re.sub(r'[^a-zA-Z0-9]',r'',temp[j])
			temp[j]=lemmatiser.lemmatize(temp[j],pos='v')
			temp[j]=lemmatiser.lemmatize(temp[j],pos='a')
			temp[j]=lemmatiser.lemmatize(temp[j],pos='n')
			temp[j]=lemmatiser.lemmatize(temp[j],pos='r')
			if temp[j] not in stoplist1:
				if temp[j] not in vocabulary:
					vocabulary[temp[j]]=1
					tdict[temp[j]]=1
				elif temp[j] in vocabulary and temp[j] not in tdict:
					vocabulary[temp[j]]+=1
					tdict[temp[j]]=1

with open(file_name) as f:
	for line in f:
		stoplist.append(line.split('\''));
for i in range(0,len(stoplist)):
	for char in ['\\n',' ',',','\'']:
		stoplist[i]=str(stoplist[i]).replace(char,'')
		if stoplist[i] not in stoplist1:
			stoplist1[stoplist[i]]=1
		else:
			stoplist1[stoplist[i]]+=1

for f in glob.glob("./articles/arxiv/*.txt"):
	with open(f,'r',encoding='cp437') as file:
		bayesone.append(file.readlines())
		file.close()
splithalf=int(len(bayesone)/2)
train=bayesone[:splithalf]
createvocabulary(train)

for f in glob.glob("./articles/jdm/*.txt"):
	with open(f,'r',encoding='cp437') as file:
		bayestwo.append(file.readlines())
		file.close()
splithalf=int(len(bayestwo)/2)
train=bayestwo[:splithalf]
createvocabulary(train)

for f in glob.glob("./articles/plos/*.txt"):
	with open(f,'r',encoding='cp437') as file:
		bayesthree.append(file.readlines())
		file.close()
splithalf=int(len(bayesthree)/2)
train=bayesthree[:splithalf]
createvocabulary(train)

for key,val in vocabulary.copy().items():
	if val==1:
		del vocabulary[key]
vocabulary=collections.OrderedDict(sorted(vocabulary.items()))

createfeaturematrix(vocabulary,classlabel1)
createfeaturematrix(vocabulary,classlabel2)
createfeaturematrix(vocabulary,classlabel3)

arxiv=matrixarxiv(bayes)
jdm=matrixjdm(bayes)
plos=matrixplos(bayes)
total=addallval(arxiv,jdm,plos)

createtestmat(vocabulary,classlabel1)
createtestmat(vocabulary,classlabel2)
createtestmat(vocabulary,classlabel3)

calculatebayesprobability(bayesfour,arxiv,jdm,plos,total)
