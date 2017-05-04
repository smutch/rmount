#!/usr/bin/env python

"""Mount a remote host."""

import click
from subprocess import call
from pathlib import Path

__author__ = 'Simon Mutch'
__date__ = '2017-03-16'
__version__ = '0.1'


@click.command()
@click.argument('host', type=click.STRING)
@click.option('--root', type=click.STRING, default='', metavar='DIR')
@click.option('--unmount', '-u', is_flag=True)
def rmount(host, root=None, unmount=False):
    mount_point = host.split(".")[0]
    if root != '':
        mount_point = '-'.join((mount_point, root.split("/")[-1]))

    local_path = Path(f"~/mounts/{mount_point}").expanduser()

    if not unmount:
        error = call(["mkdir", local_path])
        if error:
            print(f"Failed to make dir `{mount_point}`...")

        call(["sshfs", f"{host}:{root}",
              local_path,
              "-oauto_cache,reconnect,defer_permissions"
              ",negative_vncache,noappledouble"
              f",volname={mount_point}"])

    else:
        call(["umount", local_path])
        call(["rmdir", local_path])

if __name__ == '__main__':
    rmount()
