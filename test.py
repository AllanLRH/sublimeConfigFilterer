#!/usr/bin/env python
# -*- coding: utf8 -*-

import pytest  # noqa
from glob import glob
import os  # noqa
from lib import parsers_and_filters


def test__load_setingsfile():
    for file in glob("files_for_testing/*.sublime*"):
        cfg = parsers_and_filters.load_settingsfile(file)  # noqa
    return True
