import sys
from subprocess import call

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

def clean_git_msg(msg, encoding="utf8"):

    msg = str(msg)

    msg.encode(encoding)

    unsafe = ["\n", "rm"]

    for ommit in unsafe:
        msg = msg.replace(ommit, "")

    return msg

def main():

    while (True):
        commit_msg = input("Commit Message >>> ")
        commit_msg = clean_git_msg(commit_msg)
        if len(commit_msg) > 71:
            ans = query_yes_no("Message is too long (max 72 char.), Re-enter (will truncate if no)?")
            if (ans):
                continue
            else:
                commit_msg = commit_msg[0:72]
                break
        else:
            break

    call(["git", "pull"])
    call(["git", "add", "--all"])
    call(["git", "commit", "-m", commit_msg])
    call(["git", "push", "origin",  "src"])

    if len(sys.argv) == 2:
        if sys.argv[1] == 'commit-only':
            sys.exit(0)

    call([".\make.bat", "html"])

if __name__ == '__main__':
    main()
