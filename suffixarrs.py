import math
import struct
import stringsort as ssort
from collections import OrderedDict 

def test_func(f):
    """Run f's doctests."""
    import doctest
    doctest.run_docstring_examples(f, globals())

def suffixes(S, term=True):
    """Get suffixes of string S. Ordered by suffix ID. If TERM param set, append terminator '$' to all suffixes.
    >>> S = 'banana'
    >>> suffixes(S)
    ['banana$', 'anana$', 'nana$', 'ana$', 'na$', 'a$', '$']
    >>> suffixes(S, term=False)
    ['banana', 'anana', 'nana', 'ana', 'na', 'a', '']
    """
    suffs = []
    for i in range(len(S)):
        suffs.append(S[i:])
    suffs.append('')
    if term:
        return [suff + '$' for suff in suffs]
    else:
        return suffs

def suffix_arr_mergesort(S, term=True, one_indexed=True):
    """Return suffix array for S with O(n^2 * logn) runtime, using mergesort.
    >>> suffix_arr_mergesort('abaab',term=False, one_indexed=False)
    [2, 3, 0, 4, 1]
    """
    suffs = suffixes(S, term)
    suffix_ids = [(suffs[i], i+1) for i in range(len(suffs))] #To retain indices. 
    sorted_suffs = ssort.mergesort(suffix_ids)
    strs_and_ids = list(zip(*sorted_suffs))
    strs, ids = list(strs_and_ids[0]), list(strs_and_ids[1])

    if not term: #Drop the terminator suffix '$', which will always be first lexicographically
        ids.pop(0)
    if not one_indexed:
        return [i-1 for i in ids]
    return ids #1-INDEXED

def suffix_arr_radixsort(S, term=True, one_indexed=True):
    """Return suffix array for S with O(n*logn) runtime, 
    given maximal string length K is constant, using radix sort. 
    >>> suffix_arr_radixsort('abaab')
    [2, 3, 0, 4, 1]
    """
    suffs = suffixes(S, term)
    # k = len(max(suffs, key = lambda s: len(s))) #maximum suffix length.
    k = len(S) 
    #Pad all suffixes w/ term to get them to this length. 
    padded_suffs = pad_suffixes(suffs, k)
    bucket_keys = sorted(list(set(S)))
    if term:
        bucket_keys = list(set(S + '$'))
    bucket_set = {k: [] for k in bucket_keys}
    for i in range(k): 
        for B in bucket_set:
            if bucket_set[B]: #Not empty.
                sub_bucket_set = bucketSet(bucket_set[B], i)
    #I'll implement this bullshit later
    return bucket_set
    # return radixCollect(buckets)
    

def bucketSet(S, i=0):
    """Given a list of strings S, create a bucket set for S, with
    one bucket per unique I-TH CHARACTER of the strings.
    Populate this bucket set dictionary with elements in S and return it. 
    >>> bucketSet(['352','100','12$', '35$', '344'])
    {'1': ['100', '12$'], '3': ['352', '35$', '344']}
    >>> bucketSet(['100','12$'], i=1)
    {'0': ['100'], '2': ['12$']}
    """
    if not S:
        return None
    if None in S:
        return None
    assert i < len(S[0]), 'index to consider MUST be in range of strings.'
    assert all([len(s) == len(S[0]) for s in S]), 'All strings must be same length.'
    if not S:
        return None
    keys = sorted(list(set([s[i] for s in S])))
    bucket_set = {k: [] for k in keys}
    for s in S:
        bucket_set[s[i]].append(s)
    # ordered_bs = OrderedDict(sorted(bucket_set.items()))
    return bucket_set

def OneVal(d):
    """Return true if ALL dict keys have ONE associated value."""
    return all([len(v) == 1 for v in d.values()])

def radixCollect(d):
    """Traverse dictionary tree and collect suffixes."""
    pass

def pad_suffixes(suffixes, k):
    """Pad suffixes in SUFFIXES to get them all to length k, and return them.
    >>> pad_suffixes(['352', '100', '12', '35', '344'], 3)
    ['352', '100', '12$', '35$', '344']
    """
    padded = []
    for s in suffixes:
        if len(s) < k:
            m = k - len(s) # number of missing chars to get to k.
            s += '$' * m
        padded.append(s)
    return padded


test_func(suffix_arr_radixsort)

