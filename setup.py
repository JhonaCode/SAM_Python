from setuptools import find_packages, setup
#setup(
#    name='sam_python',
#    packages=find_packages(),
#    version='0.1.0',
#    description='My first Python library',
#    author='Me',
#    license='MIT',
#)

setup(
    name='sam_python',
    packages=find_packages(),
    version='0.0.4',
    description='sam_python',
    author='Jhonatan A. A. Manco',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='test',
)
