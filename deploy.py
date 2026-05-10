import subprocess
import sys


DEFAULT_COMMIT_MESSAGE = "Deploy site updates"

def run(cmd):
    result = subprocess.run(cmd, check=False)
    if result.returncode != 0:
        sys.exit(result.returncode)


def get_output(cmd):
    result = subprocess.run(cmd, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(result.returncode)
    return result.stdout


def get_commit_message():
    if len(sys.argv) > 1 and sys.argv[1].strip():
        return sys.argv[1].strip()
    return DEFAULT_COMMIT_MESSAGE


commit_message = get_commit_message()

run(["mkdocs", "build", "--clean"])
run(["git", "add", "-A"])

if get_output(["git", "status", "--porcelain"]).strip():
    run(["git", "commit", "-m", commit_message])

run(["git", "push"])
