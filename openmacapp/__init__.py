#!/usr/bin/env python3
# coding=utf-8
"""
Searches and starts an OSX app from the commandline

Usage:
  openmacapp.py [options] <name>

Options:
  -h --help     Show this screen.
  -v --verbose  Verbose

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 31-05-15 / 11:08
"""

import os
import glob

from arguments import Arguments
from consoleprinter import doinput
g_basepaths = """
/Applications
/Applications/Microsoft Office 2011/Office/Shared Applications
/Library/Documentation/Applications
/System/Library/CoreServices/Applications
/usr/local/share/applications
~/Applications
~/Documents/Applications
~/Library/Workflows/Applications
"""


class IArguments(Arguments):
    """
    IArguments
    """
    def __init__(self, doc=None):
        """
        @type doc: str, None
        """
        self.help = False
        self.name = ""
        self.verbose = False
        super().__init__(doc)


def scan_for_subfolders(base):
    """
    @type base: str
    @return: None
    """
    base = os.path.expanduser(base)
    folders = [base]
    listdir = [folder for folder in os.listdir(base) if not folder.strip().lower().endswith(".app")]
    for item in listdir:
        itemp = os.path.join(base, item)

        if os.path.isdir(itemp):
            folders.append(itemp)

    return folders


def search_appfolder(filename, searchfolder, verbose=False):
    """
    @type filename: str
    @type searchfolder: str
    @type verbose: bool
    @return: None
    """
    if verbose:
        print("\033[37msearch: " + searchfolder + "\033[0m")

    applist = []
    os.chdir(searchfolder)

    for app in glob.glob("*.app"):
        if filename.lower().strip() in app.lower().strip():
            applist.append(os.path.join(searchfolder, app))

    return applist

import copy
def main():
    """
    main
    """
    arguments = IArguments(__doc__)
    applist = []
    folders = []
    configfile = os.path.expanduser("~/.openmacapp")

    if not os.path.exists(configfile):
        open(configfile, "w").write(g_basepaths)

    bases = [base for base in open(configfile).read().split("\n") if base]
    for base in bases:
        folders.extend(scan_for_subfolders(base))

    folders = sorted(set(folders))

    for folder in folders:
        applist.extend(search_appfolder(arguments.name, folder, arguments.verbose))

    if arguments.verbose:
        print("--")

    applist = list(set(applist))

    if len(applist) == 0:
        print("\033[33m" + arguments.name + " not found\033[0m")
    elif len(applist) == 1:
        print("\033[33mopening:", os.path.basename(applist[0]).strip(".app"), "\033[0m")
        os.system("open '" + applist[0] + "'")
    else:

        answer = doinput(description="Which one?", default="q", answers=applist, force=False, returnnum=True)
        applist.sort()

        os.system("open '" + applist[answer] + "'")

if __name__ == "__main__":
    main()
