# Router modem testing over serial through SSH python program  

Python program for automated router modem testing over serial through SSH.  

Prerequisites:  
python 3.x  
python3-pip  
sudo pip install pyserial  
sudo pip install paramiko  

Usage:  
python3 main.py -D {DEVICE NAME}  

Configuration file  
File has to be named config.json and has to be in the same dir as main.py .  
Example:

{  
    "product": [  
        {  
            "name": "TRM240", ## Poduct name  
            "config": {  
                "type":"serial",  ## Connection type serial/ssh  
                "baudrate": "115200", ## Connection baudrate (only for serial)  
                "device": "/dev/ttyUSB2" ## Device connect to (only for serial)  
            },  
            "cmd_list": [ ## Commands list to send to device  
                {  
                    "cmd": "ATI", ## Command  
                    "result": "OK", ## Expected result from command  
                    "args": "" ## Command arguments   
                },  
                {  
                    "cmd": "AT+GMR",  
                    "result":"OK",  
                    "args": ""  
                }  
            ]  
        },  
        {  
            "name": "RUTX11",  
            "config": {  
                "type":"ssh",  
                "ip": "192.168.1.1", ## Device connection IP (for  ssh only)  
                "port": "22", ## Device connection port (ssh only)    
                "username": "root", ## Device connection username  
                "password": "admin01" ## Device connection password  
            },  
            "cmd_list": [  
                {  
                    "cmd": "ATI",  
                    "result": "OK",  
                    "args": ""  
                },  
                {  
                    "cmd": "AT+GMR",  
                    "result":"OK",  
                    "args": ""  
                }  
            ]  
        }  
    ]  
}  

