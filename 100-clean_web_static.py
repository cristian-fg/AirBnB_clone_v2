#!/usr/bin/python3
""" Keep it clean!"""
from fabric.api import *
from fabric.context_managers import *

env.hosts = ["35.231.133.57", "54.91.43.217"]


def do_clean(number=0):
    """Clean everything"""

    if int(number) == 0 or int(number) == 1:
        number = 1
        with lcd("versions"):
            local("(ls -t | head -n {};ls)| grep -v test \
                 |sort|uniq -u|xargs rm -rf".format(number))

        with cd("/data/web_static/releases"):
            run("(ls -t | head -n {};ls)| grep -v test \
                |sort|uniq -u|xargs rm -rf".format(number))

    elif int(number) > 1:
        with lcd("versions"):
            local("(ls -t | head -n {};ls)| grep -v test \
                 |sort|uniq -u|xargs rm -rf".format(number))

        with cd("/data/web_static/releases"):
            run("(ls -t | head -n {};ls)| grep -v test \
                |sort|uniq -u|xargs rm -rf".format(number))

    else:
        pass
