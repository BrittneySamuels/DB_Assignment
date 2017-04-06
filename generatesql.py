'''

Description: Script for generating database sql file
Created By: Andre Vidal
Date: 20-March-2017
Purpose: Database Project

'''

import names #library to randomly generate names
import random #library to generate random numbers

DB_NAME = "PMH_DB"

CITIES = ["HANDALE","BLOOMFIELD","RIVERRUN","PORTMORE","MANDEVILLE","MONTEGO_BAY","NEW_YORK","MANHATTAN","LONDON", "CHURCH HILL", "GENOVA", "TRANSILVANIA", "COPELAND", "WELLINGTON", "RODNEY", "SCOTT", "POWE", "VIDAL", "SAMUELS", "MOWATT","WALLACE"]
TOWNS = ["KINGSTOWN","ANDERSON","TREELANG","SEW BAY","MOUNTPORT","GREY TOWN","SANDY PEAK","MAROON_TOWN","PORT ANTONIO","BUFF BAY", "PORT MARIA", "SPANISH TOWN", "QUEENS", "REDVILLE", "COPPER SHOT","BRIMINGHAM", "TANTAYLOR","CHANCELLARY","NORBROOK","TRANSMAN","STRONG", "RETIREMENT", "HAMVILLE", "JOHNS TOWN", "JONES TOWN", "CALABASH", "CALLALOO", "TAFARI"]
STREETS = ["SINGLE STREET","BROWN CRESCENT","SIMPLE LANE","RED ROAD","ANGEL CRESCENT","CARTOON DRIVE","STEW ROAD","COMPLEX STREET","HART STREET","LOONA DRIVE", "QUEENS", "BALVENIE", "HOPETON", "SANDAL", "HAPPY GROOVE", "LOGWOOD", "CHERRY", "COCONUT", "PINES", "DOVEWOOD", "CORKWOOD", "CANDLENUT", "PIMENTO","PRIMROSE", "BREADNUT", "CEDAR", "SAGE", "JASMINE", "FIDDLEWOOD", "BREADFRUIT", "ALMOND", "ALAMANDA", "PRIMROSE"]

SPECIALIZATION = ["CARDIOLOGY","OBSTETRICS","GYNAECOLOGY","PEDIATRIC","RADIOLOGY","ONCOLOGY", "GASTROLOGY", "PULMONOLOGY", "ENDOCRINOLOGY", "NEPHROLOGY", "RHEUMATOLOGY", "PUBLIC HEALTH", "GERIATRICS" "INTENSIVE CARE MEDICINE", "GENERAL PRACTITIONER"]

TEST_RESULTS = ["Inconclusive","Bone Scan result"]
TEST_NAMES = ["ABO Blood Typing","Acoustic Reflex Test","HIV Test","Abdominal MRI","Arthrogram (Joint X-ray)","Biopsy, Bone Marrow","Blood Lead Level","Bone Scan","Body Temprature","CAT Scan, Body","Cardiac Blood Pool Scan","Kidney Biopsy","Knee MRI","Hepatitis A Virus Test","Hepatitis B Virus Test","Jaw X-ray","X-ray","Serum Osmolality Level","Scrotal Scan","Lung Scan"]

DIAGNOSES = {"ALZH":"Alzheimers",
			 "A00": "Intestinal infectious diseases",
			 "A15": "Tuberculosis",
			 "A20": "Certain zoonotic bacterial diseases",
			 "A30": "Other bacterial diseases",
			 "A50": "Infections with a predominantly sexual mode of transmission",
			 "A65": "Other spirochetal diseases",
			 "A70": "Other diseases caused by chlamydiae",
			 "A75": "Rickettsioses",
			 "A80": "Viral and prion infections of the central nervous system",
			 "A90": "Arthropod-borne viral fevers and viral hemorrhagic fevers",
			 "B00": "Viral infections characterized by skin and mucous membrane lesions",
			 "B10": "Other human herpesviruses",
			 "B15": "Viral hepatitis",
			 "B20": "Human immunodeficiency virus [HIV] disease",
			 "B25": "Other viral diseases",
			 "B35": "Mycoses",
			 "B50": "Protozoal diseases",
			 "B65": "Helminthiases",
			 "B85": "Pediculosis, acariasis and other infestations"}

