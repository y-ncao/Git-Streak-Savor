#!/bin/sh

APPDIR=$HOME/src/git/
export PYTHONPATH=$APPDIR/Git-Streak-Savor:$APPDIR

cd $APPDIR/Git-Streak-Savor
./git_streak_savor.py -c
