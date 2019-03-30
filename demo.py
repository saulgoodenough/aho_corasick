
'''
An example of importing and using aho_harosick automation

'''

from aho_corasick.actrie import acTrie




patterns = ['cash', 'shew', 'ew', 'wce']

ac_automation = acTrie(patterns)

string_pool = 'cashewcewcashew'

pattern_posi, pattern_count = ac_automation.align(string_pool)
