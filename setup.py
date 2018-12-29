from setuptools import setup
setup(name='noticeme',
      description=("Provides a framework for building watchers."
                   "Includes a watcher utility program "
                   "that allows you to create watchers declaratively."),
      url='https://github.com/bobbytrapz/noticeme',
      author='Bobby',
      author_email='bobbytrapz@protonmail.com',
      license='MIT',
      version='2018.12',
      py_modules=['noticeme'],
      python_requires='>=3.6',
      setup_requires=["cffi>=1.0.0"],
      install_requires=["cffi>=1.0.0"],
      cffi_modules=["noticeme/inotify_build.py:ffibuilder"],
      keywords='inotify watch development',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Python Modules',
          'Topic :: System :: Filesystems',
      ])
