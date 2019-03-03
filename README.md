
# Data-Analytics-Service-Project-for-COMP9321
===============================
Workflow
-----------
1.FIND DATASET

2.DATA CLEANSING

3.API

3.BUILD FRONTEND

4.INTERACTING WITH FRONTEND AND BACKEND

SUMMARY
-----------
In this project, 
In order to help locate what kind of combination of App features will have more customers. 
we are going to predict how welcome of the Android app by giving some features that the upcoming app have,
the dataset is from https://www.kaggle.com/ which is the address of kaggle, we use K-nn module to train our dataset, although it may not very accurate, it still provide the brief estimation of how many installations will be achieved. 
In the beginning , we extract the data that we wanted from big dataset and clean it by using pandas module, after that, K-nn module been applied to train our data, we get our model which is named 'trained_module.cav' in above.
furthermore, for the better interaction, we develop a website for people who want to check which kind of combiation of app will have best installations.
In the web part, we implement simple authorization function ,you may not need to register but have to use username and password to login, you are allow to request data in a time slot,afer it expire,however,you have to re-login to request data .
for the interaction, we use the restful Api to interact with backend.

How to run
-----------
1. Open the backend appservice.py `python appservice.py`
it should look like below
![image text](https://github.com/US579/Data-Analytics-Service-Project-for-COMP9321/blob/master/image/1.png) 

and open index.html

![image text](https://github.com/US579/Data-Analytics-Service-Project-for-COMP9321/blob/master/image/2.png) 

and than you can login 

* username: admin

* password: admin

after login the interface are showing below

![image text](https://github.com/US579/Data-Analytics-Service-Project-for-COMP9321/blob/master/image/3.png) 

  
Interface controls
-------------------
 Input parameters to predict installations
![image text](https://github.com/US579/Data-Analytics-Service-Project-for-COMP9321/blob/master/image/4.png) 



