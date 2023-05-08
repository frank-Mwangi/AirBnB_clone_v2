#!/usr/bin/python3
"""
Create .tgz archive from web_static folder
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    if not os.path.exists("versions"):
        local("mkdir versions")
    dt = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    file = 'web_static_{}.tgz'.format(dt)
    local("tar -cvzf versions/{} web_static".format(file))
    filepath = "versions/{}".format(file)
    if os.path.exists(filepath):
        return filepath
    return None
