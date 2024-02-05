#!/usr/bin/python3
""" File 2-do_deploy_web_static.py """
from fabric.api import env, run, put
from os import path

env.hosts = ['54.89.182.156', '100.25.45.217']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


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
