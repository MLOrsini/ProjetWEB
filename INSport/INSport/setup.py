#! coding: utf-8
from setuptools import setup, find_packages
import os
import carrousel

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
]


setup(
    author = u'Pablo García',
    author_email = 'poli@devartis.com',
    name = 'django-carrousel',
    version = carrousel.get_version(),
    description = 'A django application that allows adding carrousel with slides on your web site.',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url = 'https://github.com/devartis/django-carrousel',
    packages = find_packages(),
    platforms = ['OS Independent'],
    license = 'Apache License',
    classifiers = CLASSIFIERS,
    install_requires = [
        'Django>=1.4',
	'south>=0.7.2',
        'django-positions>=0.5.2',
        'easy-thumbnails>=2.1',
    ],
    zip_safe = False,
)

