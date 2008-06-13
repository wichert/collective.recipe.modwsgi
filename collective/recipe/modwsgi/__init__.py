import logging
import os
import zc.buildout
from zc.recipe.egg.egg import Eggs

WRAPPER_TEMPLATE = """\
import sys
sys.path[0:0]=%(syspath)s

from paste.deploy import loadapp
application = loadapp("config:%(config)s")
"""

class Recipe(Eggs):
    def __init__(self, buildout, name, options):
        self.name=name
        self.options=options
        self.buildout=buildout
        self.logger=logging.getLogger(self.name)
        
        if "config-file" not in options:
            self.logger.error("You need to specify either a paste configuration file")
            raise zc.buildout.UserError("No paste configuration given")



    def install(self):
        # Set some variables to make zc.recipe.egg happy
        self.options["executable"]=self.buildout["buildout"]["executable"]
        self.options["eggs-directory"]=self.buildout["buildout"]["eggs-directory"]
        self.options["develop-eggs-directory"]=self.buildout["buildout"]["develop-eggs-directory"]

        reqs,ws=self.working_set()
        path=[pkg.location for pkg in ws]

        output=WRAPPER_TEMPLATE % dict(
            config=self.options["config-file"],
            syspath=repr(path)
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
        pass

