import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import matplotlib
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.externals import joblib
import pandas as pd
import os
import tkinter.scrolledtext as tkst





def printtext():
    #global e

    global df_gender_f,df_gender_m,df_gender_t,df_pul_n,df_pul_y,df_pt_fail,df_pt_new,df_pt_newot,df_pt_relapse,df_pt_rtrt, df_pt_trnfin,df_pt_tad,df_srn,df_srp,df_srsc,df_hiv_n,df_hiv_y,df_endip_n, df_endip_p,df_endip_sc,df_extip_nr,df_extip_n,df_extip_p,df_extip_sc,df_age_12,df_age_25,df_age_35,df_age_45,df_age_60,df_age_80,df_age_g80

    

    
    gender_str = gender.get()
    gender_str = gender_str.lower()

    if gender_str == "male":
        df_gender_f = 0
        df_gender_m = 1
        df_gender_t = 0
    elif gender_str == "female":
        
        df_gender_f = 1
        df_gender_m = 0
        df_gender_t = 0

    elif gender_str == 'trans':
        df_gender_f = 0
        df_gender_m = 0
        df_gender_t = 1

    else:

        error_str_gender = "Wrong GENDER input ! Please press quit and try again"
        #messagebox.showerror("error",error_str_gender)
        

    
    sot_str  = pul.get()
    sot_str = sot_str.lower()

    if sot_str == "yes":
        df_pul_n = 0
        df_pul_y = 1
    elif sot_str == "no":
        df_pul_n = 1
        df_pul_y = 0
    else:
        error_str_sot =  "Wrong (PULMONARY TB OR NOT) input ! Please press quit and try again"
        #print (error_str_sot)
        #messagebox.showerror("error",error_str_sot)
        


          
    ptype_str = ptype.get()
    ptype_str = ptype_str.lower()

    if ptype_str == "failure":
        
        df_pt_fail = 1
        df_pt_new = 0
        df_pt_newot = 0
        df_pt_relapse = 0
        df_pt_rtrt = 0
        df_pt_trnfin = 0
        df_pt_tad = 0

        
    elif ptype_str == "new":
        
        df_pt_fail = 0
        df_pt_new = 1
        df_pt_newot = 0
        df_pt_relapse = 0
        df_pt_rtrt = 0
        df_pt_trnfin = 0
        df_pt_tad = 0

    elif ptype_str == "new others":
        
        df_pt_fail = 0
        df_pt_new = 0
        df_pt_newot = 1
        df_pt_relapse = 0
        df_pt_rtrt = 0
        df_pt_trnfin = 0
        df_pt_tad = 0


    elif ptype_str == "relapse":
        
        df_pt_fail = 0
        df_pt_new = 0
        df_pt_newot = 0
        df_pt_relapse = 1
        df_pt_rtrt = 0
        df_pt_trnfin = 0
        df_pt_tad = 0

    elif ptype_str == "retreatment":
        
        df_pt_fail = 0
        df_pt_new = 0
        df_pt_newot = 0
        df_pt_relapse = 0
        df_pt_rtrt = 1
        df_pt_trnfin = 0
        df_pt_tad = 0


    elif ptype_str == "transfer in":
        
        df_pt_fail = 0
        df_pt_new = 0
        df_pt_newot = 0
        df_pt_relapse = 0
        df_pt_rtrt = 0
        df_pt_trnfin = 1
        df_pt_tad = 0

    elif ptype_str == "TA default":
        
        df_pt_fail = 0
        df_pt_new = 0
        df_pt_newot = 0
        df_pt_relapse = 0
        df_pt_rtrt = 0
        df_pt_trnfin = 0
        df_pt_tad = 1
    else:
        ptype_error_1 = "Wrong (PATIENT TYPE) input ! Please press quit and try again"
        print (ptype_error_1)
        
        
    
    sr_str = sr.get()
    sr_str = sr_str.lower()

    if sr_str == 'negative':
        df_srn = 1
        df_srp = 0
        df_srsc = 0


    elif sr_str == 'positive':
        df_srn = 0
        df_srp = 1
        df_srsc = 0

    if sr_str == 'scanty':
        df_srn = 0
        df_srp = 0
        df_srsc = 1


    else:
        error_sr_str = "Wrong (PATIENT TYPE) input ! Please press quit and try again"
        #print (error_sr_str)
        


    
    hiv_str = hiv.get()

    hiv_str = hiv_str.lower()

    if hiv_str == 'negative':
        df_hiv_n = 1
        df_hiv_y = 0

    elif hiv_str == 'positive':
        df_hiv_n = 0
        df_hiv_y = 1

    else:
        error_hiv_str = "Wrong (HIV STATUS) input ! Please press quit and try again"
        #print (error_hiv_str)
        
        
    
    endip_str = endip.get()
    endip_str = endip_str.lower()
    

    if endip_str == 'negative':
        df_endip_n = 1
        df_endip_p = 0
        df_endip_sc = 0

    
    elif endip_str == 'positive':
        df_endip_n = 0
        df_endip_p = 1
        df_endip_sc = 0

    elif endip_str == 'scanty':
        df_endip_n = 0
        df_endip_p = 0
        df_endip_sc = 1
    else:
        error_endip_str = "Wrong (EndIP Sputum result) input ! Please press quit and try again"
        print (error_endip_str)
        #messagebox.showerror("error",error_endip_str)
        
    


    extip_str = extip.get()
    extip_str = extip_str.lower()

    if extip_str == 'na':
        df_extip_nr = 1
        df_extip_n = 0
        df_extip_p=0
        df_extip_sc = 0
        
    elif extip_str == 'negative':
        df_extip_nr = 0
        df_extip_n = 1
        df_extip_p=0
        df_extip_sc = 0

    elif extip_str == 'positive':
        df_extip_nr = 0
        df_extip_n = 0
        df_extip_p=1
        df_extip_sc = 0

    elif extip_str == 'scanty':
        df_extip_nr = 0
        df_extip_n = 0
        df_extip_p=0
        df_extip_sc = 1

    else:
        error_extip_str = "Wrong (ExtIP Sputum result) input ! Please press quit and try again"
        print (error_extip_str)
        #messagebox.showerror("error",error_extip_str)
        
    

    age_str = age.get()

    
    age_str = int(age_str)
    

    if 0< age_str <= 12:
        df_age_12 = 1
        df_age_25 = 0
        df_age_35 = 0
        df_age_45 = 0
        df_age_60 = 0
        df_age_80 = 0
        df_age_g80 = 0

    elif 12 < age_str <= 25:
        df_age_12 = 0
        df_age_25 = 1
        df_age_35 = 0
        df_age_45 = 0
        df_age_60 = 0
        df_age_80 = 0
        df_age_g80 = 0

    elif 25< age_str <= 35:
        df_age_12 = 0
        df_age_25 = 0
        df_age_35 = 1
        df_age_45 = 0
        df_age_60 = 0
        df_age_80 = 0
        df_age_g80 = 0

    elif 35< age_str <= 45:
        df_age_12 = 0
        df_age_25 = 0
        df_age_35 = 0
        df_age_45 = 1
        df_age_60 = 0
        df_age_80 = 0
        df_age_g80 = 0    



    elif 45< age_str <= 60:
        df_age_12 = 0
        df_age_25 = 0
        df_age_35 = 0
        df_age_45 = 0
        df_age_60 = 1
        df_age_80 = 0
        df_age_g80 = 0


    elif 60< age_str <= 80:
        df_age_12 = 0
        df_age_25 = 0
        df_age_35 = 0
        df_age_45 = 0
        df_age_60 = 0
        df_age_80 = 1
        df_age_g80 = 0

    
    elif age_str > 80:
        
        df_age_12 = 0
        df_age_25 = 0
        df_age_35 = 0
        df_age_45 = 0
        df_age_60 = 0
        df_age_80 = 0
        df_age_g80 = 1


    else:
        error_age_str = "Wrong ( AGE ) input ! Please press quit and try again"
        print (error_age_str)
        #messagebox.showerror("error",error_age_str)
        #tkMessageBox.alert("Error","Please re-enter age")
    #print (gender_str,sot_str)
    """
    print (df_gender_f,df_gender_m,df_gender_t,df_pul_n,df_pul_y,df_pt_fail,df_pt_new,
            df_pt_newot,df_pt_relapse,df_pt_rtrt, df_pt_trnfin,df_pt_tad,
            df_srn,df_srp,df_srsc,df_hiv_n,df_hiv_y,df_endip_n, df_endip_p,
            df_endip_sc,df_extip_nr,df_extip_n,df_extip_p,df_extip_sc,
            df_age_12,df_age_25,df_age_35,df_age_45,df_age_60,df_age_80,df_age_g80)

    """
    return (df_gender_f,df_gender_m,df_gender_t,df_pul_n,df_pul_y,df_pt_fail,df_pt_new,
            df_pt_newot,df_pt_relapse,df_pt_rtrt, df_pt_trnfin,df_pt_tad,
            df_srn,df_srp,df_srsc,df_hiv_n,df_hiv_y,df_endip_n, df_endip_p,
            df_endip_sc,df_extip_nr,df_extip_n,df_extip_p,df_extip_sc,
            df_age_12,df_age_25,df_age_35,df_age_45,df_age_60,df_age_80,df_age_g80)


