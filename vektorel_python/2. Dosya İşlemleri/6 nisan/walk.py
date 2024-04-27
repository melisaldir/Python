"""
import os
from os.path import join, getsize
for root,dirs, flies in os.walk("D\\"):
    print(root,"consumes", end="")
    print(sum(getsize(join(root, name))))
"""