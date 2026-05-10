import subprocess
import sys


def run(cmd):
    result = subprocess.run(cmd, check=False)
    if result.returncode != 0:
        sys.exit(result.returncode)


print("Building and serving docs locally...")
print("Access the site at http://localhost:8000")
print("Press Ctrl+C to stop\n")

run(["mkdocs", "serve"])
