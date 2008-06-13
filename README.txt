Introduction
============

''collective.recipe.modwsgi'' is a `zc.buildout`_ recipe which creates
a `paste.deploy`_ entry point for mod_wsgi_.

It is very simple to use. This is a minimal ''buildout.cfg'' file
which creates a WSGI script mod_python can use::

    [buildout]
    parts = mywsgiapp

    [mywsgiapp]
    recipe = collective.recipe.modwsgi
    eggs = mywsgiapp
    config-file = ${buildout:directory}/production.ini

This will create a small python script in parts/mywsgiapp called
''wsgi'' which mod_python can load.

The apache configuration for this buildout looks like this:::

    WSGIScriptAlias /mysite /home/me/buildout/parts/mywsgiapp/wsgi

    <Directory /home/me/buildout>
        Order deny,allow
        Allow from all
    </Directory>

This recipe does not fully install packages, which means that console scripts
will not be created. If you need console scripts you can add a second
buildout part which uses `zc.recipe.egg`_ or `repoze.recipe.egg`_ to do
a full install.

.. _zc.buildout: http://pypi.python.org/pypi/zc.buildout
.. _paste.deploy: http://pythonpaste.org/deploy/
.. _mod_wsgi: http://code.google.com/p/modwsgi/
.. _zc.recipe.egg: http://pypi.python.org/pypi/zc.recipe.egg
.. _repoze.recipe.egg: http://pypi.python.org/pypi/repoze.recipe.egg

