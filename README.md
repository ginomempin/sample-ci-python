# Gitlab CI/CD Example for Python-based Apps

## CONTENTS

* [DEPENDENCIES](#dependencies)
* [SETUP](#setup)
* [USAGE](#usage)
* [TROUBLESHOOTING](#troubleshooting)
* [DOCUMENTATION](#documentation)

## DEPENDENCIES

* The main requirement to run the tests is [pytest](https://docs.pytest.org/en/latest/contents.html).
* For other example-specific dependencies, see [requirements.txt](./requirements.txt).

## SETUP

* Activate a virtual environment
* Install dependencies
    ```
    pip3 install -r requirements.txt

    ```
* Configure app installation in [setup.py](./setup.py)
* Configure test setup in [pytest.ini](./pytest.ini)

## USAGE

* Activate a virtual environment
* Install app in virtual env in [editable mode](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs)
    ```
    pip3 install -e .

    ```
* Run the tests
    ```
    pytest tests

    ```

## TROUBLESHOOTING

* pytest uses cached codes instead of latest
    * Clear the pytest cache with [--cache-clear](https://docs.pytest.org/en/latest/cache.html#clearing-cache-content)
    * Optionally, also [clear the generated *\_\_pycache\_\_*](https://stackoverflow.com/q/28991015/2745495)

## DOCUMENTATION

* [pytest](https://pytest.readthedocs.io/en/latest/contents.html)
    * [Invoking `pytest`](https://docs.pytest.org/en/latest/usage.html)
    * [Good Integration Practices](https://pytest.readthedocs.io/en/latest/goodpractices.html)
* Using *src*/*tests* layout
    * [How to Setup Files/Folders](https://docs.pytest.org/en/latest/goodpractices.html#tests-outside-application-code)
    * [How to Add *src* to *sys.path*](https://docs.python.org/3.5/distutils/setupscript.html#listing-whole-packages)
    * [How to Add *src/\** packages](https://setuptools.readthedocs.io/en/latest/setuptools.html#find-namespace-packages)
* Configuring `pytest`
    * [pytest.ini](https://docs.pytest.org/en/latest/reference.html#configuration-options)
