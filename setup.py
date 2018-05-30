from distutils.core import setup
import os

description = "django api email backend"

long_description = (
)

def get_version():
    for line in open('apiemail/__version__.py'):
        if 'version' in line:
            return line.split('=')[1].strip(' \n\'"')
    raise Error("No version")

setup(
    author="Sebastien Roy",
    author_email="info@leansystems.co",
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python",
        "Topic :: Office/Business",
        "Topic :: Utilities"
    ],
    description=description,
    long_description=long_description,
    name='django-apiemail',
    packages=['apiemail'],
    url="https://github.com/choh3Vuc/django-apiemail.git",
    version=get_version(),
    install_requires=[
        'django',
        'sendgrid-python',
        'google-api-python-client',
        ]
)
