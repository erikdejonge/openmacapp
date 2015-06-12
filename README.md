#openmacapp

```
Searches and starts an OSX app from the commandline, a fragment of the applications name is enough to find it.

Usage:
  openmacapp.py [options] <name>

Options:
  -h --help     Show this screen.
  -v --verbose  Verbose

author  : rabshakeh (erik@a8.nl)
project : devenv
created : 31-05-15 / 11:08
```

**Example:**

```bash
openmacapp word
```
if there's only one possible match, start the app

```bash
$> aopen 1p
opening: 1Password 
$>
```


if there is more then 1 posibility, ask user which app to start 

```bash
$> openmacapp word
Which one? (default: q, quit: q)?
 1. 1Password.app
 2. Microsoft Word.app
$: 2
ok: /Applications/Microsoft Office 2011/Microsoft Word.app 
$>
```



**Configuration:**

The program looks for the file `"~/.openmacapp"`, this file contains the basepaths. If it's not there a default one is written, the default contains the following searchpaths

- /Applications
- ~/Applications
- ~/Documents/Applications
- /usr/local/share/applications
- ~/Library/Workflows/Applications
- /Library/Documentation/Applications
- /System/Library/CoreServices/Applications
- /Applications/Microsoft Office 2011/Office/Shared Applications
