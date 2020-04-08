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

        upload = put("{}".format(archive_path), "/tmp/{}".format(p1[-1]))
        crea_dir = run("mkdir -p /data/web_static/releases/{}/".format(p2[0]))

        data = "/data/web_static/releases"
        descom = run("tar -xzf /tmp/{} -C {}/{}/".format(p1[-1], data, p2[0]))
        delet = run("rm /tmp/{}".format(p1[-1]))

        path = "mv /data/web_static/releases"
        path2 = "/data/web_static/releases"
        m = run("{}/{}/web_static/* {}/{}/".format(path, p2[0], path2, p2[0]))

        delet_dir = run("rm -rf {}/{}//web_static".format(path2, p2[0]))
        delet_dr1 = run("rm -rf /data/web_static/current")
        sl = run("ln -s {}/{}/ /data/web_static/current".format(path2, p2[0]))

        processes = [
            upload,
            crea_dir,
            descom,
            delet,
            m,
            delet_dir,
            delet_dr1,
            sl
        ]
        print("New version deployed!")
        return all(operation.succeeded for operation in processes)

    else:
        return False
