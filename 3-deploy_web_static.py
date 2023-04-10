#!/usr/bin/python3
""" This module creates and distributes an archive to remote web servers,
using the function deploy.
"""

from fabric.api import env

env.hosts = ['18.208.119.54', '34.232.67.132']
env.user = 'ubuntu'


def do_pack():
    """Generates a .tgz archive from a directory

    Returns:
        The path to the archive upon success,
        otherwise, None
    """

    date_now = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(date_now)

    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(file_path))
        return file_path
    except Error:
        return None


def do_deploy(archive_path):
    """Distributes an archive to remote web servers

    Args:
        archive path: The path to the archive to distribute

    Returns:
        True if all operations have been done correctly,
        otherwise False
    """

    if not path.exists(archive_path):
        return False

    path_dir = archive_path.split('/')[-1]
    file_path = "/data/web_static/releases/" + path_dir.split('.')[0] + "/"
    print(file_path)

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(file_path))
        run("tar -xzf /tmp/{} -C {}".format(path_dir, file_path))

        run("rm -rf /tmp/{}".format(path_dir))
        run("mv {0}web_static/* {0}".format(file_path))
        run("rm -rf {}web_static".format(file_path))
        run("rm -rf /data/web_static/current")
        run("ln -sf {} /data/web_static/current".format(file_path))
        return True
    except Error:
        return False


def deploy():
    """Creates and distributes an archive to your web servers
    """

    archive = do_pack()
    if not archive:
        return False
    return do_deploy(archive)
