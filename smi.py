import subprocess
from pprint import pprint
import common


def read_smi(stdout, client):
    while(True):
        line = stdout.readline()

        if not line:
            return

        if line.strip().startswith(b"#"):
            continue

        client(read_smi_line(line))

def read_smi_line(line):
        values = line.strip().split()
        points = []

        for n, v in zip(common.names, values):
            try:
                v = int(v)
            except Exception:
                continue

            points.append(common.convert(n, v))

        return points



if __name__ == "__main__":

    p = subprocess.Popen(["nvidia-smi", "dmon"], stdout=subprocess.PIPE)
    read_smi(p.stdout, pprint)
