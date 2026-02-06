import os
import random
import subprocess
from datetime import datetime, timedelta

START_DATE = "2025-09-01"   # yyyy-mm-dd
END_DATE   = "2026-02-01"   # yyyy-mm-dd

start = datetime.strptime(START_DATE, "%Y-%m-%d")
end   = datetime.strptime(END_DATE, "%Y-%m-%d")

current = start

while current <= end:
    commits_today = random.randint(1, 4)  # 1–4 commits/day (natural green)

    for i in range(commits_today):
        with open("log.txt", "a") as f:
            f.write(f"Commit on {current.date()} #{i+1}\n")

        subprocess.run(["git", "add", "log.txt"])

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = current.strftime("%Y-%m-%d 12:00:00")
        env["GIT_COMMITTER_DATE"] = current.strftime("%Y-%m-%d 12:00:00")

        subprocess.run(
            ["git", "commit", "-m", f"Commit on {current.date()}"],
            env=env
        )

    current += timedelta(days=1)
