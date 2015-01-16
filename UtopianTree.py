"""
David Schonberger
Hackerrank.com
Warmpup - Utopian Tree
1/4/2015
"""

def calc_heights(cycles):
    if(cycles == 0):
        return [1]
    else:
        heights = [1]
        i = 1
        while(i <= cycles):
            if(i % 2 == 1):
                elt = 2*heights[len(heights) - 1]
            else:
                elt = heights[len(heights) - 1] + 1
                
            heights.append(elt)
            i += 1
        return heights

max_cycles = 60
l = calc_heights(max_cycles)

num = input()
for i in range(num):
    print l[input()]
