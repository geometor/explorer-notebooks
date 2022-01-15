'''
create melt script to assemble animation
'''

import os as os
import stat as stat

filename = "melt_test.sh"
fibs = [3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
fibs = list(reversed(fibs))

with open(filename, mode="w") as file:
    os.chmod(filename, stat.S_IRWXU)

    cmap_name = "copper"

    file.write("melt ")

    files = os.listdir()
    files = filter(lambda f: f.endswith('.sh'), files)
    files = sorted(files)

    i = 0

    for f in files:
        out = 2
        if i < len(fibs):
            out = fibs[i]

        file.write(f"{f} out={out} ")
        i+=1

