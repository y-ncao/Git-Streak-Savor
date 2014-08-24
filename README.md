##Git-Streak-Savor

This is a script to help you keep streak on github.

###Why This?
Do you enjoy to see all the green grids on your github personal info? Are you annoyed when you fail to keep the current streak just because you have to go to a party with your friends?

That's this tools for. Save you from loosing a streak at 11:55PM.

Input the path of your working directory to be monitored, if you don't have any modification to those directory, Git-Streak-Savor will create a commit for you to make up the streak.

Create a Cron job to run this script every day on 11:55PM. It will check if you have made any contribution today. If you did, it's won't mess up anything.

###I Know This is Cheating
I know this is cheating, but it really helps me to keep the habit to write some code for myself everyday. Every time I know I didn't do anything today, I'll feel guilty to have my robot to it for me. Also I've output every date that I might miss a streak to one of my blog's post, so that I'll know I missed one.

The good news is that it haven't triggered for a long while.

###Configuration
1. Make sure you installed the package [sh](https://pypi.python.org/pypi/sh).
2. Copy config.ini to config and change the path you want to monitor.
3. Setup the crontab to run this at 11:55PM