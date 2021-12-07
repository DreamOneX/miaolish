import setuptools


setuptools.setup(
    name='miaolish',
    version='1.0.0',
    author='DreamOneX',
    description='Let\'s learn how to bark together',
    long_description=open('readme.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DreamOneX/miaolish',
    packages=[
        'miaolish',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'jieba>=0.42.1',
    ],
)
