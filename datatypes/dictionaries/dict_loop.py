from dict_as_set_of_counters import histogram

def print_hist(dct):
    for key, value in sorted(dct.iteritems()):
        print(key, value) 

print(print_hist(histogram('alessandro')))



