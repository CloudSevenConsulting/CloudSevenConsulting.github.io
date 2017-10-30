from subprocess import call
call(["git", "pull"])
call(["git", "add", "--all"])
call(["git", "commit", "-m", "docs"])
call(["git", "push", "origin",  "master"])
