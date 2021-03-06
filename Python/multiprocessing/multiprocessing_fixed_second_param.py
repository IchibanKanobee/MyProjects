#https://stackoverflow.com/questions/5442910/python-multiprocessing-pool-map-for-multiple-arguments

import multiprocessing
from functools import partial
from contextlib import contextmanager

@contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()

def merge_names(a, b):
    return '{} & {}'.format(a, b)

if __name__ == '__main__':
    names = ['Brown', 'Wilson', 'Bartlett', 'Rivera', 'Molloy', 'Opie']
    with poolcontext(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(partial(merge_names, b='Sons'), names)
    print(results)