MEDICINES = {"A047":"Bontril slow release 105mg",
			"A":"Desoxyn 5mg",
			"B":"Asprine enteric coated 325mg",
			"A08":"Mirtazapine 15mg",
			"A07": "Citalopram 40 mg",
			"A09": "Mirtazapine 30 mg",
			"A01": "Simvastatin 20 mg",
			"A03": "Simvastatin 40 mg",
			"A04": "Simvastatin 80 mg",
			"A056": "Phrenilin forte acetaminophen 650 mg/butalbital 50 mg",
			"A062": "Methscopolamine bromide 5 mg",
			"B29": "levlite inert",
			"B300": "Diltiazem hydrochloride extended-release 300 mg",
			"b332": "Velivet desogestrel 0.125 mg / ethinyl estradiol 0.025 mg",
			"b334": "Caziant inert",
			"b342": "Aranelle ethinyl estradiol 0.035 mg / norethindrone 1 mg",
			"B360": "Cardizem LA 360 mg",
			"B474": "Estradiol and Norethindrone 1 mg / 0.5 mg",
			"b50": "Ziac 5 mg / 6.25 mg",
			"C": "Myfortic 180 mg",
			"C01": "Risperidone (orally disintegrating) 0.5 mg",
			"C02": "Risperidone (orally disintegrating) 1 mg",
			"C04": "Fluconazole 50 mg",
			"C05": "Fluconazole 100 mg",
			"C103": "Salsalate 500 mg",
			"C112": "Finasteride 1 mg",
			"C402": "Tiagabine hydrochloride 2 mg",
			}

PROCEDURES = {
			  "X0": "Central Nervous System",
			  "Y1": "Peripheral Nervous System",
			  "F2": "Heart and Great Vessels",
			  "E3": "Upper Arteries",
			  "G4": "Lower Arteries",
			  "H5": "Upper Veins",
			  "H6": "Lower Veins",
			  "H7": "Lymphatic and Hemic Systems",
			  "H8": "Eye",
			  "0F": "Ear, Nose, Sinus",
			  "0B": "Respiratory System",
			  "0C": "Mouth and Throat",
			  "C0": "Central Nervous System",
			  "C2": "Heart",
			  "C5": "Veins",
			  "D0": "Pregnancy",
			  "C7": "Lymphatic and Hematologic System",
			  "C8": "Eye",
			  "C9": "Ear, Nose, Mouth and Throat",
			  "CB": "Respiratory System",
			  "CD": "Gastrointestinal System",
			  "CF": "Hepatobiliary System and Pancreas",
			  "CG": "Endocrine System",
			  "CH": "Skin, Subcutaneous Tissue and Breast",
			  "7W": "Anatomical Regions",
			  "3O": "Circulatory",
			  "3C": "Indwelling Device",
			  "3E": "Physiological Systems and Anatomical Regions"

			  }

ALLERGY_SEVERITY = ['mild','moderate','severe']

RELATIVE_TYPES = ['FATHER','MOTHER','MOTHER_FATHER','MOTHER_MOTHER','FATHER_FATHER','FATHER_MOTHER','BROTHER','SISTER']

MED_DOSAGES =  ['once a day','twice a day','thrice a day']


Nurses = []
Doctors = []
Secretaries = []
Patients = []
Tests = []
Diags = []

#PARAMETERS : (table_name,[(attr1,data_type,size),...],primary_attr,reference (attr,ref_table,ref_attr))
def create_table(table_name,attributes,primary,references):
	text = "CREATE TABLE "+table_name+"(\n\t"
	for i in range(0,len(attributes)):
		if attributes[i][1] == "varchar": 
			text += attributes[i][0]+" "+attributes[i][1]+"("+str(attributes[i][2])+"),\n\t"
		elif attributes[i][1] == "int" or attributes[i][1] == "datetime":
			text += attributes[i][0]+" "+attributes[i][1]+",\n\t"
		elif attributes[i][1] == "decimal":
			text += attributes[i][0]+" "+attributes[i][1]+"("+str(attributes[i][2][0])+","+str(attributes[i][2][1])+"),\n\t"

	if len(references) > 0:
		for j in range(0,len(references)):
			text += "\n\tFOREIGN KEY("+references[j][0]+") REFERENCES "+references[j][1]+"("+references[j][2]+") ON DELETE CASCADE ON UPDATE CASCADE,"

	text += "\n\tPRIMARY KEY("+primary+"),"

	text = text[0:-1]
	text += "\n);"
	text+= "\n\n"
	return text

