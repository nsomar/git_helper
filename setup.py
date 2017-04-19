from setuptools import setup, find_packages

setup(
    name='ghl',
    version='0.1',
    description='Github helper',
    url='https://github.com/oarrabi/git_helper.git',
    author='Omar Abdelhafith',
    author_email='o.arrabi@me.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'click',
        'GitPython',
        'arrow'
    ],
    entry_points={
        'console_scripts': [
            'ghl=github_helper.bin:cli',
        ],
    }
)
