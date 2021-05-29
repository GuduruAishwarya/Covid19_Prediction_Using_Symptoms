from tkinter import *  # package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit
from tkinter import messagebox  #Access to standard Tk dialog boxes.
#sklearn: scikit learn has many classification,regression, clustering algorithms in machine learning,statistical modeling

from sklearn.naive_bayes import MultinomialNB #probablistic approach
from sklearn.metrics import accuracy_score

import numpy as np #to perform numerical operations
import pandas as pd  #for reading csv files
#symptoms list ->same order as dataset
l1 =['COUGH','MUSCLE_ACHES'	,'TIREDNESS','SORE_THROAT','RUNNY_NOSE','STUFFY_NOSE','FEVER','NAUSEA',
     'VOMITING','DIARRHEA','SHORTNESS_OF_BREATH',	'DIFFICULTY_BREATHING',	'LOSS_OF_TASTE',
     'LOSS_OF_SMELL','ITCHY_NOSE','ITCHY_EYES',	'ITCHY_MOUTH','ITCHY_INNER_EAR','COLD','PINK_EYE','TYPE']

#list of diseases
disease =['ALLERGY','SEVERE COVID','COMMON FLU','MILD COVID','COLD']

l2 =[] #equal length as symptoms and put all values as 0
for x in range(0 ,len(l1)):
    l2.append(0)

# TRAINING DATA
df =pd.read_csv("D:\\MiniProject\\trainingSet.csv",delimiter=",",header=0) #pandas object to read csv file
#print(df[df.columns.intersection(l1)])
#df.columns=df.columns.to_series().apply(lambda x:x.strip())
#inplace=true means returns void else it returns object which are then further saved into variable
df.replace({'TYPE' :{'MILD COVID' :0 ,'SEVERE COVID' :1 ,'COMMON FLU' :2 ,'ALLERGY' :3 ,'COLD' :4}} ,inplace=True) #numbering the diseases or giving indices
X= df[l1] #symptoms
y = df[["TYPE"]]  #output-diseases
#np.ravel(y)

# TESTING DATA
tr =pd.read_csv("D:\\MiniProject\\TestingSet.csv",delimiter=",",header=0)
#tr.columns=tr.columns.to_series().apply(lambda x:x.strip())
tr.replace({'TYPE' :{'MILD COVID' :0 ,'SEVERE COVID' :1 ,'COMMON FLU' :2 ,'ALLERGY' :3 ,'COLD' :4}} ,inplace=True)

X_test= tr[l1]
y_test = tr[["TYPE"]]
#np.ravel(y_test)

#print(tr[tr.columns.intersection(l1)])

def message():
    if (Symptom1.get() == "None" and Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
        messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
    else :
        NaiveBayes()
def printPre(n):
    print(n)
    s=""
    #ALLERGY','SEVERE COVID','COMMON FLU','MILD COVID','COLD'
    if(n==0):
        s=s+"Take your medicines as prescribed.\nEat Healthy food\nReduce exposure to allergy triggers."
    elif(n==1):
        s=s+"Wear Mask\nMaintain Self Distance\nClean hands\nJoin in Hospital"
    elif(n==2):
        s=s+"Eat nutrient-rich Diet \nWash Hands frequently\nTake rest\nClean and disinfect surfaces"
    elif(n==3):
        s=s+"Wear Mask\nStay isolated\nTake medication\nWash your hands frequently\nTake healthy food"
    elif(n==4):
        s=s+"Gargling\nBlow Your Nose Often\nTreat Stuffy Nose With Warm Salt Water."
    else :
        s=s+"no diseases"
    t4.delete("1.0", END)  # deletes existing tkinter text from widget (first,last) content indices
    t4.insert(END, s)


def NaiveBayes():
    clf3 = MultinomialNB() #multinomial Naive Bayes classifier is used for classification with discrete features
    clf3= clf3.fit(X,np.ravel(y)) # fit method takes the training data as arguments. ravel->used to change a 2-dimensional array or a multi-dimensional array into a contiguous flattened array.
#[[1,2,3],[4,5,6]]=>[1,2,3,4,5,6]
    y_pred = clf3.predict(X_test) #enables us to predict the labels of the data values on the basis of the trained model and algorithm and stores in variavle
    print(accuracy_score(y_test, y_pred)) # computes subset accuracy ->gives float type max:1 (accurate)
    #print(accuracy_score(y_test, y_pred, normalize=False)) # normalize If False, returns no of correctly classified samples else returns fraction of correctly classified samples.
    #int type gives no. of samples which are predicted as true.
    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    for k in range(0,len(l1)):
        for z in psymptoms:
            if( z==l1[k]):
                l2[k]= 1

    inputtest = [l2]
    predict = clf3.predict(inputtest) #returns array of one element
    predicted= predict[0] #gives disease index after prediction
    print("@",predicted)
    h='no'
    for a in range(0,len(disease)):
        if( predicted == a):
            h= 'yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END) #deletes existing tkinter text from widget (first,last) content indices
        t3.insert(END, disease[a]) #current position
        print(disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "No Disease found")
    printPre(predicted)

root = Tk() #creates a toplevel widget of Tk which usually is the main window of an application
root.title("Course Project DWDM")  #Shows title on widget,same as webpage
root.configure(background='#aec6cf')  #used to access an object's attributes after its initialisation. i.e setting lable as text attribute
root.geometry("1500x1000")


Symptom1 = StringVar() #Tkinter StringVar helps you manage the value of a widget such as a Label or other Entry more effectively
Symptom1.set(None) #Tkinter supports some variables  to manipulate the values of widgets.set() and get() methods are used to set and retrieve the values of these variables.
Symptom2 = StringVar()
Symptom2.set(None) #initially setting none
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)

