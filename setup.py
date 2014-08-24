from setuptools import setup, find_packages

version = '0.1'

setup(name='thoreg_dojo',
      version=version,
      description="The coding dojo of Thoreg",
      long_description="""\
Some programming examples and reminder - coding for fun and profit""",
      classifiers=['Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Software Development :: User Interfaces'],
      keywords='dojo, thoreg, examples, flask, behave, tests',
      author='Thomas Rega',
      author_email='thoreg@gmail.com',
      url='https://github.com/thoreg/dojo',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['behave',
                        'coveralls',
                        'Flask',
                        'Flask-WTF',
                        'pytest',
                        'pytest-cov',
                        'watchdog'],
      )
