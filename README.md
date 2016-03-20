# tab-translator

CI tests: [![Build status](https://travis-ci.org/ograndedjogo/tab-translator.svg)](https://travis-ci.org/ograndedjogo/tab-translator/builds)

Code coverage: [![Coverage status](https://coveralls.io/repos/ograndedjogo/tab-translator/badge.svg?branch=develop&service=github)](https://coveralls.io/github/ograndedjogo/tab-translator)

This document is adressed to developpers.

## setup

Check the [travis configuration](.travis.yml) to setup the environment.
Main steps are:
 - clone the git repo `git clone https://github.com/ograndedjogo/tab-translator.git`
 - install requirements `pip install -r requirements.txt`
 - install opencv (see [install_opencv.sh](install_opencv.sh)) and its
   dependencies (see [travis build section _addons:apt:packages_](.travis.yml))

## run tests

tests, consider the [default pytest configuration](pytest.ini) for tabt
``` bash
py.test # tests only
coverage run -m py.test # produces coverage outputs
```

## run examples

``` bash
export PYTHONPATH=$PYTHONPATH:$PWD
python examples/cv2visu.py tests/images/score.jpg
python examples/scan.py tests/images/sheet.jpg
python examples/lines.py tests/images/score_croped.jpg
```
