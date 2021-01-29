#!/bin/bash
#
# A docker entrypoint script to build a package
set -e

make all

# Copy the built packages to the mounted output volume
OUT_DIR=$1
OUT_USER=$2

mkdir -p /build-volume/"${OUT_DIR}"
mv BUILD/*.deb /build-volume/"${OUT_DIR}"

if test -z "$OUT_USER"
then
    echo "No output user set, leaving as container user (likely root)"
else
    chown --recursive $OUT_USER /build-volume/"${OUT_DIR}"
    chgrp --recursive $OUT_USER /build-volume/"${OUT_DIR}"
fi