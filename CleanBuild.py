import os, shutil
import sys

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

do_not_remove = ['.nojekyll', '.git']

target_folder = './build/html'
assert(os.path.isdir(target_folder))
target_folder = os.path.abspath(os.path.normpath(target_folder))
assert(os.path.isdir(target_folder))
ans = query_yes_no("Clean all Sphinx files from: %s" % target_folder, default="no")

if not(ans):
    print("Clean job terminated.")
    sys.exit(0)
else:
    print("Removing...")

    for the_file in os.listdir(target_folder):
        file_path = os.path.join(target_folder, the_file)

        if the_file in do_not_remove:
            continue
        else:
            print(file_path)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)
