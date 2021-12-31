1. Print the usernames of all users and their home directories

`cat /etc/passwd | awk -F ":" '{print $1 ":" $6}'`

```
#!/bin/bash

# Print the usernames of all users and their home directories
listuser=$(cat /etc/passwd | awk -F ":" '{print $1 ":" $6}')

# ● Runs once every hour.
# Make the userlist.sh file Executable by giving permissions.
# chmod +x userlist.sh
#  "crontab -e" command to edit the cron-jobs
# For hourly Crontab we can enter the below command in the cron-tab.
# @hourly /root/userlist.sh
# OR
# 5 * * * * /root/userlist.sh

# Takes the output of your above script and converts it to an MD5 hash
echo -e "$listuser" | md5sum | awk -F "-" '{print $1'}

# Stores the MD5 hash into the /var/log/current_users file.
echo -e "$listuser" | md5sum | awk -F "-" '{print $1'} > /var/log/current_users

# Store the location of the current_users file to hashfile to use the variable later.
hashfile=/var/log/current_users

# Store the Hash in a new variable newhash to compare with the oldhash.
newhash=$("echo $listuser" | md5sum)

# Store the oldhash in a variable
oldhash=$(cat $hashfile)

# compare both the hashes and if the MD5 sum changes, it should log this change in the /var/log/user_changes file with the message, DATE TIME changes occurred, replacing DATE and TIME with appropriate values.
if [[ "echo $newhash" != "echo $oldhash" ]]; then
        echo -e \"$(date)\ changes occurred \ $newhash\" > /var/log/user_changes
fi

# Replace the old MD5 hash in /var/log/current_users file with the new MD5 hash.
echo "$newhash" > /var/log/current_users
```

Cron Job to Runs once every hour.
1. Make the userlist.sh file Executable by giving permissions.

`chmod +x userlist.sh`

`crontab -e` command to edit the cron-jobs
2. For hourly Crontab we can enter the below command in the cron-tab.
```
@hourly /root/userlist.sh
# OR
# 5 * * * * /root/userlist.sh
```
It will look like this `crontab -l`
```
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command
@hourly /root/userlist.sh
```

2. Answer for Slow Performance of website.

Hello,

Thanks for reaching out to support.

There are some common causes for the slow performance:

1. Check on a different network provider, if the website is loading slowing at other network provider as well.
2. Check the `top` output and see which process is taking too much memory or CPU resources. Also it can show how much is your server load. You kill any zombie process which is showing in the `top` and free up some memory and resources.
3. Since you are using a Database on the same machine, you can run the `mytop` to check if there are any queries which is taking longer to execute and not exiting after execution. In this case you will need to make sure the database query is exexuted and exited on time otherwise it will eat up the memory.
4. Load the website on a browser and see on the network tab what are the resources getting loaded and the sizes of the resources. For Example: you check the size of the images which you can optimize by cutting down the resolution or compressing the image. It will help in loading the smaller size of the image and increase the load time of website faster.
5. Check the http access-log and see if there are too many requests from any supcious IP address. If there are too many requests at the same moment the http websever will take time to respond.
6. Check the http error_logs to see if there are any errors showing while loading some resources which might affect the load time or performance if resources are timing out.
7. Since Database Webservevr and Web-Application all three are on the same server it will eat up the 8GB memory and CPU resources if the number of request increases. It would better to atleast put the Database server in a different server to increase the performance.

Regards,
Muktheeswaran 