def prepare_data():

    global df
    

    df_gender_f,df_gender_m,df_gender_t,df_pul_n,df_pul_y,df_pt_fail,df_pt_new,df_pt_newot,df_pt_relapse,df_pt_rtrt, df_pt_trnfin,df_pt_tad,df_srn,df_srp,df_srsc,df_hiv_n,df_hiv_y,df_endip_n, df_endip_p,df_endip_sc,df_extip_nr,df_extip_n,df_extip_p,df_extip_sc,df_age_12,df_age_25,df_age_35,df_age_45,df_age_60,df_age_80,df_age_g80 = printtext()







    cols = ['pgender__F','pgender__M','pgender__T','dcpulmonary__N','	dcpulmonary__Y','PatientType__Failure',
        'PatientType__New','PatientType__New Others','PatientType__Relapse','PatientType__Retreatment Others',
        'PatientType__Transfer In','PatientType__Treatment after default','SR__Neg','SR__Pos',
        'SR__SC','HIVStatus__Neg','HIVStatus__Pos','EndIP__Neg','EndIP__Pos','EndIP__SC','	ExtIP__NR','ExtIP__Neg',
        'ExtIP__Pos','ExtIP__SC','page__<=12','page__<=25','page__<=35','page__<=45','page__<=60','page__<=80','page__>80']
    df = pd.DataFrame(columns=cols)
