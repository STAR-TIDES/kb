''' star_tides.utils.random_string
'''
import secrets
from star_tides.constants import ALPHABET


def gen_rand_n_str(n: int) -> str:
    return ''.join(secrets.choice(ALPHABET) for i in range(n))
