# firebase_config.py
import firebase_admin
from firebase_admin import credentials, storage, db

cred = credentials.Certificate('firebasekey.json')  # path to your service key

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://socialfb-97a80-default-rtdb.firebaseio.com/',
    'storageBucket': 'socialfb-97a80.appspot.com'  # ✅ Add your storage bucket here
})

bucket = storage.bucket()
