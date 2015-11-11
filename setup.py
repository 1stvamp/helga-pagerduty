from setuptools import setup, find_packages

version = '1.0.0'

setup(name="helga-pagerduty",
      version=version,
      description=('PagerDuty webhook handler for helga'),
      classifiers=['Development Status :: 1 - Beta',
                   'Environment :: IRC',
                   'Intended Audience :: Twisted Developers, IRC Bot Developers',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: IRC Bots'],
      keywords='irc bot pagerduty webhooks',
      author='Wes Mason',
      author_email='wes@1stvamp.org',
      license='GPLv3',
      packages=find_packages(),
      include_package_data=True,
      py_modules=['helga-pagerduty'],
      zip_safe=True,
      entry_points = dict(
          helga_webhooks = [
              'pagerduty= helga_pagerduty:announce',
          ],
      ),
)
