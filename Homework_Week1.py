
# coding: utf-8

# In[43]:


def all_positive (n,*args):
    return bool (sum(abs(n) for n in args))
    
print (all_positive(7))


# In[46]:


def xor3 (x,y,z):
    return (x and y and z) or (x and not y and not z) or (y and not x and not z) or (z and not y and not x)
print (xor3(1,0,0))


# In[75]:


def mirror_string(str1, n):
    reverseAlphabet = "zyxwvutsrqponmlkjihgfedcba"
    str2 = ""
    for i in range(0, n):
        str2 = str2 + str1[i]
    for i in range(n, len(str1)):
        str2 = (str2 +
                  reverseAlphabet[ord(str1[i]) - ord('a')])
    return str2
str1 = "HelloWorld"
n = 0
str2 = mirror_string(str1, n - 1)
print(str2)


# In[76]:


def binary_sum(a=str,b=str):
    return int(a,2)+int(b,2)
print (binary_sum('1','10'))


# In[77]:


def only_names(lst):
    return list(filter(lambda a: a != "", lst))
print (only_names ( ['Name', '', '', '', 'Name2', '']))


# In[78]:


discriminant = lambda a, b, c : b**2 - 4*a*c
print (discriminant(1,2,1))


# In[79]:


def full_name(lst1, lst2):
    return list(map(lambda a,b: a + ' ' +b, lst1, lst2))
print (full_name (['Nairi', 'Vlad'], ['Hakobyan', 'Poghosyan']))

