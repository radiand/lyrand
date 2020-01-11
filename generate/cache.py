import hashlib
import os
import pickle
from functools import wraps
from typing import Optional


def md5sum(path, blocksize=65536):
    hashsum = hashlib.md5()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(blocksize), b""):
            hashsum.update(block)
    return hashsum.hexdigest()


class Cache:
    """Naive function call cache between script runs. If enabled, it stores function returns on
    disk and loads them next time.
    """

    # Stores information whether cache was enabled via CLI.
    enabled = False

    # Stores information whether input file is the same as it was on last script run.
    # input file is e.g. JSON file with lyrics passed via CLI.
    possible = False

    cache_path = "/tmp"

    @classmethod
    def setup(cls, cache_path: str, input_path: str):
        """When called, it assumes that cache feature is enabled and allows all decorators to
        operate.

        Args:
            cache_path: a path where MD5 checksums and cached pickles are stored
            input_path: a path to file which contains data to process, "a source of truth". Cache
                class calculates MD5 checksum on this file and compare it with already stored one.

        """
        cls.enabled = True
        cls.cache_path = cache_path

        new_checksum = md5sum(input_path)
        old_checksum = cls._load_input_checksum(os.path.join(cache_path, "last.md5"))

        if new_checksum == old_checksum:
            cls.possible = True
        else:
            os.makedirs(cache_path, exist_ok=True)
            with open(cls._md5path(), "w") as f:
                f.write(new_checksum)

    @classmethod
    def by_function_name(cls, fn):
        """Actual decorator. If cache is enabled, it will return unpickled result from last call of
        decorated function. BE AWARE: it is unaware of passed args and kwargs - if fn name matches,
        results are unpickled.
        """
        @wraps(fn)
        def wrapper(*args, **kwargs):
            fn_name = fn.__name__
            if cls.enabled and cls.possible and os.path.isfile(cls._picklepath(fn_name)):
                obj = None
                with open(cls._picklepath(fn_name), "rb") as input_picklefile:
                    obj = pickle.load(input_picklefile)
                return obj
            ret = fn(*args, **kwargs)
            with open(cls._picklepath(fn_name), "wb") as output_picklefile:
                pickle.dump(ret, output_picklefile)
            return ret
        return wrapper

    @staticmethod
    def _load_input_checksum(path: str) -> Optional[str]:
        if os.path.isfile(path):
            with open(path) as f:
                return f.read()
        return None

    @classmethod
    def _picklepath(cls, fn_name):
        return os.path.join(cls.cache_path, fn_name + ".pickle")

    @classmethod
    def _md5path(cls):
        return os.path.join(cls.cache_path, "last.md5")
