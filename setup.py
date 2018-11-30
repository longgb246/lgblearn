# -*- coding:utf-8 -*-

# dist    :  python setup.py sdist
# install    :  python setup.py install --record log
# uninstall  :  cat log | xargs rm －rf

import setuptools

with open('README.md', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

# 信息
DISTNAME = 'lgblearn'
AUTHOR = 'longgb246'
EMAIL = 'lgb453476610@163.com'
VERSION = '0.0.1'
DESCRIPTION = '''lgblearn for machine learning tools'''
LICENSE = 'MIT'
URL = 'https://github.com/longgb246/lgblearn'
DOWNLOAD_URL = URL
PYTHON_REQUIRES = '>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*'
PLATFORMS = 'any'
CLASSIFIERS = [
    # 'Development Status :: 5 - Production/Stable',
    # 'Environment :: Console',
    # 'Operating System :: OS Independent',
    # 'Intended Audience :: Science/Research',
    # 'Programming Language :: Python',
    # 'Programming Language :: Python :: 2',
    # 'Programming Language :: Python :: 3',
    # 'Programming Language :: Python :: 2.7',
    # 'Programming Language :: Python :: 3.5',
    # 'Programming Language :: Python :: 3.6',
    # 'Programming Language :: Python :: 3.7',
    # 'Programming Language :: Cython',
    # 'Topic :: Scientific/Engineering',

    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish (should match 'license' above)
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2',
    # 'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    # 'Programming Language :: Python :: 3',
    # 'Programming Language :: Python :: 3.5',
    # 'Programming Language :: Python :: 3.6',
    # 'Programming Language :: Python :: 3.7',
    'Programming Language :: Cython',
    'Operating System :: OS Independent',
]

# 其他要求
# numpy 版本等
min_numpy_ver = '1.12.0'
SETUPTOOLS_KWARGS = {
    'install_requires': [
        'python-dateutil >= 2.5.0',
        'pytz >= 2011k',
        'numpy >= {numpy_ver}'.format(numpy_ver=min_numpy_ver),
    ],
    'setup_requires': ['numpy >= {numpy_ver}'.format(numpy_ver=min_numpy_ver)],
    'zip_safe': False,
}

# 安装
setuptools.setup(
    name=DISTNAME,
    version=VERSION,
    maintainer=AUTHOR,
    author=AUTHOR,
    maintainer_email=EMAIL,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url=URL,
    download_url=DOWNLOAD_URL,
    packages=setuptools.find_packages(include=['lgblearn', 'lgblearn.*']),
    # packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    # py_modules=['six'],  # 剔除不属于包的单文件Python模块
    # install_requires=['peppercorn'],  # 指定项目最低限度需要运行的依赖项
    # package_data={'': ['templates/*', '_libs/*.dll']},
    # package_data={
    #     'sample': ['package_data.dat'],
    # },  # 包数据，通常是与软件包实现密切相关的数据
    classifiers=CLASSIFIERS,
    platforms=PLATFORMS,
    python_requires=PYTHON_REQUIRES,
    # python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',  # python的依赖关系
    # **SETUPTOOLS_KWARGS
)
