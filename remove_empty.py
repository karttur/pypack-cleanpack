'''
From https://gist.github.com/jacobtomlinson/9031697
'''

import os, sys

def removeEmptyFolders(path, removeRoot=True, removeHidden=True):
    'Function to remove empty folders'
    if not os.path.isdir(path):
        return

    # remove empty subfolders
    files = os.listdir(path)
    if len(files):
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                removeEmptyFolders(fullpath)
    
    # if folder empty, delete it
    files = os.listdir(path)
    if len(files) == 0 and removeRoot:
        print ("Removing empty folder:", path)
        os.rmdir(path)
    
def usageString():
    'Return usage string to be output in error cases'
    return 'Usage: %s directory [removeRoot]' % sys.argv[0]

if __name__ == "__main__":
    removeRoot = True
    removeHidden = True
    rootFolder = '/Volumes/karttur/mbpro_20180611_tg/Documents/GitHub'
    
    if not os.path.isdir(rootFolder):
        print ("No such directory %s" % sys.argv[1])
        sys.exit(usageString())
            
    removeEmptyFolders(rootFolder, removeRoot, removeHidden)