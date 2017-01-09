#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import print_function

import sys
import getopt
import os


def main(argv):
    inputfile = ""
    prefix = "convert_results"

    try: 
        opts, args = getopt.getopt(argv, "hi:f:", ["help", "ifile=", "prefix="])
    except getopt.GetoptError: 
        sys.exit(2) 
    
    for opt, arg in opts: 
        if opt in ("-h","--help"): 
            print("get_new_name.py -i <inputfile> -f <format>")
            print("-f prefix: new as default")
            sys.exit() 

        elif opt in ('-i', '--ifile'):
            inputfile = arg
        elif opt in ('-f', '--prefix'):
            prefix = arg
    
    inputfile = os.path.abspath(inputfile)
    dirname = os.path.dirname(inputfile)
    fname = inputfile.rsplit(os.sep)[-1]

    if not os.path.isfile(inputfile) or not os.path.isdir(dirname):
        sys.exit(2)

    ndirname = os.path.join(dirname, prefix)
    if not os.path.isdir(ndirname):
        os.mkdir(ndirname)

    l_fname = fname.split('.')
    nl_fname = l_fname[:-1]
    nl_fname.append('GBK')
    nl_fname.append(l_fname[-1])
    n_fname = '.'.join(nl_fname)

    print(os.path.join(dirname, prefix, n_fname))

if __name__ == '__main__':
    main(sys.argv[1:])

