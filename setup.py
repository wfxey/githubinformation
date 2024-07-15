from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='githubinformation',
    version='1.0',
    packages=find_packages(),
    license='MIT',
    description='A tool that lets you check your GitHub Project for updates.',
    author='wfxey',
    author_email='projectsdi02@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/wfxey/githubinformation',
    download_url='https://github.com/wfxey/githubinformation/archive/refs/tags/v1.0.tar.gz',
    keywords=['updates', 'github', 'check-for-updates'],
    install_requires=[
        'requests',
        'packaging',
    ],
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
