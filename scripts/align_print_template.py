#!/usr/bin/env python

"""
Read an alignment from stdin and for each block print the result of 
evaluating `template_string` (in cheetah template format). The alignment
block will be place of the template context as `a` and the list of components
as `c`.

usage: %prog template [options]
    -f, --format = maf: Input format, maf (default) or axt
"""

from __future__ import division

import psyco_full

import sys
import cookbook.doc_optparse
from bx import align

from Cheetah.Template import Template

def main():

    # Parse command line arguments
    options, args = cookbook.doc_optparse.parse( __doc__ )

    try:
        template = Template( args[0] )
        format = options.format
        if not format: format = "maf"
    except:
        cookbook.doc_optparse.exception()

    reader = align.get_reader( format, sys.stdin ) 

    for a in reader: 
        template.a = a
        template.c = a.components
        print template

if __name__ == "__main__": 
	main()