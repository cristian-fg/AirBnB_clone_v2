#!/usr/bin/python3
"""distributes an archive to your web servers"""
from fabric.api import *
from datetime import datetime
import os.path
from os.path import getsize


env.hosts = ["35.231.133.57", "54.91.43.217"]


@runs_once
def do_pack():
    """Function that compress a files"""
    fil = "web_static_{:s}.tgz".format(datetime.now().strftime("%Y%m%d%H%M%S"))
    print("Packing web_static to versions/{}".format(fil))

    local("mkdir -p versions")
    path = local("tar -cvzf versions/{:s} web_static".format(fil))

    size = getsize("versions/{}".format(fil))

    if path.succeeded:
        print("web_static packed: versions/{} -> {}Bytes".format(fil, size))
        return("versions/{}".format(fil))
    else:
        return None


def do_deploy(archive_path):
    """functio that distributes an archive to your web servers"""
    if os.path.isfile(archive_path):
        p1 = archive_path.split("/")
        # ['versions', 'web_static_20170315003959.tgz']
        p2 = p1[-1].split(".")
        # ['web_static_20170315003959', 'tgz']

        put(archive_path, "/tmp/")
        sudo("mkdir -p /data/web_static/releases/{}/".format(p2[0]))

        data = "/data/web_static/releases"
        sudo("tar -xzf /tmp/{} -C {}/{}/".format(p1[-1], data, p2[0]))
        sudo("rm /tmp/{}".format(p1[-1]))

        path = "mv /data/web_static/releases"
        path2 = "/data/web_static/releases"
        sudo("{}/{}/web_static/* {}/{}/".format(path, p2[0], path2, p2[0]))

        sudo("rm -rf {}/{}//web_static".format(path2, p2[0]))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {}/{}/ /data/web_static/current".format(path2, p2[0]))

        print("New version deployed!")
        return True

    else:
        return False


@task
def deploy():
    """Deploy all automatic"""

    new = do_pack()
    if new is None:
        return False

    new_up = do_deploy(new)
    return new_up
