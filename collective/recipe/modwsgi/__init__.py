import logging
import os
import stat
import zc.buildout
from zc.recipe.egg.egg import Eggs

WRAPPER_TEMPLATE = """\
import ConfigParser
import sys
syspaths = [
    %(syspath)s,
    ]

for path in reversed(syspaths):
    if path not in sys.path:
        sys.path[0:0]=[path]


from paste.deploy import loadapp

if sys.version_info >= (2, 6):
    from logging.config import fileConfig
else:
    from paste.script.util.logging_config import fileConfig


configfile = "%(config)s"
try:
    fileConfig(configfile)
except ConfigParser.NoSectionError:
    pass
application = loadapp("config:" + configfile)
"""


class Recipe:
    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.name = name
        self.options = options
        self.logger = logging.getLogger(self.name)

        if "config-file" not in options:
            self.logger.error(
                    "You need to specify either a paste configuration file")
            raise zc.buildout.UserError("No paste configuration given")

    def install(self):
        egg = Eggs(self.buildout, self.options["recipe"], self.options)
        reqs, ws = egg.working_set()
        path = [pkg.location for pkg in ws]
        extra_paths = self.options.get('extra-paths', '')
        extra_paths = extra_paths.split()
        path.extend(extra_paths)

        output = WRAPPER_TEMPLATE % dict(
            config=self.options["config-file"],
            syspath=",\n    ".join((repr(p) for p in path))
            )

        location = os.path.join(self.buildout["buildout"]["parts-directory"],
                              self.name)
        if not os.path.exists(location):
            os.mkdir(location)
            self.options.created(location)

        target = os.path.join(location, "wsgi")
        f = open(target, "wt")
        f.write(output)
        f.close()

        exec_mask = stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
        os.chmod(target, os.stat(target).st_mode | exec_mask)
        self.options.created(target)

        return self.options.created()

    def update(self):
        self.install()
