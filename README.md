# SYSTEM HEALTH CHECK AUTOMATION
This python script is supposed to check for basic system errors like if the disk is nearly full or if the C.P.U usage is too high etc.
This was accomplished using given python modules and functions

1. psutil.cpu_percent(interval=None, percpu=False)

Return a float representing the current system-wide CPU utilization as a percentage. When interval is > 0.0 compares system CPU times elapsed before and after the interval (blocking). When interval is 0.0 or None compares system CPU times elapsed since last call or module import, returning immediately. That means the first time this is called it will return a meaningless 0.0 value which you are supposed to ignore. In this case it is recommended for accuracy that this function be called with at least 0.1 seconds between calls. When percpu is True returns a list of floats representing the utilization as a percentage for each CPU. First element of the list refers to first CPU, second element to second CPU and so on. The order of the list is consistent across calls.


2. psutil.virtual_memory()

Return statistics about system memory usage as a named tuple including the following fields, expressed in bytes. Main metrics:

•	total: total physical memory (exclusive swap).
•	available: the memory that can be given instantly to processes without the system going into swap. This is calculated by summing different memory values depending on the platform and it is supposed to be used to monitor actual memory usage in a cross platform fashion.

3. shutil.disk_usage() 

This method tells the disk usage statistics about the given path as a named tuple with the attributes total, used and free where total represents total amount of memory, used represents used memory and free represents free memory.
 
4. smtplib

The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon. For details of SMTP and ESMTP operation, consult RFC 821 (Simple Mail Transfer Protocol) and RFC 1869 (SMTP Service Extensions).

class smtplib.SMTP(host='', port=0, local_hostname=None, [timeout, ]source_address=None)

An SMTP instance encapsulates an SMTP connection. It has methods that support a full repertoire of SMTP and ESMTP operations. If the optional host and port parameters are given, the SMTP connect() method is called with those parameters during initialization. If specified, local_hostname is used as the FQDN of the local host in the HELO/EHLO command. Otherwise, the local hostname is found using socket.getfqdn(). If the connect() call returns anything other than a success code, an SMTPConnectError is raised. The optional timeout parameter specifies a timeout in seconds for blocking operations like the connection attempt (if not specified, the global default timeout setting will be used). If the timeout expires, socket.timeout is raised. The optional source_address parameter allows binding to some specific source address in a machine with multiple network interfaces, and/or to some specific source TCP port. It takes a 2-tuple (host, port), for the socket to bind to as its source address before connecting. If omitted (or if host or port are '' and/or 0 respectively) the OS default behavior will be used.
 

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

