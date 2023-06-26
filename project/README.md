# NMAP AND LOCATION
#### Video Demo:  <https://youtu.be/CWaUcNbfqrg>
[![Video Demo:](https://i9.ytimg.com/vi/CWaUcNbfqrg/mq2.jpg?sqp=CICUyJwG-oaymwEmCMACELQB8quKqQMa8AEB-AHUBoAC4AOKAgwIABABGDMgZShXMA8%3D&rs=AOn4CLBE8jUfXp_McJGXQ3aAj9ysK5IuuA&retry=3)](https://youtu.be/CWaUcNbfqrg)
#### Description:

![image](https://github.com/code50/38144008/blob/main/project/images/image_1.png)

Nmap and Location is a code based in Python 3.10 where you can evaluate if exist ports and service active in your server using your Ip public address. After that you can check as well the location about specific server using API application programming Interface.

![image](https://github.com/code50/38144008/blob/main/project/images/image_2.png)

#### File project.py:
In this file you can see all the code generated. I am using three function as a core.
# get_interface()
Permit show an interface to the customer and also evaluate if the ip address is correct.
# get_nmap_scanner():
Permit scan all the ports tcp in a range 1-9090 as well I am using the argument -Pn in order to not send request icmp to my target, if you want to validate you can usea awireshark to see this flow of packets.
# get_location():
Permit send the location providing latitud and longitud using Application Programming Interface API. I declarate the API Key in the file test_project.py with the finality if someone want to test the code.


#### File test_project.py:
In this file exist code in order to test all the behivor if the user insert incorrect value what happend in the code. As well I tested if the user insert a correct value what is the result final.


![image](https://github.com/code50/38144008/blob/main/project/images/image_3.png)
#### File requirements.txt:
If you want to run this project in your machine on cloud or in site. You can see all the detail in the file requirements.txt where specify all the library and versions.

