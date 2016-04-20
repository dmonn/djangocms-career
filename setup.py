from setuptools import setup, find_packages
import os
import djangocms_career

REQUIREMENTS = [
    'Django>=1.6,<1.10',
    'django-cms>=3.0.12',
    'djangocms-text-ckeditor>=2.8.1',
    'python-dateutil>=2.5.2',
]

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

setup(
    author="Dominic Monn",
    author_email="monn.dominic@gmail.com",
    name='djangocms-career',
    version=djangocms_career.__version__,
    description='Django CMS Plugin to showcase a career or educational paths on portfolio and CV-Websites.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/dmonn/djangocms-career/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)