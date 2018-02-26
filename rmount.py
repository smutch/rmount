#!/usr/bin/env python

"""Mount a remote host."""

from subprocess import call
from pathlib import Path
import click

__author__ = 'Simon Mutch'
__date__ = '2017-03-16'
__version__ = '0.1'


def _mount(host, root, mount_point, local_path):
    error = call(["mkdir", local_path])
    if error:
        print(f"Failed to make dir `{mount_point}`...")

    call(["sshfs", f"{host}:{root}",
            local_path,
            "-oauto_cache,reconnect,defer_permissions"
            ",negative_vncache,noappledouble,follow_symlinks"
            f",volname={mount_point}"])


def _unmount(local_path):
    call(["umount", local_path])
    call(["rmdir", local_path])

@click.command()
@click.argument('host', type=click.STRING)
@click.option('--root', type=click.STRING, default='', metavar='DIR')
@click.option('--remount', '-r', is_flag=True)
@click.option('--unmount', '-u', is_flag=True)
def rmount(host, root='', remount=False, unmount=False):
    mount_point = host.split(".")[0]
    if root != '':
        mount_point = '-'.join((mount_point, root.split("/")[-1]))

    local_path = str(Path(f"~/mounts/{mount_point}").expanduser())

    if remount:
        _unmount(local_path)
        _mount(host, root, mount_point, local_path)
        return 0

    if not unmount:
        _mount(host, root, mount_point, local_path)
    else:
        _unmount(local_path)

    return 0


if __name__ == '__main__':
    rmount()
