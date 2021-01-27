import setuptools
from os import path

current_dir = path.abspath(path.dirname(__file__))
with open(path.join(current_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="logtailtool",
    version="1.0.1",
    license='MIT',
    author="minyong-jeong",
    author_email="jmy3155@gmail.com",
    description="LogTailTool tail a log file in python",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/minyong-jeong/logtailtool",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
