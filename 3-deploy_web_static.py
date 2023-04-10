#!/usr/bin/python3
""" This module creates and distributes an archive to remote web servers,
using the function deploy.
"""

from fabric.api import env

env.hosts = ['18.208.119.54', '34.232.67.132']
env.user = 'ubuntu'


def deploy():
    """Creates and distributes an archive to your web servers
    """
    do_pack = __import__("1-pack_web_static").do_pack
    do_deploy = __import("2-do_deploy_web_static").do_deploy

    archive = do_pack()
    if not archive:
        return False
    return do_deploy(archive)
