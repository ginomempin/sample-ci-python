# Gitlab CI/CD Example for Python-based Apps

![pipeline status][1] ![coverage report][2]

## CONTENTS

* [DEPENDENCIES](#dependencies)
* [SETUP](#setup)
* [USAGE](#usage)
* [ISSUES](#issues)
* [DOCUMENTATION](#documentation)

## DEPENDENCIES

* Python-specific
    * [distutils](https://docs.python.org/3.8/distutils/introduction.html)
        * For installing the sample `src/app` module into the Python environment
        * This facilitates importing the app-under-test modules in `tests` codes
        * The alternative to not using this is to append `src/app` to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path)
    * [pytest](https://docs.pytest.org/en/latest/contents.html)
        * For creating and running the tests
    * [pytest-cov](https://github.com/pytest-dev/pytest-cov)
        * For gathering and reporting code coverage
    * For other example-specific dependencies, see [requirements.txt](./requirements.txt).
* Gitlab-specific
    * Access to a Gitlab instance
    * Access to a build/test/server PC for [`gitlab-runner`](https://docs.gitlab.com/runner/)

## SETUP

* Configure the `app` installation in [setup.py](./setup.py) ([reference](https://docs.python.org/3.8/distutils/setupscript.html#writing-the-setup-script))
* Configure the `tests` configuration in [pytest.ini](./pytest.ini) ([reference](https://docs.pytest.org/en/stable/reference.html#ini-options-ref))
* Configure the coverage collection in [.coveragerc](./coveragerc) ([reference](https://coverage.readthedocs.io/en/latest/config.html))
* Setup a local testing environment
    * Using a **virtual environment**
        * Create/Activate a virtual environment
            ```none
            $ python3.8 -m venv "~/.venvs/samples"
            $ source ~/.venvs/samples/bin/activate
            (samples) $ python -V
            Python 3.8.5

            ```
        * Install dependencies
            ```none
            (samples) $ pip install -r requirements.txt

            ```
        * Install the `app` as a module in [editable mode](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs)
            ```none
            (samples) $ pip install -e .
            (samples) $ python
            ...
            >>> from app.models.stack import Stack
            >>> ss = Stack()

            ```
    * Using a **Docker** container
        * Build a Docker image using the [Dockerfile](./Dockerfile)
            ```none
            $ docker build --tag sample-ci-python:3.8 .

            ```
        * Start the container
            ```none
            $ docker run -it sample-ci-python:3.8 /bin/bash
            root@7648c3c82d32:/workspace#
            root@27f8a8b7be41:/workspace# ls -al
            total 36
            drwxr-xr-x 1 root root 4096 Aug  1 07:16 .
            drwxr-xr-x 1 root root 4096 Aug  1 07:16 ..
            -rw-r--r-- 1 root root   66 Aug  1 06:11 .coveragerc
            -rw-r--r-- 1 root root  266 Aug 12  2019 .gitlab-ci.yml
            -rw-r--r-- 1 root root  223 Aug  1 06:27 pytest.ini
            -rw-r--r-- 1 root root  393 Aug  1 06:09 requirements.txt
            -rw-r--r-- 1 root root  288 Aug  1 05:57 setup.py
            drwxr-xr-x 1 root root 4096 Aug  1 06:14 src
            drwxr-xr-x 3 root root 4096 Aug  1 05:56 tests
            root@27f8a8b7be41:/workspace# python
            Python 3.8.2 (default, Feb 26 2020, 14:58:38)
            [GCC 8.3.0] on linux
            Type "help", "copyright", "credits" or "license" for more information.
            >>> from app.models.stack import Stack
            >>> ss = Stack()

            ```
* Setup Gitlab CI
    * [Install a Gitlab Runner](https://docs.gitlab.com/runner/install/) on a publicly-accessible machine
    * [Register the Runner](https://docs.gitlab.com/runner/register/index.html) with your Gitlab instance
        * Get the coordinator URL and registration tokens:
            * For shared runners: <http://your/gitlab/instance/admin/runners>
            * For project-specific runners: <http://your/gitlab/project/settings/ci_cd>
        * Use [Docker as the executor](https://docs.gitlab.com/runner/executors/docker.html) (see [ISSUES](#issues) section on possible disk space issue)
        * Set project-specific [tags](https://docs.gitlab.com/ee/ci/runners/#using-tags)
    * Configure the CI configuration in [.gitlab-ci.yml](./.gitlab-ci.yml)
        * Set which Docker [image](https://docs.gitlab.com/runner/executors/docker.html#the-image-keyword) and [services](https://docs.gitlab.com/runner/executors/docker.html#the-services-keyword) to use
        * Set the [tags](https://docs.gitlab.com/ee/ci/runners/#using-tags)
        * Set the commands for `before_script` and `script`
        * For other configurations, see [GitLab CI/CD Pipeline Configuration Reference](https://docs.gitlab.com/ee/ci/yaml/)
    * Configure the Gitlab Runner at *Gitlab project* > *Settings* > *CI/CD*
        * Select *Disable AutoDevOps* to explicitly require *.gitlab-ci.yml*
        * Enable the runner only for "important" commits
            * Enable only on tagged jobs
            * Enable only on protected branches (ex. `develop`, `master`)
        * Set other options such as *Timeout*, *Custom CI config path*, and *Triggers*
        * Sample Configuration:
            ![Sample Configuration](./docs/sample-ci-runner.png)

## USAGE

* Run the tests
    * From the **virtual environment** or from the **Docker container**
        ```
        $ python -m pytest
        ==================== test session starts ====================
        platform linux -- Python 3.8.2, pytest-6.0.1, py-1.9.0, pluggy-0.13.1 -- /usr/local/bin/python
        cachedir: .pytest_cache
        rootdir: /workspace, configfile: pytest.ini, testpaths: tests
        plugins: cov-2.10.0
        collected 3 items

        tests/model_tests/stack_test.py::constructor_test PASSED    [1/3]
        tests/model_tests/stack_test.py::push_test PASSED           [2/3]
        tests/model_tests/stack_test.py::pop_test PASSED            [3/3]

        ----------- coverage: platform linux, python 3.8.2-final-0 -----------
        Name                         Stmts   Miss Branch BrPart  Cover
        --------------------------------------------------------------
        src/app/__init__.py              0      0      0      0   100%
        src/app/models/__init__.py       0      0      0      0   100%
        src/app/models/stack.py         12      0      0      0   100%
        --------------------------------------------------------------
        TOTAL                           12      0      0      0   100%
        Coverage HTML written to dir coverage


        ==================== 3 passed in 0.08s ==========================

        ```
    * From Gitlab
        * Make changes to the codes in *src/app* and/or in *tests*
        * Make changes to the [.gitlab-ci.yml](./.gitlab-ci.yml) configuration (if necessary)
        * Commit the changes then push to Gitlab
        * Go to your *Gitlab project* > *CI/CD* > *Pipelines*
        * Select the currently *running* job to view progress/result
* Get the code coverage report
    * From the generated *coverage* directory in the same level as *src* and *tests*
    * From the downloadable [artifacts](https://docs.gitlab.com/ee/ci/pipelines/job_artifacts.html) of the CI job

## ISSUES

* `pytest` uses cached codes instead of latest
    * Clear the `pytest` cache with [--cache-clear](https://docs.pytest.org/en/latest/cache.html#clearing-cache-content)
    * Optionally, also [clear the generated *\_\_pycache\_\_*](https://stackoverflow.com/q/28991015/2745495)
* "*This job is stuck, because you don’t have any active runners that can run this job.*"
    * Make sure that the *.gitlab-ci.yml* has the correct tags
    * Make sure the `gitlab-runner` service is running
    * Make sure the machine running `gitlab-runner` is accessible by the Gitlab instance
* "*yaml invalid*"
    * Go to the *Gitlab project* > *CI/CD*
    * On the top-right portion, click the *CI Lint* button
    * Paste the contents of *gitlab-ci.yml* file and validate
* The jobs are not running on the same runner/environment
    * Example: 1 job for build, 1 job for tests
    * As of now, Gitlab CI does not support this:
        * [Sticky Runners](https://gitlab.com/gitlab-org/gitlab-ce/issues/29447)
        * [Caching general build artifacts between stages](https://gitlab.com/gitlab-org/gitlab-runner/issues/336)
        * [Force all pipeline jobs to execute on same concurrent runner](https://gitlab.com/gitlab-org/gitlab-ce/issues/30060)
    * The current workaround now is to use `before_script` to build and a job for tests
* The `gitlab-runner` is leaving a lot of `-cache-` containers/volumes
    * See a [discussion](https://gitlab.com/gitlab-org/gitlab-runner/issues/2980#note_106845694) of this behavior here
    * Possible solutions:
        * Manually regularly run `docker system prune`
        * Setup a `cron` job `docker system prune -f`
            ```
            # Cleanup docker containers/volumes every 3am every monday
            0 3 * * 1 /usr/bin/docker system prune -f

            ```

## DOCUMENTATION

* On Setting-Up the App with `distutils`
    * [Writing the Setup Script](https://docs.python.org/3.8/distutils/setupscript.html#writing-the-setup-script)
* On Setting-Up the Tests with [pytest](https://pytest.readthedocs.io/en/latest/contents.html)
    * [Configuration Options](https://docs.pytest.org/en/stable/reference.html#ini-options-ref)
    * [Invoking `pytest`](https://docs.pytest.org/en/latest/usage.html)
    * [Good Integration Practices](https://pytest.readthedocs.io/en/latest/goodpractices.html)
    * [How to Setup Files/Folders](https://docs.pytest.org/en/latest/goodpractices.html#tests-outside-application-code)
    * [How to Add *src* to *sys.path*](https://docs.python.org/3.5/distutils/setupscript.html#listing-whole-packages)
    * [How to Add *src/\** packages](https://setuptools.readthedocs.io/en/latest/setuptools.html#find-namespace-packages)
* On Setting-Up code coverage with [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/readme.html)
    * [Configuration Reference](https://coverage.readthedocs.io/en/latest/config.html)
* On Setting-Up Gitlab CI
    * [Getting started with GitLab CI](http://192.168.1.61/help/ci/quick_start/README)
    * [Installing a Gitlab Runner](https://docs.gitlab.com/runner/install/)
    * [Registering a Gitlab Runner](https://docs.gitlab.com/runner/register/index.html)
    * [Configuring a Gitlab Runner](https://docs.gitlab.com/runner/#configuring-gitlab-runner)
    * [.gitlab-ci.yml Reference](https://docs.gitlab.com/ee/ci/yaml/README.html)
    * [Job Artifacts](https://docs.gitlab.com/ee/ci/pipelines/job_artifacts.html)
* On Setting-Up a Docker Registry
    * [Deploy a registry server](https://docs.docker.com/registry/deploying/)
    * [Test an insecure registry](https://docs.docker.com/registry/insecure/)

[1]: http://url/to/gitlab/instance/sample-ci-python/badges/master/pipeline.svg
[2]: http://url/to/gitlab/instance/sample-ci-python/badges/master/coverage.svg
