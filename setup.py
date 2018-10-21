from setuptools import setup, find_packages
import io,os,sys

def tag():
    return os.getenv("version")


def read_text_lines(fname):
    with io.open(fname) as fd:
        lines=fd.readlines()
        return ''.join(lines)


setup(
    name="word_cloud",
    version=tag(),
    packages=find_packages(),
    description='Word cloud of data scientist',
    long_description=open("README.md").read(),
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing :: Linguistic'
    ],
    author='kavgan',
    author_email='ganesan.kavita@gmail.com',
    license='Apache',
    url='https://github.com/kavgan/word_cloud',
    download_url='https://github.com/kavgan/word_cloud/archive/{0}.tar.gz'.format(tag()),
    keywords=['word cloud','visualization','text mining'],
    install_requires=[

    ],
    include_package_data=True,
    entry_points={

    }
)