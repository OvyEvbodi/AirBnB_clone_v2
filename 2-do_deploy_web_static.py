#!/usr/bin/python3
"""This module Distributes an archive to remote web servers,
using the function do_deploy.
It contains 1 function ``do_deploy`` that does all the work
"""

from fabric.api import run, put, env
from os import path


def do_deploy(archive_path):
    """Distributes an archive to remote web servers

    Args:
        archive path: The path to the archive to distribute

    Returns:
        True if all operations have been done correctly,
        otherwise False
    """

    env.hosts = ['18.208.119.54', '34.232.67.132']
    env.user = 'ubuntu'

    if not path.exists(archive_path):
        return False

    path_dir = archive_path.split('/')[-1]
    file_path = "/data/web_static/releases/" + path_dir.split('.')[0]
    print(file_path)

    try:
        put(archive_path, "/tmp/")
        run(f"mkdir -p {file_path}")
        run(f"tar -xzf /tmp/{archive_path} -C {file_path}")

        run(f"rm -rf /tmp/{archive_path}")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -sf {file_path} /data/web_static/current/")
        return True
    except Error:
        return False
