CoLTE Release
=============

This repository contains the release automation used by the CoLTE project to
build images for multiple target platforms. This is a PUBLIC repository shared
with the goal of increasing transparency and allowing community input into
improvement of the release process. As a public repository, it contains no key
material and uses variables or input prompts for important project-specific
secrets and parameters.

Usage
-----

The release is divided into three steps. All commands shown should be run from the root of this repo.

1. Build all the deb packages. This can be done for a specific tag with the
   command `python3 do_build.py --clean --tag [TAGNAME]`.

2. Then add the built packages to the local package archive. `python3
   do_release.py`. The release script will prompt you for GPG key passwords as
   needed.

3. Upload the completed archive to the public webserver. On our private
   production machine, there is a script `./server_upload [NETID]` which does
   this.

4. Bonus: Clean up any dangling docker images. `docker container prune; docker
   image prune` *Be careful*, since this command may delete other containers not
   associated with this release!