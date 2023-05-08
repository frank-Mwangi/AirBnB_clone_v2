#!/usr/bin/python3
"""Deploy an archive to remote webservers."""


from fabric.api import env, put, run
import os


env.hosts = ['100.25.103.66', '100.25.215.1']


def do_deploy(archive_path):
    """
    Uploads an archive file to remote web servers.

    args:
        archive_path: path to the archive file
    Returns:
        True if success, false otherwise

    """
    if not os.path.exists(archive_path):
        return False
    put(archive_path, "/tmp")
    dirName = archive_path.split('/')[1].split('.')[0]
    run("mkdir -p /data/web_static/releases/{}".format(dirName))
    archiveName = archive_path.split('/')[1]
    run("tar -xzf /tmp/{} -C"
        " /data/web_static/releases/{}/".format(archiveName, dirName))
    run("rm /tmp/{}".format(archiveName))
    run("mv /data/web_static/releases/{}/web_static/*"
        " /data/web_static/releases/{}/".format(dirName, dirName))
    run("rm -rf /data/web_static/releases/{}/web_static".format(dirName))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/"
        " /data/web_static/current".format(dirName))
    return True
