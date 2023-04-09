#!/usr/bin/python3
""" This module generates a .tgz archive
from the contents of the web_static folder of an AirBnB Clone repo.
It contains 1 function ``do_pack``, which does all the work.
"""

from fabric.api import local
from datetime import datetime


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
