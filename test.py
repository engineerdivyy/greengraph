import os, subprocess
from datetime import datetime

with open("test.txt", "a") as f:
    f.write("test\n")

subprocess.run(["git", "add", "test.txt"])

env = os.environ.copy()
env["GIT_AUTHOR_DATE"] = "2025-01-16 12:00:00"
env["GIT_COMMITTER_DATE"] = "2025-01-16 12:00:00"

subprocess.run(["git", "commit", "-m", "test commit"], env=env)
