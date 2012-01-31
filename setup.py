from setuptools import setup, find_packages
import os

version = '1.5'

setup(name='collective.recipe.modwsgi',
      version=version,
      description='WSGI from buildout',
      long_description=open('README.rst').read() + '\n' +
                       open(os.path.join('docs', 'HISTORY.txt')).read(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Buildout :: Recipe',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        ],
      keywords='wsgi buildout',
      author='Wichert Akkerman',
      author_email='wichert@wiggy.net',
      url='https://github.com/wichert/collective.recipe.modwsgi',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.recipe'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
          'zc.recipe.egg',
      ],
      entry_points='''
      [zc.buildout]
      default = collective.recipe.modwsgi:Recipe
      ''',
      )
