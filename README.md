# bme590hrm 
Calculates the instantaneous heart rate, average heart rate, input time interval, and also indicates conditions like Bradycardia and Tachycardia for the window size selected. <br />
The output also includes the total number of requests made to the service.


The Software License for the file is:
=========
LICENSE.md ( MIT License)

The Travis Badge is:
=========
[![Build Status](https://travis-ci.org/MounikaVanka/bme590hrm.svg?branch=master)](https://travis-ci.org/MounikaVanka/bme590hrm)

Read the Docs Badge:
=========
<a href='http://bmehrmproject.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/bmehrmproject/badge/?version=latest' alt='Documentation Status' />
</a>   


Starting the Program
=========
The program may be started by posting the following inputs for Average Heart Rate and Instantaneous heart rate respectively on the web server:
1. POST/api/heart_rate/summary <br />
http://vcm-1612.vm.duke.edu:5000/heart_rate/summary
2. POST/api/heart_rate/average <br />
http://vcm-1612.vm.duke.edu:5000/heart_rate/average
3. GET/api/requests <br />
The address to the Virtual Machine requests is:
http://vcm-1612.vm.duke.edu:5000/requests


Requirements:
=========
Python 3.6

Input parameters:

FOR INSTANTANEOUS HEART RATE: 

{ <br />
    "time": [1, 2, 3, ...],      
    "voltage": [20, 1, 20, 14, ...]  
} 

FOR AVERAGE HEART RATE: 

{ <br />
    "averaging_period": 20, <br />
    "time": [1, 2, 3, ...], <br />
    "voltage": [100, 60, 62, ...]  <br />
} <br />
  


Output
=========
The output for the Instantaneous Heart Rate with the HR and Tachy and Brady cardia vectors is in the following form:

{ <br />
    "time": [1, 2, 3, ...], <br />
    "instantaneous_heart_rate": [100, 60, 62, ...], <br />
    "tachycardia_annotations": [true, false, true, ...], <br />
    "bradycardia_annotations": [true, false, true, ...] <br />
} <br />

The output for the Average Heart Rate with the Avg HR, Brady and Tachcardia vectors is in the following form:

{ <br />
    "time": [1, 2, 3, ...], <br />
    "averaging_period": 20, <br />
    "instantaneous_heart_rate": [100, 60, 62, ...], <br />
    "tachycardia_annotations": [true, false, true, ...], <br />
    "bradycardia_annotations": [true, false, true, ...] <br />
} <br />



Unit Testing
=========
Unit testing is performed using py.test by running test_hrm.py.

Team Members:
======
+ Caleb Willis
+ Tim Hoer
+ Mounika Vanka


Credits
=======
* Mark Palmeri
* Suyash Kumar
* Arjun Desai