#
    df1 = pd.DataFrame(data=[[df_gender_f,df_gender_m,df_gender_t,df_pul_n,df_pul_y,df_pt_fail,df_pt_new,
                          df_pt_newot,df_pt_relapse,df_pt_rtrt, df_pt_trnfin,df_pt_tad,
                          df_srn,df_srp,df_srsc,df_hiv_n,df_hiv_y,df_endip_n, df_endip_p,
                          df_endip_sc,df_extip_nr,df_extip_n,df_extip_p,df_extip_sc,
                          df_age_12,df_age_25,df_age_35,df_age_45,df_age_60,df_age_80,df_age_g80]],columns=cols)
    df = pd.concat([df,df1], axis=0)

    df.index = range(len(df.index))
    return df

def run_model():

    global result_low_str,result_med_str, result_high_str,report
    filename = filedialog.askopenfilename()


    loaded_model = joblib.load(filename)
    result = loaded_model.predict(df)
    proba = loaded_model.predict_proba(df)
    
    #f_imp = loaded_model

    if result == 0:

        result_low_str = "Priority: Low , Class : {0} , Probability: {1}".format(result, proba)
        print ("Priority: Low , Class : {0} , Probability: {1}".format(result, proba))
        report = result_low_str

    elif result == 1:
        result_med_str = "Priority: Medium , Class : {0} , Probability: {1}".format(result, proba)
        print ("Priority: Medium , Class : {0} , Probability: {1}".format(result, proba))
        report = result_med_str

    else:
        result_high_str = "Priority: High , Class : {0} , Probability: {1}".format(result, proba)
        print ("Priority: High , Class : {0} , Probability: {1}".format(result, proba))
        report = result_high_str

    messagebox.showinfo("result",report)

    return report

