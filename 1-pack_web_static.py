#!/usr/bin/python3:wq

""" The 1-pack_web_static.py module """
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """
    Genarates a .tgz archive from the contents of the
    web_static folder of AirBnB clone
    """
    local("mkdir -p versions")

    current_time = datetime.now()
    date_time_str = current_time.strftime("%Y%m%d%H%M%S")

    archive_name = "web_static_{}.tgz".format(date_time_str)

    res = local("tar -cvzf versions/{} web_static".format(archive_name))

    if res.succeeded:
        archive_path = os.path.join("versions", archive_name)
        return archive_path
    else:
        return None
