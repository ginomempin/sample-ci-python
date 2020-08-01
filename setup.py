from setuptools import setup, find_namespace_packages

setup(
    name="myapp",
    version="0.0.1",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    python_requires=">=3.8",
    install_requires=["numpy"],
    test_requires=["pytest", "pytest-cov"],
)
