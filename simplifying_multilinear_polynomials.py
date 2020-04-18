# When we attended middle school were asked to simplify mathematical expressions like 
# "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy ("2x+xy"). But tell that 
# to your pc and we'll see!

# Write a function: simplify, that takes a string in input, representing a multilinear 
# non-constant polynomial in integers coefficients (like "3x-zx+2xy-x"), and returns 
# another string as output where the same expression has been simplified in the 
# following way ( -> means application of simplify):

# -All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, 
# e.g.:
# "cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"


# -All monomials appears in order of increasing number of variables, e.g.:
# "-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

# -If two monomials have the same number of variables, they appears in lexicographic 
# order, e.g.:
# "a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

# -There is no leading + sign if the first coefficient is positive, e.g.:
# "-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

# N.B. to keep it simplest, the string in input is restricted to represent only 
# multilinear non-constant polynomials, so you won't find something like `-3+yx^2'. 
# Multilinear means in this context: of degree 1 on each variable.

# Warning: the string in input can contain arbitrary variables represented by lowercase 
# characters in the english alphabet.

string1 = "-a+5ab+3a-c-2a"
string2 = "a+ca-ab"

import re

def simplify(poly):
    nums = '1234567890'
    sorter = {'pos': [], 'neg': []}
    monos = re.split(r'[+-]', poly)
    for each in monos:
        if poly[poly.find(each) - 1] == '+':
            sorter['pos'].append(each)
        elif poly[poly.find(each) - 1] == '-':
            sorter['neg'].append(each)
        else:
            sorter['pos'].append(each)
    sums_dict = {}
    for k, v in sorter.items():
        for each_mono in v:
            if each_mono == '':
                v.remove(each_mono)
            elif each_mono[0] not in nums:
                v[v.index(each_mono)] = '1' + each_mono
        for i in range(len(v)):
            v[i] = (int(v[i][0]), v[i][1:])
        for each_tup in v:
            if each_tup[1] not in sums_dict.keys():
               sums_dict[each_tup[1]] = 0
            for each_var, each_sum in sums_dict.items():
                if each_tup[1] == each_var and k == 'pos':
                    each_sum += int(each_tup[0])
                    
                
    print(sums_dict)

simplify(string1)  