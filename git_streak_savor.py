#!/usr/bin/env python

import argparse
import re
import os
import logging
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

log_path = '/home/ycao/Dropbox/src/git_streak_savor.log'
logging.basicConfig(filename=log_path, level=logging.DEBUG)

current = datetime.today()

logging.info(str(current))

for p in path_list:
    path = HOME_DIR + p
    logging.debug('before-->')
    logging.debug(os.getcwd())
    os.chdir(path)
    logging.debug('after-->')
    logging.debug(os.getcwd())
    logging.debug(str(git.pull('origin', 'master')))
    logging.info('Pulled %s' % p)

    git_time_str = re.search('\d{4}-\d{2}-\d{2}', str(git.log('-1', '--date=iso'))).group(0) # Magic line
    last_mod_time = datetime.strptime(git_time_str, '%Y-%m-%d')
    # Check if time diff
    if current.date() - last_mod_time.date() == timedelta(0):
        logging.info('Found a new mod path %s, abort update' % p)
        exit(0)

with open(target_path, 'a') as tfile:
    tfile.write(str(current.date())+' ')

os.chdir(target_path.rsplit('/',1)[0])


if args.commit:
    logging.debug(str(git.add(target_path)))
    logging.info('Done with add')
    logging.debug(str(git.commit('-m', 'Keep streak on %s' % str(current.date()))))
    logging.info('Done with commit')
    logging.debug(str(git.push('origin', 'master')))
    logging.info('Done with push')
else:
    logging.debug(str(git.checkout(target_path)))
    logging.info('Aborted and reverted')

logging.info('-'*20)
