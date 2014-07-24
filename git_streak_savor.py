#!/usr/bin/env python

import argparse
import re
import os
from sh import git
from datetime import datetime, timedelta

# Flag parser for either commit or abort
parser = argparse.ArgumentParser(description='Save my github streak.')
parser.add_argument('-c', '--commit', dest='commit', action='store_true',
                    required=False, default=False, help='Actually commit the change (default: no)')
args = parser.parse_args()

HOME_DIR = '/home/ycao'
path_list = ['/Documents/Python_Study',
             '/Documents/jekyll-blog',]
target_file = '/Documents/jekyll-blog/_posts/2014-07-12-github-streak-savor.md'
target_path = HOME_DIR + target_file
current = datetime.today()

for p in path_list:
    path = HOME_DIR + p
    os.chdir(path)
    git.pull('origin', 'master')
    print 'Pulled %s' % p

    git_time_str = re.search('\d{4}-\d{2}-\d{2}', str(git.log('-1', '--date=iso'))).group(0) # Magic line
    last_mod_time = datetime.strptime(git_time_str, '%Y-%m-%d')
    # Check if time diff
    if current.date() - last_mod_time.date() == timedelta(0):
        print 'Found a new mod path %s, abort update' % p
        exit(0)

with open(target_path, 'a') as tfile:
    tfile.write(str(current.date())+' ')

os.chdir(target_path.rsplit('/',1)[0])


if args.commit:
    git.add(target_path)
    print 'Done with add'
    git.commit('-m', 'Keep streak on %s' % str(current.date()))
    print 'Done with commit'
    git.push('origin', 'master')
    print 'Done with push'
else:
    git.checkout(target_path)
    print 'Aborted and reverted'
