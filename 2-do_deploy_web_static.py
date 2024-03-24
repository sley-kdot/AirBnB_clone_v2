#!/usr/bin/python3
"""
module contains a script that distributes and deploys using fabric
"""
from fabric.api import *
from datetime import datetime
import os


env.hosts = ['54.83.66.203', '100.26.227.228']


def do_deploy(archive_path):
    """distributes an archive to web servers"""

    # check if file exist
    it_exists = os.path.exists(archive_path)
    if not it_exists:
        return False

    try:
        # upload the .tgz archive to /tmp
        put(archive_path, "/tmp")
        file_path = archive_path[9:34]
        
        # unpack the archive file
        file_name = archive_path[9:]
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(file_name, file_path))

        # del the archive file from tmp dir
        run("rm /tmp/{}".format(file_name))
        run("rm -rf /data/web_static/current")

        # create a new sym-link ponting to the new version
        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(file_path))

        print("New version deployed")
        return True
    except Exception as er:
        return False
