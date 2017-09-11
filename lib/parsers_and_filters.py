#!/usr/bin/env python
# -*- coding: utf8 -*-

import jsoncfg
import os
import json


def load_setingsfile(filepath):
    """Loads a Sublime Text settings file.

    Parameters
    ----------
    filepath : str
        Path to settings file.

    Returns
    -------
    OrderedDict
        Settings as an OrderedDict.

    Raises
    ------
    FileNotFoundError
        If settings file is not found.
    """
    if not os.path.isfile(filepath):
        raise FileNotFoundError("The settings file {} could not be found".format(filepath))
    settings = jsoncfg.load(filepath)
    return settings


def replace_params(settingsfile, rulesfile):
    """Have a settings file on each system which are to overwrite the default settings on
    that system.
    """
    settings = load_setingsfile(settingsfile)
    rules = load_setingsfile(rulesfile)
    settings.update(rules)
    return settings
