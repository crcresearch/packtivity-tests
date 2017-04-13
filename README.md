# Packtivity tests

Collection of functional tests for packtivity code developed by CRC (https://github.com/diana-hep/packtivity)
Note that some tests might be slow as they import and pull docker images
from dockerhub and external data preservation systems (i.e. CurateND)

# Prepare your system

This project requires umbrella, yadage and docker installed. Note that yadage not in requirements.txt - you
should install the version you'd like to test in your virtual environment from GitHub fork you are using, i.e.

```bash
pip install git+https://github.com/Baguage/yadage-schemas.git
pip install git+https://github.com/diana-hep/packtivity
```

To test your local version of packtivity, install it using develop command:

```python setup.py develop```

# Usage

1. Create new virtual environment

2. Install dependencies:

```pip install -r requirements.txt```

3. Run tests

```pytest```