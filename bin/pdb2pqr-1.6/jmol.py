#!@WHICHPYTHON@
"""
    Jmol applet generator
"""

__date__ = "5 July 2007"
__author__ = "Samir Unni"
__version__ = "0.0.1"
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
import cgi
import cgitb
import shutil
import sys
from .src.aconf import *
from sys import stdout


def jmolGen():
    """
        Write the contents of the (static) page containing the Jmol applet to a
        file, then output a dynamic page that redirects to that static page.
    """

    global jmolType
    file = stdout
    file.write("Content-type: text/html\n\n")
    cgitb.enable()

    form = cgi.FieldStorage()

    visType = form["vistype"].value
    jobid = form["jobid"].value
    pqrFileName = form["pqrfilename"].value
    scriptName = "myscript.spt"
    jmolPage = "jmol.html"
    jmolJsFile = "Jmol.js"
    jmolAppFile = "JmolApplet.jar"
    jmolColorMin = form["jmolcolormin"].value
    jmolColorMax = form["jmolcolormax"].value

    try:
        jmolType = form["jmoltype"].value
    except KeyError:
        pass

    dxFilePath = "%s-%s.dx" % (pqrFileName[:-4], jmolType)

    shutil.copyfile(jmolJsFile, '%s%s%s/%s' % (INSTALLDIR, TMPDIR, jobid, jmolJsFile))
    shutil.copyfile(jmolAppFile, '%s%s%s/%s' % (INSTALLDIR, TMPDIR, jobid, jmolAppFile))

    script = open('%s%s%s/%s' % (INSTALLDIR, TMPDIR, jobid, scriptName), 'w')
    script.write('load %s\n' % pqrFileName)
    script.write('isosurface s1 colorscheme bwr color absolute %s %s sasurface map \"%s\"\n' % (
        jmolColorMin, jmolColorMax, dxFilePath))
    script.write('write isosurface pot.jvxl')
    script.close()

    jmolpage = open('%s%s%s/%s' % (INSTALLDIR, TMPDIR, jobid, jmolPage), 'w')
    jmolpage.write('<html>\n')
    jmolpage.write('<head><script type=\"text/javascript\" src=\"%s\"></script>\n' % jmolJsFile)
    jmolpage.write('<title>Jmol visualization for %s</title>\n' % pqrFileName)
    jmolpage.write('<link href=\"../../pdb2pqr.css\" type=\"text/css\" rel=\"stylesheet\">\n')
    jmolpage.write('</head>\n')
    jmolpage.write('<body>\n')
    jmolpage.write(
        '<h3>Please be patient while the applet loads and while the surface is rendered and colored by electrostatic potential</h3>\n')
    jmolpage.write('<script type=\"text/javascript\">\n')
    jmolpage.write('jmolApplet(600, \"script myscript.spt\");\n')
    jmolpage.write('</script>\n')
    jmolpage.write(
        '<h3>You can perform simple operations like a MouseOver; or right-clicking on the biomolecule then making your selections.</h3>\n')
    jmolpage.write('<script type=\"text/javascript\">\n')
    jmolpage.write(
        'var gaJsHost = ((\"https:\" == document.location.protocol) ? \"https://ssl.\" : \"http://www.\");\n')
    jmolpage.write(
        'document.write(unescape(\"%3Cscript src=\'\" + gaJsHost + \"google-analytics.com/ga.js\' type=\'text/javascript\'%3E%3C/script%3E\"));\n')
    jmolpage.write('</script>\n')
    jmolpage.write('<script type=\"text/javascript\">\n')
    jmolpage.write('try {\n')
    jmolpage.write('var pageTracker = _gat._getTracker(\"UA-11026338-3\");\n')
    jmolpage.write('pageTracker._trackPageview();\n')
    jmolpage.write('} catch(err) {}</script>\n')
    jmolpage.write('</body>\n')
    jmolpage.write('</html>\n')

    jmolpage.close()

    sys.stdout.write('<html> <body>')
    sys.stdout.write('<meta http-equiv=\"refresh\" content=\"1;url=%s\">' % ('tmp/%s/%s' % (jobid, jmolPage)))
    sys.stdout.write('</body> </html>')
    sys.stdout.flush()


jmolGen()
