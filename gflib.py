#!/usr/bin/env python
"""Python library for downloading git flow."""


import os
import tempfile
import shlex
import subprocess


EXEC_FILES = ['git-flow']
SCRIPT_FILES = [
    'git-flow-init',
    'git-flow-feature',
    'git-flow-hotfix',
    'git-flow-release',
    'git-flow-support',
    'git-flow-version',
    'gitflow-common',
    'gitflow-shFlags'
]


if os.environ.get('DEBUG') is not None:
    DEBUG = ''
else:
    DEBUG = '-q'


def gf_repo():
    """Set Git Flow Repo based on env variable or file.

    @return: Git Flow Repo from Env Var or File.
    @rtype: str
    """
    gfv = os.environ.get('GF_REPO')
    if gfv is not None:
        return gfv
    elif gfv is None:
        with open('GF_REPO') as gfvf:
            return gfvf.read()


def gf_version():
    """Set Git Flow Version based on env variable or file.

    @return: Git Flow Version from Env Var or File.
    @rtype: str
    """
    gfv = os.environ.get('GF_VERSION')
    if gfv is not None:
        return gfv
    elif gfv is None:
        with open('GF_VERSION') as gfvf:
            return gfvf.read()


def get_gitflow():
    """Downloads Git Flow from Github and creates setuptools 'scripts' struct.

    @return: Setuptools 'scripts'-type file list.
    @rtype: list
    """
    co_dir = tempfile.mkdtemp()
    git_cmds = [
        "git clone %s %s %s" % (DEBUG, gf_repo(), co_dir),
        "git checkout %s %s " % (DEBUG, gf_version()),
        "git submodule %s init" % DEBUG,
        "git submodule %s update" % DEBUG
    ]
    for cmd in git_cmds:
        subprocess.Popen(shlex.split(cmd), cwd=co_dir).wait()
    return [os.path.join(co_dir, dlf) for dlf in EXEC_FILES + SCRIPT_FILES]
