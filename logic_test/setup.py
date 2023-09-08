from setuptools import setup, find_packages

setup(
    name='my_package',
    version='1.0',
    packages=find_packages(),
    install_requires=[
    ],
)

# $env:PYTHONPATH = "C:\Users\life\Desktop\logic_test;" + $env:PYTHONPATH (треба ввести в першу чергу, вказавши адресу папки з кодом my_code.py)

# pip install my_code встановлює як пакет

# python my_code.py запускає


# pip uninstall my_code видаляє