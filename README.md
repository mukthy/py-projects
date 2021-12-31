`
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
`
