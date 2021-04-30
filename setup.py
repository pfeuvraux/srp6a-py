import os
from setuptools import (
  setup,
  find_packages
)

curr_dir = os.path.dirname(os.path.abspath(__file__))


setup(
  name="srp6a-py",
  version="0.0.1-dev",
  description="Just an easy-to-use SRP Python module",
  long_description="nope",
  license="WTFPL License",
  url=None,
  author="Paul Feuvraux",
  author_email="pfeuvraux@gmail.com",
  classifier=[
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Topic :: Security :: Cryptography"
  ],
  package_dir={"": "src"},
  packages=find_packages(where="src"),
  python_requires=">=3.8",
  #sinstall_requires=install_requirements,
  zip_safe=False,

)
