import os
import re
import setuptools


def read_version():
    # importing gpustat causes an ImportError :-)
    __PATH__ = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(__PATH__, 'nstu_client/__init__.py')) as f:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  f.read(), re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find __version__ string")


# get project version
__version__ = read_version()

# get project long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# get project requirements list
with open("requirements.txt", "r", encoding="utf-8") as fh:
    packages = fh.read().split("/n")

setuptools.setup(
    name="nstu-client",
    version=__version__,
    author='nstu.ru',
    author_email='nstudeveloper@nstu.ru',
    description="NSTU ModelRun tools package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.ria.com/neural/ria-modelhub-tools.git",
    packages=setuptools.find_packages(),
    install_requires=packages,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Operating System :: OS Independent",
    ],
    keywords='nstu nstu-client nstu-com nstu.ru nstu',
    entry_points={
        'console_scripts': ['nstu_client=nstu_client:main'],
    },
    python_requires='>=3.6'
)


# model_hub == start_model
# modelhub_client == nstu_client
# ModelHub == ModelRun
# ModelHubClientTest == ModelRunClientTest