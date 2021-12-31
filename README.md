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


3. Sequence of Git Commands.

Answer:

1. to initialize.

`git init`

2. to make sure who is commiting.

`git config-global user.name "name"`

`git config-global user.email "email@email.com"`

3. to clone if its a remote repo before making the commit.

`git clone <git repo>`

4. add the current directly files/folders to staged.

`git add .`

5. commit the changes to repo.

`git commit -m 'first commit'`

6. for second commit, make some changes.

`git commit -m 'second commit'`

7. For feature branch, use checkout.

`git checkout -b Feature`

8. Check out master branch.

`git checkout master`

9. Add some changes and commit it.

`git add files`

`git commit -m 'third commit'`

10. Merge the feature branch.

`git merge Feature`

11. make some changes and commit feature.

`git add .`

`git commit -m 'fourth commit'`


4. Using Git to implement a new feature/change without affecting the main branch

Answer:

1. Clone the remote repository locally:

`git clone https://github.com/mukthy/books-toscrape-challenge.git`

2. Check if there are any available branches in the local repository:

`git branch`

3. To create a new branch called as `newfeature` on the local repository:

`git branch newfeature`

A git branch allows us to create a new working directory where we can make changes or add new content without affecting the main branch or source code.

4. Check if the new branck is created

`git branch`

```
*master
newfeature
```

5. Switch from the `master` branch to the `newfeature` branch that we created:

`git checkout newfeature`

6. If you want to create a new branch and switch to the newly created branch using single command:

`git checkout -b newfeature`

Once you are switched to the `newfeature` branch you can make the changes to the files or add files/folders.

7. Check all the untracked files and changes:

`git status`

8. To track all the changes made or files/folders in the new branch.

`git add .`

If you want to add only one single file of your new branch to track, then you can do the following:

`git add filename.txt`

9. To commit the changes to your local repository.

`git commit -m 'First Commit Message from newfeature Branch"`

10. To push the local repository to remote.



a. to confirm the URL of the remote repository

`git remote -v`

b. To create a newfeature branch on the remote repository and push.

`git push origin newfeature`

11. Now you can create a Merge Request 



a. Goto to your GitLab https://gitlab.com/muktheeswaran.m/sample.git and you should see Create merge request.

b. In the New Merge Request screen you have to select the `source` and `target` branches, you can dropdown and select the branches.

c. After selecting you can click `Compare branches and continue`

d. In the new merge request, check the Request for Merge option.

e. Once the MR is approved. The appropriate user merges that MR and the work from your Feature branch will be merged into the default branch.

5. What is a technical book/blog you read recently that you enjoyed?


I enjoy going through this book, `Automate the Boring Stuff with Python` by `By Al Sweigart`. The good thing it is available for free under CC license. They also have a course on Udemy if we need to watch in visual. This book have cool trick and interesting project ideas to automate. I have not completed it and so far there is nothing to dislike.

