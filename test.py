#!/usr/bin/env python
# -*- coding: utf8 -*-

import pytest  # noqa
from glob import glob
import os  # noqa
from lib.parsers_and_filters import *


def test__load_setingsfile():
    for file in glob("files_for_testing/*.sublime*"):
        cfg = load_setingsfile(file)  # noqa
    return True
