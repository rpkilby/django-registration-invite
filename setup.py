import sys
from setuptools import setup, find_packages


# require pypandoc conversion for upload
if 'upload' in sys.argv[1:]:
    import pypandoc
    README = pypandoc.convert('README.md', 'rst')
else:
    README = open('README.md').read()


setup(
    name='django-registration-invite',
    version='0.0.1',
    description='HMAC-based invitation backend for django-registration',
    long_description=README,
    author='Ryan P Kilby',
    author_email='rpkilby@ncsu.edu',
    keywords='django-registration invitation invite',
    url='https://github.com/rpkilby/django-registration-invite/',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    license='BSD License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
