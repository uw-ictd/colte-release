#! /usr/bin/env python3

""" This module adds built deb packages to the package archive.

It attempts to only use python3 standard library functions for portability, but
assumes the host system has python3 and has access to reprepro on the user PATH.
"""

from pathlib import Path

import logging
import subprocess

DISTRIBUTIONS = ["buster", "bionic", "focal", "bullseye"]

def main(workspace_path):
    repo_path = Path("repo").resolve()
    for distro in DISTRIBUTIONS:
        deb_path = workspace_path.joinpath("build-volume").joinpath(distro)
        debs = deb_path.glob("*.deb")

        for deb in debs:
            log.info("Adding {} to {}".format(deb, distro))
            subprocess.run([
                "reprepro",
                "--basedir",
                repo_path,
                "includedeb",
                distro,
                deb.resolve(),
                ],
                cwd=repo_path
            )

    # Do the final export!
    subprocess.run(
        ["reprepro", "--basedir", repo_path, "export"],
        cwd=repo_path,
        )

if __name__ == "__main__":
    logging.basicConfig()
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    main(workspace_path=Path("scratch/"))

    logging.shutdown()