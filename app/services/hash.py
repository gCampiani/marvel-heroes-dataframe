import hashlib

from decouple import config


def build_hash(ts, private_key=config("PRIVATE_API_KEY"), public_key=config("PUBLIC_API_KEY")):
    return hashlib.md5(f'{ts}{private_key}{public_key}'.encode("UTF-8")).hexdigest()
    