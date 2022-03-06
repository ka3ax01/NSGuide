
import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyBj4VfUwExEDr0tY5SdGB_i_HjjTY2i7mk",
  'authDomain': "nsguide-2032a.firebaseapp.com",
  "databaseURL": "xxxxxx",
  'projectId': "nsguide-2032a",
  'storageBucket': "nsguide-2032a.appspot.com",
  'serviceAccount': "serviceAcckey.json",
  'messagingSenderId': "282807297559",
  'appId': "1:282807297559:web:874dab59d48259fb789e52",
  'measurementId': "G-84N06KEE4X"
};
        
firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
storage = firebase.storage()



# =============================================================================
# email = input("Enter your email: ")
# password = input("Enter your password: ")
# 
# try:
#     auth.sign_in_with_email_and_password(email,password)
#     print("Successfully sign in")
# except:
#     print("Failed to sign in")
#     
# =============================================================================
# =============================================================================
# try:
#  
#     storage.child("Data/Baiterek/51.jpg").download("dfasa.jpg","dfasa.jpg")
# except:
#     print('~~~Download Failed~~~')
# 
# =============================================================================
it = 0
all_files = storage.child("Data").list_files()    
for file in all_files:
    it = it +1
           
    try:
        print(file.name)
        print(it)
        #Option 1: Fail
        #storage.child(file.name).download(""+it+".jpg")
        #Option 2: Fail
        #file.dwonload_to_filename(file.name)
        #Option 3: Fail
        storage.child(file.name).download("/...", ""+it+".jpg")
        #Option 4: Fail
        #file.dwonload_to_filename("/...",file.name)
    
    except:    
        print('~~~Download Failed~~~') 

# =============================================================================
# a = storage.child("Data/Baiterek/88.jpg").download("/...","dfasdaa.jpg")
# print(a)
# =============================================================================
