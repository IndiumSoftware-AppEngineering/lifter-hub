from setuptools import setup, find_packages

setup(
    name="lifter-hub",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "psycopg2-binary",  # PostgreSQL driver
    ],
    python_requires=">=3.11",
)
