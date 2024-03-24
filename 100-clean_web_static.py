#!/usr/bin/python3
"""
Deletes out-of-date archives
"""

import os
from fabric.api import *

env.hosts = ['54.90.48.253', '52.86.174.39']


def do_clean(number=0):
    """Delete out-of-date archives.
    Arguments:
        number (int): The no of archives to keep.
    If no is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
