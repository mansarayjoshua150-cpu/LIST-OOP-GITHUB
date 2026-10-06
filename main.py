#patient class
class patient:
    def __init__(self, name, ID, patient_id, age, gender, diagnosis):
        self.name = name
        self.patient_id = patient_id
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

    def display_info(self):
            print("\n***** patient information ******")
            print(f"ID: {self.patient_id}")
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Gender: {self.gender}")
            print(f"Diagnosis: {self.diagnosis}")

            # Hospital class
class Hospital :
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name

        self.patient = []

    def add_patient(self, patient):
        self.patient,append(patient)
        print("patient added successfully")

    def display_patient(self):
        print(f"n\********** All Patients *************")
 print(f"\n ***** {self.hospital_name}******")


 #check if there are patient
 if len(self.patient) == 0:
    print("No Patient Records Found.")
    else:
        for patient in sef.patient:
            patient.display_info()

        
        #patient Objects
        patient1 = patient(101, "saidu", 23, "Male", "poverty")
        patient2 = patient(102, "Abu Turay", 30, "Male", "Malaria")
        patient3 = patient(103, "Yabom Turay", 21, "Female", "Headacher")

        #Hospital Object
        hospital = Hospital("Donald Clinic")
#Add patient to the hospital using the add_patient method in the hospital class
        hospital.add_patient(patient1)
        hospital.add_patient(patient2)
        hospital.add_patient(patient3)

        #Display all patient records in the hospital
 hospital.display_patient()




