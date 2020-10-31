#! /usr/bin/env python3

import shutil
import psutil
import socket
import smtplib 
from datetime import datetime

def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage > 80

def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_available_memory():
    """available memory in linux-instance, in byte"""
    available_memory = psutil.virtual_memory().available/(1024*1024)
    return available_memory > 500

def check_localhost():
    """check localhost is correctly configured on 127.0.0.1"""
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'


if __name__ == "__main__":
    """"Running System Tests"""
    error_message = ""
    status = "Unhealthy"
    count = 1
    if check_cpu_usage():
        error_message += "{}. CPU usage is over 80%\n".format(count)
        count+=1
    if not check_disk_usage('/'):
        error_message += "{}. Available disk space is less than 20%\n".format(count)
        count+=1
    if not check_available_memory():
        error_message += "{}. Available memory is less than 500MB\n".format(count)
        count+=1
    if not check_localhost():
        error_message += "{}. localhost cannot be resolved to 127.0.0.1\n".format(count)
    if error_message == "":
        status = "Healthy"
    """ Sending Email if error is found"""
    if status == "Unhealthy":
        """ Gmail Server is used here """
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        sender_email_id= "Enter your mail id"
        password = "Enter Your Password"
        receiver_email_id= "Enter Receivers mail id"
        """getting time and date at which error was generated"""
        now = datetime.now()
        dt= now.strftime("%d-%B-%Y %H:%M:%S")
        d,t=dt.split()
        try:
            s.starttls() 
            s.login(sender_email_id, password)
            message = """
From : {}
To : {}
Subject : Errors encountered on your device
Date: {}
Time: {}

Your Device encountered the following errors.Please look into them as soon as possible
Errors: 
{}""".format(sender_email_id,receiver_email_id,d,t,error_message)
            s.sendmail(sender_email_id,receiver_email_id, message) 
            s.quit() 
        except:
            print("Error was found but mail could not be sent")
