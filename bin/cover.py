#! /usr/bin/env python

from shutil import copyfile
from cloudmesh.common.util import path_expand
from cloudmesh.common.dotdict import dotdict
from bookmanager.cover import Cover
from pprint import pprint
from pathlib import Path
from cloudmesh.common.util import banner
import os

def cover():
    cover = Cover()

    Path(os.path.dirname("./dest")).mkdir(parents=True, exist_ok=True)

    source = Path("./template/cover-image.png").resolve()
    destination = Path("./dest/cover.png").resolve()

    copyfile(source, destination)

    banner(f"Generating Cover Page: {destination}")

    table = []

    cover.generate(
        image=destination,
        background=source,
        title="NIST Big Data\nInteroperability Framework",
        subtitle = "\nVolume 8: Reference Architecture \nInterfaces",
        author="Wo L Chang\nGregor von Laszewski",
        email="laszewski@gmail.com",
        webpage="https://github.com/cloudmesh/cloudmesh-nist"
    )

if __name__ == '__main__':
    cover()
