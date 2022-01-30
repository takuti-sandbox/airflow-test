from setuptools import setup, find_packages

setup(
    name='takuti',
    version='0.0.1',
    description='A package for testing custom Python modules for Apache Airflow',
    author='Takuya Kitazawa',
    author_email='k.takuti@gmail.com',
    license='MIT',
    url='https://github.com/takuti-sandbox/airflow-test/',
    packages=find_packages(exclude=['*tests*']),
    install_requires=['apache-airflow'],
)
