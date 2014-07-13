gitp
====

Extra functionalities for Git, written in Python.
This script allows you to execute any command line script, before and/or after executing any git command.


Instalation
-----

- Clone this repository
- `$ sudo cp gitp.py /usr/bin/gitp`
- `$ sudo chmod +x /usr/bin/gitp`

Usage
-----

Copy the json file to your repository, then replace its sample commands for their custom commands, that can be executed before or after any git command (like pull, push, commit, etc).

Use `$ gitp ...` instead of `$ git ...` example:

`$ gitp commit -m "message"`