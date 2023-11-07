# Notes

You can use miniconda to install via a gazillion youtube videos or the offical docs [here](https://developer.apple.com/metal/tensorflow-plugin/)


# My approach

```
$ cd notebooks/nbenv
$ mkdir metalenv
$ cd metalenv
# this will install to root dir
#$ python3 -m venv ~/venv-metal
# this will install to this dir
$ python3 -m venv venv-metal
# go up a dir
$ cd ..
# activate the env
$ source nbenv/venv-metal/bin/activate
# update pip
# Note at this point, python and python3 are equivalent.
(venv-metal) $ python -m pip install -U pip
# install base tensorflow
$ python -m pip install tensorflow
# install metal tensorflow
$ python -m pip install tensorflow-metal
```

#### Install the base modules

#### Manually

```
$ python -m pip install pandas
$ python3 -m pip install scikit-learn
```

#### Requirements.txt

```
$ pip install  -r requirements.txt
```

# Test it

## From Jeff Heatons Git

Shamelessly ripped off from

* [repo](https://github.com/jeffheaton/t81_558_deep_learning)
* [platform dump](https://github.com/jeffheaton/t81_558_deep_learning/blob/master/install/tensorflow-install-march-2023.ipynb)



Jeff's mod is out of date so use this one.  Keras no longer has a version.  Its part of tensorflow.

```
# python platform status
import sys

from tensorflow import keras
import pandas as pd
import sklearn as sk
import tensorflow as tf

print(f"Tensor Flow Version: {tf.__version__}")
print()
print(f"Python {sys.version}")
print(f"Pandas {pd.__version__}")
print(f"Scikit-Learn {sk.__version__}")
gpu = len(tf.config.list_physical_devices('GPU'))>0
print("GPU is", "available" if gpu else "NOT AVAILABLE")
```

Make sure it prints GPU is available.

```
(venv-metal)  $ scripts> python3 platform_testy.py
Tensor Flow Version: 2.14.0

Python 3.9.6 (default, Sep 26 2022, 11:37:49)
[Clang 14.0.0 (clang-1400.0.29.202)]
Pandas 2.1.2
Scikit-Learn 1.3.2
GPU is available
```


# vscode on macOS vs vscode on github codespaces

I do not truly understand why sometimes I can get reuse
of existing environements versus creating new ones.  If
you are in some weird state where the terminal is on one venv
and the notebooks are in a different one, deactivate the terminal
environment.

```
$ deactivate
```

Then switch to the venv created by vscode notebooks.

```
# from the root of the git repo
$ source ./.venv/bin/activate
(.venv) $ pip install tensorflow-metal
```

The above hack is so that github codespaces and gcp flask App Engine
do not need a separate requirements.txt.