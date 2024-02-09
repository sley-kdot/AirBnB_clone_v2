#!/usr/bin/python3
""" The  3-deploy_web_static.py module """
from datetime import datetime
from fabric.api import local, env, run, put
from os import path

env.hosts = ['54.89.182.156', '100.25.45.217']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """
    Genarates a .tgz archive from the contents of the
    web_static folder of AirBnB clone
    """
    local("mkdir -p versions")

    local("mkdir -p versions")

    current_time = datetime.now()
    date_time_str = current_time.strftime("%Y%m%d%H%M%S")

    archive_name = "web_static_{}.tgz".format(date_time_str)

    res = local("tar -cvzf versions/{} web_static".format(archive_name))

    if res.succeeded:
        archive_path = path.join("versions", archive_name)
        return archive_path
    else:
        return None


def do_deploy(archive_path):
    """ Distributes an archive to the web server

    Arguments:
        archive_path (str): The path of the archive to distribute
    Returns:
        If file doesn't exist at path error occurs - False
        Otherwise - True
    """
    if not path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp')

        # Uncompress archive to the folder
        archive_filename = path.basename(archive_path)
        release_folder = '/data/web_static/releases/{}'.format(
            archive_filename.split('.')[0])
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

        # Delete the archive from web server
        run('rm /tmp/{}'.format(archive_filename))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new the symbolic link /data/web_static/current
        run('ln -s {} /data/web_static/current'.format(release_folder))

        print('New version deployed!')
        return True
    except Exception as e:
        print('Error:', e)
        return False


def deploy():
    """ Deploy the web static """
    archive_path = do_pack()
    if archive_path is None:
        return False
    success = do_deploy(archive_path)
    return success
