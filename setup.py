from setuptools import setup

setup(
    name='doxystub',
    maintainer="Grégoire Passault",
    maintainer_email="g.passault@gmail.com",
    description="Stubs generator based on Doxygen+Boost.Python",
    url="https://github.com/rhoban/doxystub",
    version="0.0.1",
    long_description=open("README.md").read(),
    license="MIT",
    entry_points={'console_scripts': 'doxystub = doxystub.doxystub:main'},
    packages=['doxystub']
)
