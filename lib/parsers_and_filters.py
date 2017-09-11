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
    with open(filepath) as fid:
        line_list = fid.readlines()
    keep_list = list()
    discard_line = line_list[0].startswith('/*')
    for i in range(len(line_list)):
        if not discard_line:
            if not line_list[i].strip().startswith('//') and len(line_list[i].strip()):
                keep_list.append(line_list[i])
        if line_list[i].startswith('/*'):
            discard_line = True
        if line_list[i].startswith('*/'):
            discard_line = False
    keep_list[0] = keep_list[0].replace('[', '{')
    keep_list[-1] = keep_list[-1].replace(']', '}')
    file_content = ''.join(keep_list).strip()
    # print('\n'*10, '-'*50, file_content, '-'*50, '\n'*10, sep='\n')
    cfg = jsoncfg.loads(file_content)
    return cfg

