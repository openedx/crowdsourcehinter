"""Setup for Crowdsource Hinter XBlock."""

from __future__ import absolute_import
import os
from setuptools import setup

with open('README.md') as a:
    long_description = a.read()


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.
    Returns a list of requirement strings.
    """
    requirements = set()
    for path in requirements_paths:
        with open(path) as reqs:
            requirements.update(
                line.split('#')[0].strip() for line in reqs
                if is_requirement(line.strip())
            )
    return list(requirements)


def is_requirement(line):
    """
    Return True if the requirement line is a package requirement;
    that is, it is not blank, a comment, a URL, or an included file.
    """
    return line and not line.startswith(('-r', '#', '-e', 'git+', '-c'))


setup(
    name='crowdsourcehinter-xblock',
    version='0.6',
    description='crowdsourcehinter XBlock',  # TODO: write a better description.
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[
        'crowdsourcehinter',
    ],
    install_requires=load_requirements('requirements/base.in'),
    entry_points={
        'xblock.v1': [
            'crowdsourcehinter = crowdsourcehinter:CrowdsourceHinter',
        ]
    },
    package_data=package_data("crowdsourcehinter", ["static", "public"]),
    keywords='crowdsourcehinter xblock',
    url='https://github.com/edx/crowdsourcehinter',
    author='edX',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
