import datetime
import psutil
import smtplib
import json
import time
from twilio.rest import Client

#Obtains current date and time and formats it
raw_date = datetime.datetime.fromtimestamp(time.time())
date = raw_date.strftime('%B %d, %Y %H:%M:%S')
hour = raw_date.strftime('%H:%M')
#hour = "6:00"

#Connects to mail server and sends messages
try:
    with open("text_files/script_config.json") as config_json:
        #Loads data from script_config.json
        config_data = json.load(config_json)

        #If the time is 6 AM or 6 PM, connects to email server and sends an email status report
        if hour == "6:00" or hour == "18:00":
            #Connects to SMTP server using json data
            smtpConn = smtplib.SMTP(config_data['mail_server'], int(config_data['mail_port']))
            smtpConn.ehlo()
            smtpConn.starttls()
            smtpConn.login(config_data['username'], config_data['password'])

            #Creates a string displaying CPU usage
            cpu_string = "\n\nCPU usage per core: "
            core_count = 1
            for core in psutil.cpu_percent(interval=.1, percpu=True):
                cpu_string += "\n\t" + str(core_count) + ": " + str(core) + "%  "
                core_count += 1

            #Creates a string displaying RAM usage
            ram_string = "\n\nRAM usage:\n\tUsed: " + str(psutil.virtual_memory().used) + "\n\tAvailable: " + str(psutil.virtual_memory().available) + "\n\tPercent used: " + str(psutil.virtual_memory().percent)
            
            #Creates a string displaying disk usage
            volume_string = "\n\nHard disk usage:\n"
            volumes = psutil.disk_partitions()
            for volume in volumes:
                volume_string += "\t"
                volume_string += volume[1]
                volume_string += "  Used: " + str(psutil.disk_usage(volume[1]).used)
                volume_string += "  Available: " + str(psutil.disk_usage(volume[1]).free)
                volume_string += "  Percent used: " + str(psutil.disk_usage(volume[1]).percent) + "%"
                volume_string += "\n"
            
            #Creates a string displaying network I/O
            network_string = "\nNetwork I/O:\n\tBytes sent: " + str(psutil.net_io_counters().bytes_sent) + "\n\tBytes received: " + str(psutil.net_io_counters().bytes_recv) + "\n\tIn errors: " + str(psutil.net_io_counters().errin) + "\n\tOut errors: " + str(psutil.net_io_counters().errout) + "\n\tIn packets dropped: " + str(psutil.net_io_counters().dropin) + "\n\tOut packets dropped: " + str(psutil.net_io_counters().dropout)

            #Sends an email with CPU, RAM, disk, and network data
            my_message = "From: " + config_data['from_email'] + "\nSubject: Test\n" + date + cpu_string + ram_string + volume_string + network_string

            smtpConn.sendmail(config_data['from_email'], config_data['to_email'], my_message)
            
            print(my_message)

            #Closes mail server connection
            smtpConn.close()

        #Connects to Twilio SMS client using json data
        accountID = config_data['twilio_account_id']
        authToken = config_data['twilio_auth_token']
        trialNumber = config_data['twilio_trial_number'] # number must be prefixed with a +1, e.g. +12485551212
        cellNumber = config_data['twilio_cell_number'] # use same number format as above

        twClient = Client(accountID, authToken)

        #If resource usage exceeds a certain threshold, sends a text message alert
        send_alert = False
        alert_message = date + "\n"

        #Checks CPU usage and adds alert information if greater than 85%
        cpu_usage = psutil.cpu_percent(interval=.1)
        if cpu_usage > 85:
            send_alert = True
            alert_message += "\nCPU usage has reached " + str(cpu_usage) + "%\n"
        
        #Checks RAM usage and adds alert information if greater than 90%
        mem_usage = psutil.virtual_memory().percent
        if mem_usage > 90:
            send_alert = True
            alert_message += "\nRAM usage has reached " + str(mem_usage) + "%\n"

        #Checks percent of space used in each volume and adds alert information of a volume exceeds 70%
        volumes = psutil.disk_partitions()
        for volume in volumes:
            space_used = psutil.disk_usage(volume[1]).percent
            if space_used > 70:
                send_alert = True
                alert_message += "\n" + volume[1] + " is " + str(space_used) + "% full and close to running out of space\n"

        #Checks network I/O and adds alert information if errors or dropped packets are appearing
        net_errors_in = psutil.net_io_counters().errin 
        net_errors_out = psutil.net_io_counters().errout 
        net_drop_in = psutil.net_io_counters().dropin 
        net_drop_out = psutil.net_io_counters().dropout 

        if net_errors_in > 0 or net_errors_out > 0 or net_drop_in > 0 or net_drop_out > 0:
            send_alert = True
            alert_message += "\nNetwork issues detected:\n\tIn errors: " + str(net_errors_in) + "\n\tOut errors: " + str(net_errors_out) + "\n\tIn packets dropped: " + str(net_drop_in) + "\n\tOut packets dropped: " + str(net_drop_out)

        #print(alert_message)
        current_time = time.time()
        last_text_time = config_data['last_text']
        seconds_since_last_text = current_time - float(last_text_time)

        #If an issue is detected and an alert has not been sent in the last hour, sends the alert message as a text
        if send_alert and seconds_since_last_text >= 3600:
            #Sends text message with alert information
            my_message = twClient.messages.create(body=alert_message, from_=trialNumber, to=cellNumber)

            #Updates last_text json value to the current time
            config_data['last_text'] = str(current_time)
            with open("text_files/script_config.json", "w") as config_json:
                json.dump(config_data, config_json)
except:
    print("Config file not found.")
    exit()