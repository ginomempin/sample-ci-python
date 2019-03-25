from setuptools import setup, find_namespace_packages

setup(
    name="myapp",
    package_dir={"" : "src"},
    packages=find_namespace_packages(where="src"),
    python_requires='>=3.5',
    install_requires=[
        "numpy"
    ],
    test_requires=[
        "pytest"
    ]
)
