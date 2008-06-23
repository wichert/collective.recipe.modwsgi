import logging
import os
import zc.buildout
from zc.recipe.egg.egg import Eggs

WRAPPER_TEMPLATE = """\
import sys
sys.path[0:0]= [
    %(syspath)s,
    ]

from paste.deploy import loadapp
application = loadapp("config:%(config)s")
"""

class Recipe:
    def __init__(self, buildout, name, options):
        self.buildout=buildout
        self.name=name
        self.options=options
        self.logger=logging.getLogger(self.name)

        
        if "config-file" not in options:
            self.logger.error("You need to specify either a paste configuration file")
            raise zc.buildout.UserError("No paste configuration given")



    def install(self):
        egg=Eggs(self.buildout, self.options["recipe"], self.options)
        reqs,ws=egg.working_set()
        path=[pkg.location for pkg in ws]

        output=WRAPPER_TEMPLATE % dict(
            config=self.options["config-file"],
            syspath=",\n    ".join((repr(p) for p in path))
            )

        location=os.path.join(self.buildout["buildout"]["parts-directory"],
                              self.name)
        if not os.path.exists(location):
            os.mkdir(location)
            self.options.created(location)

        target=os.path.join(location, "wsgi")
        f=open(target, "wt")
        f.write(output)
        f.close()
        os.chmod(target, 0755)
        self.options.created(target)

        return self.options.created()


    def update(self):
        self.install()

