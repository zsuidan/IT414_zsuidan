import psutil
import smtplib
import json
import time

#Creates a string displaying disk usage
volume_string = ""
volumes = psutil.disk_partitions()
for volume in volumes:
    volume_string += volume[1]
    volume_string += str(psutil.disk_usage(volume[1]))
    volume_string += "\n"

#Connects to mail server and sends messages
try:
    with open("text_files/script_config.json") as config_json:
        #Loads data from script_config.json
        config_data = json.load(config_json)

        #Connects to SMTP server using json data
        smtpConn = smtplib.SMTP(config_data['mail_server'], int(config_data['mail_port']))
        smtpConn.ehlo()
        smtpConn.starttls()
        smtpConn.login(config_data['username'], config_data['password'])
       
        #Sends an email with CPU, RAM, disk, and network data
        my_message = "From: " + config_data['from_email'] + "\nSubject: Test\n" + time.ctime() + "\nCPU usage: " + str(psutil.cpu_percent(interval=.1, percpu=True)) + "\nMemory usage: " + str(psutil.virtual_memory()) + "\nHard disk usage:\n" + volume_string + "Network I/O: " + str(psutil.net_io_counters())

        smtpConn.sendmail(config_data['from_email'], config_data['to_email'], my_message)
        
        print(my_message)

        #Closes mail server connection
        smtpConn.close()
except:
    print("Config file not found.")
    exit()