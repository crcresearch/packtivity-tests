# -*- coding: utf-8 -*-
#
# This file is part of the packivity testing project.
# For copyright and licensing information about this package, see the
# NOTICE.txt and LICENSE.txt files in its top-level directory; they are
# available at https://github.com/crcresearch/packitivity-tests
#
# This Source Code Form is subject to the terms of the MIT License
#

import os
import subprocess

from pip._vendor.distlib._backport import shutil

base_dir = os.path.dirname(os.path.abspath(__file__))


def test_run():
    cwd = os.getcwd()
    os.chdir(base_dir)
    print os.getcwd()
    if os.path.exists("_packtivity"):
        shutil.rmtree("_packtivity")
    try:
        subprocess.call(["./run.sh"])
    finally:
        os.chdir(cwd)

    # Make sure output files were created
    assert(os.path.exists(os.path.join(base_dir, "_packtivity")))
