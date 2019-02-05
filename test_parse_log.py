# -*- coding: utf-8 -*-

import re
import sys


def main():
    """ 
    parse logs, generate occurence of successive viewmodes 
    with associate levels
    input: standard input
    output: results are written to standard ouput
    """

    current_viewmode = None
    current_count = 0
    l_all_level = []
    
    # the pattern of good plan tuile
    regex = re.compile(r"(.+)/map/1.0/slab/(.+)/256/([0-9]+)(/[0-9]+){2}")
    
    # input comes from STDIN
    for line in sys.stdin:
        try:
            # remove leading and trailing whitespace
            url_tuile = line.strip()
            # check if line matches with pattern
            matchs = regex.match(url_tuile)
            
            if matchs:
                # group return matching subgroubs 
                viewmode = matchs.group(2)
                level = matchs.group(3)
                
                if current_viewmode == viewmode:
                    # occurence of successive viewmodes
                    current_count += 1
                    # manage duplicate values
                    if level not in l_all_level:
                        l_all_level.append(level) 
                else:
                    if current_viewmode:
                        # write result to STDOUT
                        print('%s\t%s\t%s' % (current_viewmode, current_count, ','.join(l_all_level)))
                    current_count = 1
                    l_all_level = [level]
                    current_viewmode = viewmode
    
        except ValueError:
            continue
        
    # do not forget to output the last wviewmode if needed!
    if current_viewmode:
        if current_viewmode == viewmode:
            print('%s\t%s\t%s' % (current_viewmode, current_count, ','.join(l_all_level)))

if __name__ == '__main__':
    main()
