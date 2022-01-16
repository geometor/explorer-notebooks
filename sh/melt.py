'''
create melt script to assemble animation
'''

import os as os
import stat as stat
import sys as sys

offsets = [3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
offsets = list(reversed(offsets))

def list_png(dirname):
    """list files in folder

    :dirname: TODO
    :returns: TODO

    """
    filename = dirname + '/melt_build.sh'

    with open(filename, mode='w') as file:
        os.chmod(filename, stat.S_IRWXU)

        file.write('melt ')

        files = os.listdir(dirname)
        files = filter(lambda f: f.endswith('.sh'), files)
        files = sorted(files)

        i = 0

        for f in files:
            out = 2
            if i < len(offsets):
                out = offsets[i]

            file.write(f'{f} out={out} ')
            i+=1

if __name__ == '__main__':
    dirname = sys.argv[1] if sys.argv[1] else '.'
    list_png(dirname)

