from setuptools import setup, find_packages
import os

version = '1.0rc1'

setup(name='collective.recipe.modwsgi',
      version=version,
      description="WSGI from buildout",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Zope Public License",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Wichert Akkerman',
      author_email='wichert@wiggy.net',
      url='',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.recipe'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
          'zc.recipe.egg',
      ],
      entry_points="""
      [zc.buildout]
      default = collective.recipe.modwsgi:Recipe
      """,
      )
