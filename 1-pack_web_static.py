#!/usr/bin/python3
"""
module contains a scrput that generates a .tgz achive using fabric
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    local("mkdir -p versions")
    current_datetime = datetime.now()
    str_datetime = current_datetime.strftime("%Y%m%d%H%M%S")

    file_path = f"versions/web_static_{str_datetime}.tar.gz"
    result = local(f"tar -czvf {file_path} web_static")

    if result.succeeded:
        return file_path
    else:
        None
