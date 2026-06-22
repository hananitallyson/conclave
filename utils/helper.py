import subprocess
from datetime import datetime

def clear():
    subprocess.run("clear")


def fromiso(iso):
    return datetime.fromisoformat(iso)


def timestring(iso):
    date = fromiso(iso)

    return date.strftime("%Y-%m-%d %H:%M")
