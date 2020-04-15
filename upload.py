from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from PIL import Image
import os
import io

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': 'image', 'mimeType':'image/jpeg'})
file1.SetContentFile("image.jpg")
file1.Upload()

