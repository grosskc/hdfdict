# -- coding: utf-8 --
"""hdfdict helps h5py to dump and load python dictionaries

If you have a hierarchical data structure of numpy arrays in a
dictionary for example, you can use this tool to save this
dictionary into a h5py `File()` or `Group()` and load it again.
This tool just maps the hdf `Groups` to dict `keys` and
the `Datset` to dict `values`.
Only types supported by h5py can be used.
The dicitonary-keys need to be strings until now.

Example
-------

```python
import numpy as np
import hdfdict

d = {
        'testdata': np.random.randn(10),
        'b': np.sin(np.linspace(0, 10))
}

hdf = hdfdict.dump(d, 'test.h5')

res = hdfdict.load(hdf)

print(res)

```


"""

from .hdfdict import load, dump

# Get version from package metadata
# importlib.metadata is available in Python 3.8+ (we require 3.9+)
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version('hdfdict')
except PackageNotFoundError:
    # Fallback for when package is not installed (e.g., development mode)
    __version__ = '0.3.1'

__all__ = ['load', 'dump']
