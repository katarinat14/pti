from setuptools import setup, find_packages

setup(
    name="pti",
    version="0.01",
    packages=find_packages(),
    author="Katarina Topolic, Milica Lapov",
    author_email="katarinatopolic@gmail.com",
    install_requires=[
        # Add your project dependencies here, e.g., 'requests', 'numpy'
    ],
    description="A short description of your project",
    long_description=open("README.md").read()
)