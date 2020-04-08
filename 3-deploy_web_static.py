#!/usr/bin/python3
"""distributes an archive to your web servers"""
from fabric.api import *

pack = __import__('1-pack_web_static')
up = __import__('2-do_deploy_web_static')


env.hosts = ["35.231.133.57", "54.91.43.217"]


def deploy():
    """Deploy all automatic"""

    new = pack.do_pack()
    if new is None:
        return False

    new_up = up.do_deploy(new)
    return new_up