#PARAMETERS : (tablename,[attr1,attr2,attr3,...])
def populate_table(table_name,attributes):
	text = "\nINSERT INTO "+table_name+" values ('"+attributes[0]+"'"
	for i in range(1,len(attributes)):
		try:
			float(attributes[i])
			text+= ", "+attributes[i]
		except ValueError:
			try:
				int(attributes[i])
				text+= ", "+attributes[i]
			except ValueError:
				text+= ", '"+attributes[i]+"'"

	text+= ");"
	return text;


def comment_multi_line(text):
	return "\n\n/*"+text+"*/\n"


def comment_single_line(text):
	return "#"+text+"\n"


def main():
	#SETTING UP DATABASE
	print "creating database...\n"
	filetext = comment_multi_line("DROPPING DATABASE")
	filetext+= "DROP DATABASE IF EXISTS "+DB_NAME+";\n"
	filetext+= comment_multi_line("CREATING DATABASE")
	filetext+= "CREATE DATABASE "+DB_NAME+";"
	filetext+= comment_multi_line("USE DATABASE")
	filetext+= "USE "+DB_NAME+";"
	filetext+= comment_multi_line("=============CREATING TABLES=============")
	print "[COMPLETE]\n"
	#CREATING THE TABLES

	print "creating tables..."
	filetext+= comment_multi_line("NURSE RELATED TABLES")
	filetext+= create_table("Nurse",[("nur_id","varchar",10),("first_name","varchar",50),("last_name","varchar",50),("password","varchar",50),("nur_DOB","datetime","null")],"nur_id",[])
	filetext+= create_table("Registered_Nurse",[("nur_id","varchar",10),("first_name","varchar",50),("last_name","varchar",50),("nur_DOB","datetime","null")],"nur_id",[("nur_id","Nurse","nur_id")])
	filetext+= create_table("Enrolled_Nurse",[("nur_id","varchar",10),("first_name","varchar",50),("last_name","varchar",50),("nur_DOB","datetime","null")],"nur_id",[("nur_id","Nurse","nur_id")])
	filetext+= create_table("Midwife_Nurse",[("nur_id","varchar",10),("first_name","varchar",50),("last_name","varchar",50),("nur_DOB","datetime","null")],"nur_id",[("nur_id","Nurse","nur_id")])
	filetext+= create_table("Nurse_Address",[("nur_id","varchar",10),("address_line_1","varchar",50),("address_line_2","varchar",50),("address_line_3","varchar",50)],"nur_id",[("nur_id","Nurse","nur_id")])
	
	
	filetext+= comment_multi_line("SECRETARY TABLE")
	filetext+= create_table("Secretary",[("sec_id","varchar",10),("first_name","varchar",50),("last_name","varchar",50),("password","varchar",50)],"sec_id",[])
	
	
	filetext+= comment_multi_line("DOCTOR RELATED TABLES")
	filetext+= create_table("Doctor",[("doc_id","varchar",10),("first_name","varchar",50),("last_name","varchar",50),("password","varchar",50)],"doc_id",[])
	filetext+= create_table("Intern",[("doc_id","varchar",10),("first_name","varchar",50),("last_name","varchar",50),("start_date","datetime","null"),("end_date","datetime","null")],"doc_id",[("doc_id","Doctor","doc_id")])
	filetext+= create_table("Consultant",[("doc_id","varchar",10),("first_name","varchar",50),("last_name","varchar",50),("specialization","varchar",50)],"doc_id",[("doc_id","Doctor","doc_id")])
	filetext+= create_table("Resident",[("doc_id","varchar",10),("first_name","varchar",50),("last_name","varchar",50)],"doc_id",[("doc_id","Doctor","doc_id")])
	filetext+= create_table("Doctor_Address",[("doc_id","varchar",10),("address_line_1","varchar",50),("address_line_2","varchar",50),("address_line_3","varchar",50)],"doc_id",[("doc_id","Doctor","doc_id")])
	filetext+= create_table("Doctor_Contact",[("doc_id","varchar",10),("doc_number","int","null")],"doc_id",[("doc_id","Doctor","doc_id")])

	filetext+= comment_multi_line("PATIENT RELATED TABLES")
	filetext+= create_table("Patient",[("pat_id","varchar",10),("first_name","varchar",50),("last_name","varchar",50),("pat_DOB","datetime","null")],"pat_id",[])
	filetext+= create_table("Patient_Address",[("pat_id","varchar",10),("address_line_1","varchar",50),("address_line_2","varchar",50),("address_line_3","varchar",50)],"pat_id",[("pat_id","Patient","pat_id")])
	filetext+= create_table("Patient_Contact",[("pat_id","varchar",10),("pat_number","int","null")],"pat_id",[("pat_id","Patient","pat_id")])

	filetext+= comment_multi_line("OTHER TABLES")
	filetext+= create_table("Test",[("test_id","varchar",10),("test_name","varchar",100)],"test_id",[])
	filetext+= create_table("Diagnosis",[("diag_id","varchar",10),("diag_name","varchar",100)],"diag_id",[])
	filetext+= create_table("Medicine",[("med_id","varchar",10),("med_name","varchar",100)],"med_id",[])
	filetext+= create_table("Allergies",[("pat_id","varchar",10),("med_id","varchar",10),("severity","varchar",30)],"pat_id,med_id",[("pat_id","Patient","pat_id"),("med_id","Medicine","med_id")])
	filetext+= create_table("Procedure_",[("proc_id","varchar",10),("proc_name","varchar",100)],"proc_id",[])

	filetext+= create_table("Patient_Test",[("doc_id","varchar",10),("pat_id","varchar",10),("test_id","varchar",10),("test_result","varchar",100)],"doc_id,pat_id,test_id",[("doc_id","Doctor","doc_id"),("pat_id","Patient","pat_id"),("test_id","Test","test_id")])
	filetext+= create_table("Patient_Diagnosis",[("doc_id","varchar",10),("pat_id","varchar",10),("diag_id","varchar",10),("diag_date","datetime","null")],"doc_id,pat_id,diag_id",[("doc_id","Doctor","doc_id"),("pat_id","Patient","pat_id"),("diag_id","Diagnosis","diag_id")])
	filetext+= create_table("Patient_Medicine",[("doc_id","varchar",10),("pat_id","varchar",10),("med_id","varchar",10)],"doc_id,pat_id,med_id",[("doc_id","Doctor","doc_id"),("pat_id","Patient","pat_id"),("med_id","Medicine","med_id")])
	filetext+= create_table("Patient_Procedure",[("doc_id","varchar",10),("pat_id","varchar",10),("proc_id","varchar",10)],"doc_id,pat_id,proc_id",[("doc_id","Doctor","doc_id"),("pat_id","Patient","pat_id"),("proc_id","Procedure_","proc_id")])

	filetext+= create_table("Family_Med_History",[("pat_id","varchar",10),("relative_type","varchar",15),("diag_id","varchar",10)],"pat_id,relative_type,diag_id",[("pat_id","Patient","pat_id"),("diag_id","Diagnosis","diag_id")])
	filetext+= create_table("Daily_Updates",[("nur_id","varchar",10),("pat_id","varchar",10),("update_date","datetime","null"),("body_temp","decimal",(10,2)),("respir_rate","decimal",(10,2)),("pulse_rate","decimal",(10,2)),("blood_pressure","varchar",20),("med_id","varchar",10),("med_dosage","varchar",20)],"nur_id,pat_id,update_date",[("nur_id","Nurse","nur_id"),("pat_id","Patient","pat_id")])
	print "[COMPLETE]\n"
	#INSERTING INTO TABLES

	filetext+= "\n"

	filetext+= comment_single_line("========================================================================");
	filetext+= comment_single_line("===============================   NURSES   =============================");
	filetext+= comment_single_line("========================================================================");

	print "Populating Nurses..."
	for i in range(0,15):
		nurse = ["N0000"+str(i),names.get_first_name(),names.get_last_name(),str(random.randrange(1970,1990))+"-"+str(random.randrange(1,12))+"-"+str(random.randrange(1,28)),str(random.randrange(1,500))+" "+STREETS[random.randint(0,len(STREETS)-1)],TOWNS[random.randint(0,len(TOWNS)-1)],CITIES[random.randint(0,len(CITIES)-1)]]
		Nurses.append(nurse)
		filetext+= populate_table("Nurse",[nurse[0],nurse[1],nurse[2],nurse[0]+nurse[1][0]+nurse[2][0],nurse[3]])
		filetext+= populate_table("Registered_Nurse",[nurse[0],nurse[1],nurse[2],nurse[3]])
	
	filetext+= "\n"
	
	for i in range(15,30):
		nurse = ["N0000"+str(i),names.get_first_name(),names.get_last_name(),str(random.randrange(1970,1990))+"-"+str(random.randrange(1,12))+"-"+str(random.randrange(1,28)),str(random.randrange(1,500))+" "+STREETS[random.randint(0,len(STREETS)-1)],TOWNS[random.randint(0,len(TOWNS)-1)],CITIES[random.randint(0,len(CITIES)-1)]]
		Nurses.append(nurse)
		filetext+= populate_table("Nurse",[nurse[0],nurse[1],nurse[2],nurse[0]+nurse[1][0]+nurse[2][0],nurse[3]])
		filetext+= populate_table("Enrolled_Nurse",[nurse[0],nurse[1],nurse[2],nurse[3]])
	
	filetext+= "\n"

	for i in range(30,45):
		nurse = ["N0000"+str(i),names.get_first_name(),names.get_last_name(),str(random.randrange(1970,1990))+"-"+str(random.randrange(1,12))+"-"+str(random.randrange(1,28)),str(random.randrange(1,500))+" "+STREETS[random.randint(0,len(STREETS)-1)],TOWNS[random.randint(0,len(TOWNS)-1)],CITIES[random.randint(0,len(CITIES)-1)]]
		Nurses.append(nurse)
		filetext+= populate_table("Nurse",[nurse[0],nurse[1],nurse[2],nurse[0]+nurse[1][0]+nurse[2][0],nurse[3]])
		filetext+= populate_table("Midwife_Nurse",[nurse[0],nurse[1],nurse[2],nurse[3]])
	
	filetext+= "\n"

	for i in range(0,len(Nurses)):
		filetext+= populate_table("Nurse_Address",[Nurses[i][0],Nurses[i][4],Nurses[i][5],Nurses[i][6]])

	filetext+= "\n"

	for i in range(0,15):
		sec = ["S0000"+str(i),names.get_first_name(),names.get_last_name()]
		Secretaries.append(sec)
		filetext+= populate_table("Secretary",[sec[0],sec[1],sec[2],sec[0]+sec[1][0]+sec[2][0]])
		
	filetext+= "\n\n"

	print "[COMPLETE]\n"

	filetext+= comment_single_line("========================================================================");
	filetext+= comment_single_line("=============================   DOCTORS  ===============================");
	filetext+= comment_single_line("========================================================================");

	print "Populating Doctors..."
	for i in range(0,10):
		doctor = ["D0000"+str(i),names.get_first_name(),names.get_last_name(),str(random.randrange(2014,2015))+"-"+str(random.randrange(1,12))+"-"+str(random.randrange(1,28)),str(random.randrange(2017,2018))+"-"+str(random.randrange(1,12))+"-"+str(random.randrange(1,28)),str(random.randrange(1,500))+" "+STREETS[random.randint(0,len(STREETS)-1)],TOWNS[random.randint(0,len(TOWNS)-1)],CITIES[random.randint(0,len(CITIES)-1)],str(random.randint(1000000,9999999))]
		Doctors.append(doctor)
		filetext+= populate_table("Doctor",[doctor[0],doctor[1],doctor[2],doctor[0]+doctor[1][0]+doctor[2][0]])
		filetext+= populate_table("Intern",[doctor[0],doctor[1],doctor[2],doctor[3],doctor[4]])
	
	filetext+= "\n"
	
	for i in range(10,20):
		doctor = ["D0000"+str(i),names.get_first_name(),names.get_last_name(),SPECIALIZATION[random.randint(0,len(SPECIALIZATION)-1)],"",str(random.randrange(1,500))+" "+STREETS[random.randint(0,len(STREETS)-1)],TOWNS[random.randint(0,len(TOWNS)-1)],CITIES[random.randint(0,len(CITIES)-1)],str(random.randint(1000000,9999999))]
		Doctors.append(doctor)
		filetext+= populate_table("Doctor",[doctor[0],doctor[1],doctor[2],doctor[0]+doctor[1][0]+doctor[2][0]])
		filetext+= populate_table("Consultant",[doctor[0],doctor[1],doctor[2],doctor[3]])
	
	filetext+= "\n"

	for i in range(20,30):
		doctor = ["D0000"+str(i),names.get_first_name(),names.get_last_name(),str(random.randrange(1940,2017))+"-"+str(random.randrange(1,12))+"-"+str(random.randrange(1,28)),"",str(random.randrange(1,500))+" "+STREETS[random.randint(0,len(STREETS)-1)],TOWNS[random.randint(0,len(TOWNS)-1)],CITIES[random.randint(0,len(CITIES)-1)],str(random.randint(1000000,9999999))]
		Doctors.append(doctor)
		filetext+= populate_table("Doctor",[doctor[0],doctor[1],doctor[2],doctor[0]+doctor[1][0]+doctor[2][0]])
		filetext+= populate_table("Resident",[doctor[0],doctor[1],doctor[2]])
	
	filetext+= "\n"

	for i in range(0,len(Doctors)):
		filetext+= populate_table("Doctor_Address",[Doctors[i][0],Doctors[i][5],Doctors[i][6],Doctors[i][7]])

	filetext+= "\n"

	for i in range(0,len(Doctors)):
		filetext+= populate_table("Doctor_Contact",[Doctors[i][0],Doctors[i][8]])


	filetext+= "\n\n"

	print "[COMPLETE]\n"
	filetext+= comment_single_line("========================================================================");
	filetext+= comment_single_line("=============================   PATIENTS   =============================");
	filetext+= comment_single_line("========================================================================");

	print "Populating Patients..."
	for i in range(0,500010):
		Patients.append(["P000"+str(i),names.get_first_name(),names.get_last_name(),str(random.randrange(1940,2017))+"-"+str(random.randrange(1,12))+"-"+str(random.randrange(1,28)),str(random.randrange(1,500))+" "+STREETS[random.randint(0,len(STREETS)-1)],TOWNS[random.randint(0,len(TOWNS)-1)],CITIES[random.randint(0,len(CITIES)-1)],str(random.randint(1000000,9999999))])
		filetext+= populate_table("Patient",[Patients[i][0],Patients[i][1],Patients[i][2],Patients[i][3]])
		#print i
	
	filetext+= "\n"

	for i in range(0,len(Patients)):
		filetext+= populate_table("Patient_Address",[Patients[i][0],Patients[i][4],Patients[i][5],Patients[i][6]])

	filetext+= "\n"

	for i in range(0,len(Patients)):
		filetext+= populate_table("Patient_Contact",[Patients[i][0],Patients[i][7]])


	print "[COMPLETE]\n"

	filetext+= "\n\n"

	filetext+= comment_single_line("========================================================================");
	filetext+= comment_single_line("===========================   OTHER TABLES   ===========================");
	filetext+= comment_single_line("========================================================================");

	print "Populating Other Tables [Tests]..."
	for i in range(0,5000):
		test = ["T0000"+str(i),TEST_NAMES[random.randint(0,len(TEST_NAMES)-1)]]
		Tests.append(test)
		filetext+= populate_table("Test",[test[0],test[1]])
	
	filetext+= "\n"

	print "[COMPLETE]\nPopulating Other Tables [Diagnoses]..."
	DIAG_KEYS = DIAGNOSES.keys()#GET LIST OF DIAGNOSIS KEYS
	for key in DIAG_KEYS:
		filetext+= populate_table("Diagnosis",[key,DIAGNOSES[key]])
	
	filetext+= "\n"

	print "[COMPLETE]\nPopulating Other Tables [Medicines]..."
	MED_KEYS = MEDICINES.keys()#GET LIST OF DIAGNOSIS KEYS
	for key in MED_KEYS:
		filetext+= populate_table("Medicine",[key,MEDICINES[key]])
	
	filetext+= "\n"

	print "[COMPLETE]\nPopulating Other Tables [Allergies]..."
	patient_sample = random.sample(xrange(len(Patients)),len(Patients)/2)
	for p in patient_sample:
		#print MEDICINES[MED_KEYS[random.randint(0,len(MED_KEYS)-1)]], Patients[p]
		filetext+= populate_table("Allergies",[Patients[p][0],MED_KEYS[random.randint(0,len(MED_KEYS)-1)],ALLERGY_SEVERITY[random.randint(0,len(ALLERGY_SEVERITY)-1)]])


	filetext+= "\n"

	print "[COMPLETE]\nPopulating Other Tables [Procedures]..."
	PROC_KEYS = PROCEDURES.keys()#GET LIST OF DIAGNOSIS KEYS
	for key in PROC_KEYS:
		filetext+= populate_table("Procedure_",[key,PROCEDURES[key]])
	
	filetext+= "\n"


	print "[COMPLETE]\nPopulating Other Tables [Family History]..."
	for i in range(0,len(Patients)):
		relatives_sample = random.sample(xrange(len(RELATIVE_TYPES)),len(RELATIVE_TYPES))
		diagnosis_sample = random.sample(xrange(len(DIAGNOSES)),len(DIAGNOSES))

		for j in range(0,random.randint(0,len(RELATIVE_TYPES)/2)):
			#print RELATIVE_TYPES[int(relatives_sample[j])],DIAGNOSES[DIAG_KEYS[int(diagnosis_sample[j])]]
			filetext+= populate_table("Family_Med_History",[Patients[i][0],RELATIVE_TYPES[int(relatives_sample[j])],DIAG_KEYS[int(diagnosis_sample[j])]])

	filetext+= "\n"

	print "[COMPLETE]\nPopulating Other Tables [Patient Tests]..."
	for t in Tests:
		filetext+= populate_table("Patient_Test",[Doctors[random.randint(0,len(Doctors)-1)][0],Patients[random.randint(0,len(Patients)-1)][0],t[0],TEST_RESULTS[random.randint(0,len(TEST_RESULTS)-1)]])

	filetext+= "\n"
	
	print "[COMPLETE]\nPopulating Other Tables [Patient Diagnosis]..."
	diag_entries=[]
	for i in range(0,5000):
		doctor = Doctors[random.randint(0,len(Doctors)-1)][0]
		patient = Patients[random.randint(0,len(Patients)-1)][0]
		diag = DIAG_KEYS[random.randint(0,len(DIAG_KEYS)-1)]
		diag_date = str(random.randrange(1990,2015))+"-"+str(random.randrange(1,12))+"-"+str(random.randrange(1,28))
		entry = (doctor,patient,diag,diag_date)
		if entry not in diag_entries:
			diag_entries += [entry]
			filetext+= populate_table("Patient_Diagnosis",[entry[0],entry[1],entry[2],entry[3]])

	filetext+= "\n"
	
	print "[COMPLETE]\nPopulating Other Tables [Patient Medicine]..."
	med_entries=[]
	for i in range(0,5000):
		doctor = Doctors[random.randint(0,len(Doctors)-1)][0]
		patient = Patients[random.randint(0,len(Patients)-1)][0]
		med = MED_KEYS[random.randint(0,len(MED_KEYS)-1)]
		entry = (doctor,patient,med)
		if entry not in med_entries:
			med_entries += [entry]
			filetext+= populate_table("Patient_Medicine",[entry[0],entry[1],entry[2]])

	filetext+= "\n"
	
	print "[COMPLETE]\nPopulating Other Tables [Patient Procedure]..."
	proc_entries=[]
	for i in range(0,5000):
		doctor = Doctors[random.randint(0,len(Doctors)-1)][0]
		patient = Patients[random.randint(0,len(Patients)-1)][0]
		proc = PROC_KEYS[random.randint(0,len(PROC_KEYS)-1)]
		entry = (doctor,patient,proc)
		
		if entry not in proc_entries:
			proc_entries += [entry]
			filetext+= populate_table("Patient_Procedure",[entry[0],entry[1],entry[2]])


	filetext+= "\n"
	
	print "[COMPLETE]\nPopulating Other Tables [Daily Updates]..."
	for p in Patients:
		temp_day = random.randint(1,20)
		temp_month = random.randint(1,12)
		temp_year = random.randint(1990,2016)
		for day in range (temp_day,temp_day+random.randint(3,5)):
			nurse = Nurses[random.randint(0,len(Nurses)-1)][0]
			body_temp = str(round(random.uniform(92,105),2))
			respir_rate = str(round(random.uniform(10,100),2))
			pulse_rate = str(round(random.uniform(10,180),2))
			blood_pressure = str(round(random.uniform(50,180),2)) + " over " + str(round(random.uniform(40,110)))
			med_id = MED_KEYS[random.randint(0,len(MED_KEYS)-1)] 
			med_dosage = MED_DOSAGES[random.randint(0,len(MED_DOSAGES)-1)] 
			filetext+= populate_table("Daily_Updates",[nurse,p[0],str(temp_year)+"-"+str(temp_month)+"-"+str(day),body_temp,respir_rate,pulse_rate,blood_pressure,med_id,med_dosage])


	print "[COMPLETE]\n"
	print "*========FINISHED========*"

	f=open("pmh_db_file.sql","w+")
	f.write(filetext)
	f.close()


if __name__ == "__main__":
    main()