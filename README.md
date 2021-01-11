# SYSTEM HEALTH CHECK AUTOMATION
This python script is supposed to check for basic system errors like if the disk is nearly full or if the C.P.U usage is too high etc.
This was accomplished using given python modules and functions

1. psutil.cpu_percent(interval=None, percpu=False)

2. psutil.virtual_memory()

3. shutil.disk_usage() 
 
4. smtplib

![Figure 4.1](/images/Screenshot%202020-11-15%20195444.jpg)
 
The basic working of the program is shown in the flowchart (fig. 4.1).
The format of the error report in shown in figure 4.2

 ![Figure 4.2](/images/Screenshot%202020-11-15%20133335.jpg)


The emails sent by the program when the errors were encountered are shown in figure 4.3 

 

 ![Figure 4.3](/images/Screenshot%202020-11-15%20133124.jpg)


If this scripts finds and error but for some reasons unable to send mail then a message pops up on screen saying “FAILED TO SEND ERROR REPORT”. This is shown in figure 4.4

 
![Figure 4.4](/images/Screenshot%202020-11-15%20135900.jpg)


This mail is sent via Gmail servers but all other mail servers can be added.

 
![Figure 4.5](/images/Screenshot%202020-11-15%20133425.jpg)

In the figure 4.5, the sender_email_id and password should be entered. Sender’s account means the mail id through which the report is to be sent.
Receiver_email_id should have the mail id of person to whom the report generated is to be sent.

###Updated
Added an feature that will maintain a log file of all actions when the program is executed.
