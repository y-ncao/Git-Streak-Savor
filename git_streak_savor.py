#!/usr/bin/env python

import subprocess
import re
from datetime import datetime, timedelta

def git_last_mod(path=None):
    p = subprocess.Popen(['git', 'log', '-1', '--date=iso'], stdout=subprocess.PIPE, cwd=path)
    out, err = p.communicate()
    m = re.search('\d{4}-\d{2}-\d{2}', out)
    return m.group(0)

def git_pull(path=None):
    p = subprocess.Popen(['git', 'pull', 'origin', 'master'], stdout=subprocess.PIPE, cwd=path)
    out, err = p.communicate()
    if err is not None:
        print 'Found Error in %s' % path
    return err

def git_add(path=None):
    p = subprocess.Popen(['git', 'add', path], stdout=subprocess.PIPE, cwd=path.rsplit('/',1)[0])
    out, err = p.communicate()
    if err is not None:
        print 'Found Error in %s' % path
    return err

def git_commit(message, path=None):
    p = subprocess.Popen(['git', 'commit', '-m', message], stdout=subprocess.PIPE, cwd=path.rsplit('/',1)[0])
    out, err = p.communicate()
    if err is not None:
        print 'Found Error in %s' % path
    return err

def git_push(path=None):
    p = subprocess.Popen(['git', 'push', 'origin', 'master'], stdout=subprocess.PIPE, cwd=path.rsplit('/',1)[0])
    out, err = p.communicate()
    if err is not None:
        print 'Found Error in %s' % path
    return err


if __name__ == '__main__':
    HOME_DIR = '/home/ycao'
    path_list = [ '/Documents/Python-Study',
                  '/Documents/jekyll-blog',
                  ]
    target_file = '/Documents/jekyll-blog/_posts/2014-07-12-github-streak-savor.md'
    target_path = HOME_DIR + target_file
    current = datetime.today()

    for p in path_list:
        path = HOME_DIR + p
        git_pull(path)
        git_time_str = git_last_mod(path)
        last_mod_time = datetime.strptime(git_time_str, '%Y-%m-%d')
        # Check if time diff
        if current.date() - last_mod_time.date() == timedelta(0):
            print 'Found a new mod path %s, abort update' % p
            exit(0)

    with open(target_path, 'a') as tfile:
        tfile.write(str(current.date())+' ')

    git_add(target_path)
    git_commit('Keep streak on %s' % str(current.date()), target_path)
    git_push(target_path)

# Todo:
# 1. Move path to config file so directory wouldn't expose to public
# 2. Write Cron job template
