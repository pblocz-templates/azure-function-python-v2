import subprocess as sp
import sys
from typing import Iterable, cast

output = sys.argv[1]
args = sys.argv[2:]

logfile = open(output, "wb")  # noqa: WPS515
cmd = ["vulture"] + args

with sp.Popen(
    cmd, stdout=sp.PIPE, stderr=sp.STDOUT, bufsize=1, universal_newlines=True
) as p:
    with open(output, "w") as buf:
        for line in cast(Iterable[str], p.stdout):

            filel = line.replace(": ", ":0: V000 ", 1)

            print(line, end="")  # noqa: WPS421
            buf.write(filel)
    rc = p.returncode

sys.exit(rc)
