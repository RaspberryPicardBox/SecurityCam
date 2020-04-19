# SecurityCam
A Python3 based security camera script using OpenCV.

# Features
When motion is detected, snapshots are taken using the devices camera, and automatically uploaded to Google Drive cloud. When there are too many, they snapshot-deleter searches out and deltes any created images, leaving a nice clean root directory.

Note: Images are stored in the root directory of your Google Drive account - it is recommended you use an empty Drive, as things can fill up fast and deletion may cause issues with other files!

Requires OpenCV-python, Numpy and Pydrive.

Credit for the insipration for this code goes to Adrian Rosebrock. A link to their original tutorial can be found here: https://www.pyimagesearch.com/2015/06/01/home-surveillance-and-motion-detection-with-the-raspberry-pi-python-and-opencv/
