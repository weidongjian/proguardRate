#!/usr/bin/env python
# coding=utf-8
from setuptools import setup

setup(
    name='proguard_rate',
    version='0.1',
    author='weidongjian',
    author_email='weidongjian@gmail.com',
    url='https://github.com/weidongjian/proguardRate',
    description="计算代码混淆率",
    long_description="计算代码混淆率",
    long_description_content_type="text/markdown",
    python_requires='>=3',
    packages=['proguard_rate'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'proguard_rate=proguard_rate:proguard_rate'
        ]
    }
)