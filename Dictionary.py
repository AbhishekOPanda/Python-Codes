# returns the key of the element with the maximum value in a dictionary
def strongestKey(d):
    val=list(d.values())
    ky=list(d.keys())
    return ky[val.index(max(val))]
