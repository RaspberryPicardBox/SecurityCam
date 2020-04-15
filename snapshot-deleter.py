from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

drive = GoogleDrive(gauth)

print("Load complete!")

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
print("Starting process...")
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
  if "Snapshot" in file1['title']:
        print("Found a Snapshot File. Deleting...")
        file1.Delete()
print("Done!")
