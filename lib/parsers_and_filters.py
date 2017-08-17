#!/usr/bin/env python
# -*- coding: utf8 -*-

import jsoncfg
import os


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
    cfg = jsoncfg.load(filepath)
    return cfg

