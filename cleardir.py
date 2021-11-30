import os

dir = 'SVGS'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))