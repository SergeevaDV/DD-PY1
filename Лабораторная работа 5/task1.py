from pprint import pprint
dict_ = [{'bin': bin(x), 'dec': x, 'hex': hex(x), 'oct': oct(x)} for x in range(16)]
pprint(dict_)