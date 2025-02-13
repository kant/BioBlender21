#!/usr/bin/python
"""
Driver for PDB2PQR

This module takes a PDB file as input and performs optimizations
before yielding a new PDB-style file as output.

Ported to Python by Todd Dolinsky (todd@ccb.wustl.edu)
Washington University in St. Louis

Parsing utilities provided by Nathan A. Baker (baker@biochem.wustl.edu)
Washington University in St. Louis

Copyright (c) 2002-2010, Jens Erik Nielsen, University College Dublin;
Nathan A. Baker, Washington University in St. Louis; Paul Czodrowski &
Gerhard Klebe, University of Marburg

All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.
* Neither the names of University College Dublin, Washington University in
St. Louis, or University of Marburg nor the names of its contributors may
be used to endorse or promote products derived from this software without
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.

"""

__date__ = "5 April 2010"
__author__ = "Todd Dolinsky, Nathan Baker, Jens Nielsen, Paul Czodrowski, Jan Jensen, Samir Unni, Yong Huang"
__version__ = "1.6"

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from main import mainCommand
from main_cgi import mainCGI
from src.aconf import *

if __name__ == "__main__":
    """ Determine if called from command line or CGI """

    if not ("REQUEST_METHOD" in os.environ):
        # Append Numeric/Numpy path to sys.path if the user specified a non-standard location during configuration
        package_path = PACKAGE_PATH
        if package_path != "":
            sys.path.extend(package_path.split(":"))
        mainCommand(sys.argv)
    else:
        mainCGI()

