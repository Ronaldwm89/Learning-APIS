# ISS Overhead Notifier 🚀 
This Python script sends an email notification when the International Space Station (ISS) is passing over your location at night. It uses APIs to fetch the ISS position and sunrise/sunset times to determine visibility.

 ## Features - 
 **ISS Location Tracking:** Fetches the current location of the ISS. - 
 **Sunrise/Sunset Detection:** Determines if it's night based on local sunrise/sunset times. - 
 **Email Notifications:** Sends an email alert when the ISS is visible from your location. 
 
 ## How to Use 
 1. Clone this repository. 
 2. Install required packages: `requests`, `datetime`, `smtplib`, `time`. 
 3. Update `MY_LAT`, `MY_LONG`, `E_MAIL`, and `PASSWORD` with your details. 
 4. Run `conditionals_true()` to start the script. 
 
 ## Dependencies 
 - `requests` 
 - `datetime` 
 - `smtplib` 
 - `time` 