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

if there is more then 1 posibility, give a number 

```bash
$ openmacapp word
Which one? (default: q, quit: q)?
 1. 1Password.app
 2. Microsoft Word.app
$: 
```

**Configuration:**

The program looks for the file `"~/.openmacapp"`, this file contains the basepaths. If it's not there a default one is written