#p = sub.Popen('F:\CEPT_2018\STUDIO_EGOV\Sequential\publish_ml\tkinter_1.py',stdout=sub.PIPE,stderr=sub.PIPE)
#output, errors = p.communicate()

root = Tk()
root.geometry("800x600")


root.title('Early Case-Severity Warning System: CEPT 2018')

#text = Text(root)
#text.grid(row=11, column=1, sticky=W)
#text.insert(END, output)



gender = Entry(root)
L1 = Label(root,text="Gender")
L1.grid(row=0, column=0, sticky=N+S+E+W)
gender.grid(row=0, column=1, sticky=N+S+E+W)


pul = Entry(root)

L2 = Label(root,text="pulmonary tb or not")
L2.grid(row=1, column=0, sticky=N+S+E+W)
pul.grid(row=1, column=1, sticky=N+S+E+W)


ptype = Entry(root)

L3 = Label(root,text="Patient Type")
L3.grid(row=2, column=0, sticky=N+S+E+W)
ptype.grid(row=2, column=1, sticky=N+S+E+W)



sr = Entry(root)

L4 = Label(root,text="Sputum result")
L4.grid(row=3, column=0, sticky=N+S+E+W)
sr.grid(row=3, column=1, sticky=N+S+E+W)


hiv = Entry(root)

L5 = Label(root,text="HIV status")
L5.grid(row=4, column=0, sticky=N+S+E+W)
hiv.grid(row=4, column=1, sticky=N+S+E+W)



endip = Entry(root)

L6 = Label(root,text="EndIP result")
L6.grid(row=5, column=0, sticky=N+S+E+W)
endip.grid(row=5, column=1, sticky=N+S+E+W)


extip = Entry(root)

L7 = Label(root,text="ExtIP result")
L7.grid(row=6, column=0, sticky=N+S+E+W)
extip.grid(row=6, column=1, sticky=N+S+E+W)


age = Entry(root)

L8 = Label(root,text="Age")
L8.grid(row=7, column=0, sticky=N+S+E+W)
age.grid(row=7, column=1, sticky=N+S+E+W)





gender.focus_set()




b = Button(root,text='submit',command=printtext)
b.grid(row=8, column=0, sticky=E+W)


p = Button(root, text="prepare data", command=prepare_data).grid(row=9, column=0, sticky=N+S+E+W)


r = Button(root, text="run model", command=run_model).grid(row=10, column=0, sticky=N+S+E+W)


q = Button(root, text="Quit", command=root.destroy).grid(row=11, column=0, sticky=N+S+E+W)


text = Text(root)
text.insert(INSERT, "Welcome to the Early Case-Severity Warning System Software \n\n")
text.insert(INSERT, "Developed by route2sabya for CEPT M.Tech Geomatics\n\n")
text.insert(INSERT, "The software predicts case severity of tuberculosis patients and assigns priority \n\n")
text.insert(INSERT, "You can use this region to save results from the interpreter\n\n")



text.insert(END,'================Add results here================')
text.grid(row=12, column=1, sticky=N+S+E+W)



root.mainloop()
