#!/usr/bin/python3
"""Compress files"""
from fabric.api import *
from datetime import datetime
from os.path import getsize


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
