#!/usr/bin/python3
"""distributes an archive to your web servers"""
from fabric.api import *
import os.path


env.hosts = ["35.231.133.57", "54.91.43.217"]


def do_deploy(archive_path):
    """functio that distributes an archive to your web servers"""
    if os.path.isfile(archive_path):
        p1 = archive_path.split("/")
        # ['versions', 'web_static_20170315003959.tgz']
        p2 = p1[-1].split(".")
        # ['web_static_20170315003959', 'tgz']

        put(archive_path, "/tmp/")
        sudo("mkdir -p /data/web_static/releases/{}".format(p2[0]))

        sudo("tar -xzf /tmp/{} -C /data/web_static/releas\
            es/{}".format(p1[-1], p2[0]))
        sudo("rm /tmp/{}".format(p1[-1]))

        sudo("mv /data/web_static/releases/{0}/web_static/* /data/web_static/release\
            s/{0}/".format(p2[0]))

        sudo("rm -rf /data/web_static/releases/{}/web_static/".format(p2[0]))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s /data/web_static/releases/{} /data/web_stat\
            ic/current".format(p2[0]))

        print("New version deployed!")
        return True

    else:
        return False
