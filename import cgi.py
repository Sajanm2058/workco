import cgi
from base64 import b64encode
import face_recognition
formData = cgi.FieldStorage()
face_match = 0
image = formData.getvalue("current_image")
email = formData.getvalue("email")
data_uri = image
header, encoded = data_uri.split(",",1)
data = b64encode(encoded)
with open("image.png", "wb") as f:
    f.write(data)
got_image = face_recognition.load_image_file("image.png")
existing_image = face_recognition.load_image_file("students/"+email+".jpg")
got_image_facialfeature = face_recognition.face_encoding(got_image)[0]
existing_image_facialfeature = face_recognition.face_encoding(existing_image)[0]
results = face_recognition.compare_faces([existing_image_facialfeature],got_image_facialfeature)
if(results[0]):
    face_match = 1
else:
    face_match = 0

print("Content_Type:text/html")
print()
if(face_match==1):
    print("<script>alert('welcome ",email," ')</script>")
else:
    print("<script>alert('face not recognized')</script>")