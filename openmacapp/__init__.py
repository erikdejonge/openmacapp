#!/usr/bin/env python3
# coding=utf-8
"""

Searches ("~/.openmacapp) and starts an OSX app from the commandline

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
import copy

from arguments import Arguments
from consoleprinter import doinput, console
g_basepaths = """
/Applications
/Applications/Utilities
/Applications/Microsoft Office 2011/Office/Shared Applications
/Library/Documentation/Applications
/System/Library/CoreServices
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
    if not os.path.exists(base):
        return []

    folders = []
    base = os.path.expanduser(base)

    if not base.lower().endswith("app") and not os.path.isfile(base):
        folders = [base]
        listdir = [folder for folder in os.listdir(base) if os.path.exists(os.path.join(base, folder)) and os.path.isdir(os.path.join(base, folder)) and not folder.strip().lower().endswith(".app")]
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
    sbases = set()

    for base in bases:
        if os.path.exists(base) and not base.lower().endswith(".app") and os.path.isdir(base):
            for subbase in os.listdir(base):
                if not subbase.lower().endswith(".app"):
                    sbases.add(os.path.join(base, subbase))
                else:
                    sbases.add(base)

    bases.extend(list(sbases))

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

        # print("open '" + applist[0] +"'")
    else:
        answer = ""
        applistorg = copy.deepcopy(applist)
        print(applist)
        answer, display_answers = doinput(description="Which one?", default="q", theanswers=applist, force=False, returnnum=True)

        os.system("open \"" + display_answers[answer].replace('"', '\"') + "\"")


if __name__ == "__main__":
    main()
