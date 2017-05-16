def remove_dup(inlist):
    outlist = []
    for i in inlist:
        if i not in outlist:
            outlist.append(i)
    return outlist
            
print(remove_dup(['a', 'a', 'b', 'b', 'c', 'd', 'e']))
