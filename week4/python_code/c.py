

#!/usr/bin/env python3
import os
import subprocess
from multiprocessing import Pool

src = os.path.expanduser("~/data/prod/")
dest = os.path.expanduser("~/data/prod_backup/")
def get_pathlist(folder):
        pathlist = []

        for root, dirs, files in os.walk(folder):
                path = root[len(folder):]
                if dirs != []:
                        for d in dirs:
                                pathlist.append((path, d))
                for f in files:
                        pathlist.append((path, f))
        return pathlist



def run(path):
        source = os.path.join(src, path[0], path[1])
        destination = os.path.join(dest, path[0])
        subprocess.call(['rsync', '-arh', source, destination])



if __name__ == "__main__":

        task = get_pathlist(src)
        p = Pool(len(task), maxtasksperchild=1)
        p.map(run, task)




