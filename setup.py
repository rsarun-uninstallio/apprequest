from distutils.core import setup
setup(
  name = 'apprequest',
  packages = ['apprequest'],
  version = '0.1',
  license='MIT',
  description = 'AppRequest - Maintains a unique ID to track every operation',
  author = 'arun.rs',
  author_email = 'arunrs@uninstall.io',
  url = 'https://github.com/rsarun-uninstallio/apprequest',
  download_url = 'https://github.com/rsarun-uninstallio/apprequest/archive/v0.1.tar.gz',
  keywords = ['scraping', 'easy', 'scraper', 'website', 'download', 'links', 'images', 'videos'],
  install_requires=['uuid'],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2.7',
  ],
)