S6Lb = Label(root, text="What to Do ??? :")
S6Lb.config(font=("Elephant", 25),background="#aec6cf")
S6Lb.grid(row=13, column=2, sticky=W)

t4 = Text(root, height=7, width=50)# to show text data on application , displays mutli line text
t4.config(font=("TimesNewRoman", 14))
t4.grid(row=14, column=2,padx=30 )

w2 = Label(root, text="Covid19 Prediction From Symptoms ",font="none 30 bold") #widget implements a display box where you can place text or images
#w2.config(anchor=CENTER) #setting few attributes and configuring label
w2.configure(background="#aec6cf")
w2.grid(row=1, column=0, columnspan=2,pady=30) #grid ->where to locate it geometry manager puts widgets in 2d table. i.e. row and columns



S1Lb = Label(root, text="Symptom 1")
S1Lb.config(font=("Elephant", 15),background="#aec6cf")
S1Lb.grid(row=7, column=0 , padx=2,pady=10,sticky=W)  #sticking to W West direction if cell cannot fit widget

S2Lb = Label(root, text="Symptom 2")
S2Lb.config(font=("Elephant", 15),background="#aec6cf")
S2Lb.grid(row=8, column=0, padx=2,pady=10, sticky=W)

S3Lb = Label(root, text="Symptom 3")
S3Lb.config(font=("Elephant", 15),background="#aec6cf")
S3Lb.grid(row=9, column=0, padx=2,pady=10, sticky=W)

S4Lb = Label(root, text="Symptom 4")
S4Lb.config(font=("Elephant", 15),background="#aec6cf")
S4Lb.grid(row=10, column=0, padx=2,pady=10, sticky=W)

S5Lb = Label(root, text="Symptom 5")
S5Lb.config(font=("Elephant", 15),background="#aec6cf")
S5Lb.grid(row=11, column=0, padx=2,pady=10, sticky=W)

lr = Button(root, text="Predict",height=1, width=20, command=message) #adds buttons to application. command-> method to be invoked if button is clicked
lr.config(font=("Elephant", 15))
lr.grid(row=14, column=0,pady=10)

OPTIONS = sorted(l1) #list of symptoms in sorted order for option menu

S1En = OptionMenu(root, Symptom1,* OPTIONS) #helper class that creates popup menu and a button to display it. Drop down list with many option values
S1En.grid(row=7, column=1)

S2En = OptionMenu(root, Symptom2,* OPTIONS) #selected value is saved in the variable
S2En.grid(row=8, column=1)

S3En = OptionMenu(root, Symptom3,* OPTIONS)
S3En.grid(row=9, column=1)

S4En = OptionMenu(root, Symptom4,* OPTIONS)
S4En.grid(row=10, column=1)

S5En = OptionMenu(root, Symptom5,* OPTIONS)
S5En.grid(row=11, column=1)

S6Lb = Label(root, text="Disease :")
S6Lb.config(font=("Elephant", 22),background="#aec6cf")
S6Lb.grid(row=7, column=2, sticky=W)

t3 = Text(root, height=2, width=20)# to show text data on application , displays mutli line text
t3.config(font=("Elephant", 20))
t3.grid(row=9, column=2 , padx=10)




root.mainloop() #tells python to run tinker event loops till user exits window
