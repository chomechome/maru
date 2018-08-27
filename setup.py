import codecs
import os
import re
import sys
import shutil

import setuptools

PACKAGE = 'maru'
ROOT = os.path.dirname(os.path.abspath(__file__))


def get_path(filename):
    return os.path.join(ROOT, filename)


def get_version():
    pattern = re.compile(r'__version__\s*=\s*\'(?P<version>\d+\.\d+\.\d+)\'')
    with codecs.open(get_path('{}/__init__.py'.format(PACKAGE))) as f:
        match = pattern.search(f.read())
        if match is not None:
            return match.group('version')

        raise ValueError('Version not found for package "{}"'.format(PACKAGE))


def get_description():
    with codecs.open(get_path('README.rst'), encoding='utf-8') as f:
        return '\n' + f.read()


def get_requirements():
    requirements = []

    with codecs.open(get_path('requirements.txt'), encoding='utf-8') as f:
        for requirement in f:
            if '#' in requirement:
                requirement, _, _ = requirement.partition('#')

            requirement = requirement.strip()
            if requirement and not requirement.startswith('-r '):
                requirements.append(requirement)

    return requirements


def get_extra_requirements():
    return {
        'gpu': [
            'tensorflow-gpu',
        ]
    }


class UploadCommand(setuptools.Command):
    """
    Support setup.py upload
    """
    description = 'Build the package and upload it to PyPI'
    user_options = []

    @staticmethod
    def _print_status(text):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(text))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self._print_status('Removing previous builds...')
        shutil.rmtree('dist', ignore_errors=True)

        self._print_status('Building source distribution...')
        os.system('{} setup.py sdist bdist_wheel'.format(sys.executable))

        self._print_status('Uploading the package to PyPi via Twine...')
        os.system('twine upload dist/*')

        self._print_status('Pushing git tags...')
        os.system('git tag v{}'.format(get_version()))
        os.system('git push --tags')

        sys.exit()


setuptools.setup(
    name=PACKAGE,
    version=get_version(),
    description='Morphological Analyzer for Russian',
    long_description=get_description(),
    author='Vladislav Blinov',
    author_email='cunningplan@yandex.ru',
    url='https://github.com/chomechome/maru',
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=get_requirements(),
    extras_require=get_extra_requirements(),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    cmdclass={
        'upload': UploadCommand,
    },
)
