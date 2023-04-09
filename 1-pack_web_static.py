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
    file_path = f"versions/web_static_{date_now}.tgz"

    try:
        local("mkdir -p versions")
        local(f"tar -czvf {file_path} web_static")
        return file_path
    except Error:
        return None
