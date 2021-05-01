# srp-6a

This Python module provides SRP tools.

:warning: **YOU NEED TO INSTALL [restless](http://github.com/pfeuvraux/restless) first! :warning:

# Implementation details

This SRP implementation hardens SRP-6a version:

* Secret generation: scrypt instead of SHA1 (with github.com/pfeuvraux/restless). The plan is to use argon2id in the future.
* Hashing: SHA384.

# Usage

Please, see `tests/test_e2e.py` to see how to use it.
