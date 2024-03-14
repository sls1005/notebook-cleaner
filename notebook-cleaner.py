#!/usr/bin/env python
# -*- coding: ASCII -*-
# Notebook Cleaner 1.1
# Python 3 is recommended for interpreting this, while Python 2 is also supported.
import json
from sys import version_info, stdout, stderr, argv
from os.path import exists

usage = '''
Usage: notebook-cleanser.py [options] <file>

arguments:
      <file>                 The name of the input file.

options:
      -h, --help             Display this help message and exit.

      -o, --output <file>    The name of the output file.

      --indent <N>           The number of spaces to be used for indentation. Note that this does not affect the appearance of the notebook. It normally shouldn't be specified.

By default, this overwrites the original file (the input file). If `--output` is provided, it instead writes to the specified output file. This always overwrites the output file if it exists.
'''

if version_info.major < 3:
    range = xrange

def main():
    input_file = ''
    output_file = ''
    indent = None

    argc = len(argv)
    k = argc - 1
    i = 1
    while i < argc:
        a = argv[i]
        if a in ('-h', '--help'):
            stdout.write(usage)
            exit()
        elif a in ('-o', '--output'):
            if i < k:
                output_file = argv[i+1]
                i += 2
            else:
                stderr.write("[Error] Expected a file name after %s.\n" % a)
                exit(1)
        elif a == '--indent':
            if i < k:
                s = argv[i+1]
                try:
                    indent = int(s)
                except ValueError:
                    stderr.write("[Error] '%s' is not an integer.\n" % s)
                    exit(1)
                i += 2
            else:
                stderr.write("[Error] Expected an integer after %s.\n" % a)
                exit(1)
        else:
            input_file = a
            i += 1

    if input_file == '':
        stdout.write(usage)
        exit()
    elif output_file == '':
        output_file = input_file

    x = {}
    with open(input_file, 'r') as f:
        x = json.load(f)

    v = x['nbformat']
    if type(v) is not int:
        stderr.write("[Error] Unknown format.\n")
        exit(2)
    elif v < 4:
        stderr.write("[Error] Format version %d is not supported.\n" % v)
        exit(3)

    for i in range(len(x['cells'])):
        x['cells'][i]['metadata'] = {}

    for k in list(x['metadata'].keys()):
        if k not in ('kernelspec', 'kernel_info', 'language_info'):
            x['metadata'].pop(k)

    with open(output_file, 'w') as f:
        print("\nWriting to '%s'..." % output_file)
        json.dump(x, f, indent=indent)

if __name__ == '__main__':
    main()
