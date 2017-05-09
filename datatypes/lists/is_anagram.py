#Return True is the word is anagram or False is isn't

def is_anagram(t,u):
    if sorted(t)== sorted(u):
        return True
    else:
        return False

print is_anagram('realtor', 'rotlear') # True
print is_anagram('superpuff','local') # False
print is_anagram('alla', 'lala') # True
print is_anagram('tools', 'stool') # True
print is_anagram('double', 'trouble') # False
