import setuptools


def main():
    with open('README.md') as fp:
        readme = fp.read()

    setuptools.setup(
        name='jaggr',
        version='0.0.1',
        description='A fancy data aggregator for JSON-like objects.',
        long_description=readme,
        long_description_type='text/markdown',
        url='https://github.com/odashi/jaggr',
        author='Yusuke Oda',
        author_email='yus.takara@gmail.com',
        license='Apache Software License 2.0',
        classifieirs=[
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'Intended Audience :: Information Technology',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Topic :: Scientific/Engineering :: Information Analysis',
            'Topic :: Scientific/Engineering :: Mathematics',
            'Topic :: Utilities',
        ],
        keywords='json data aggregator',
        packages=['jaggr'],
        install_requires=[],
        python_requires='>=3.7',
    )


if __name__ == '__main__':
    main()
