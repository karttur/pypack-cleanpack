'''
Created on 10 sep. 2019

@author: thomasgumbricht
'''
import os, sys
import hashlib
import path


def Hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()   

def MatchingFolders(masterpath, slavepath, checkHidden=False, removeDSstore = False):
    if masterpath == slavepath:
        sys.exit('EXITING masterpath == slavepath')
    if not os.path.isdir(masterpath):
        sys.exit('EXITING asterpath does not exist')
    if not os.path.isdir(slavepath):
        sys.exit('EXITING slavepath does not exist')
    for root, dirs, nofiles in os.walk(masterpath, topdown=True):
        if not checkHidden:
            dirs[:] = [d for d in dirs if not d[0] == '.']
        for subdir in dirs:
            mastersubpath = os.path.join(root,subdir)
            slavesubroot = root.replace(masterpath, slavepath)
            slavesubpath = os.path.join(slavesubroot,subdir)
            if os.path.isdir(slavesubpath):
                #if removeDSstore, just remove it directly
                if removeDSstore:
                    dsStore = os.path.join(slavesubpath,'.DS_Store')
                    print (dsStore)
                    if os.path.isfile(dsStore):
                        
                        os.remove(dsStore)
                for file in os.listdir(mastersubpath):
                    if file[0] == '.':
                        continue
                    masterFile = os.path.join(mastersubpath,file)
                    if os.path.isfile(masterFile):

                        slaveFile = os.path.join(slavesubpath,file)
                        if os.path.isfile(slaveFile):
                            #print ('Duplicate file',slavesubpath,file)
                            #print ('duplicate name',root,name)
                            master_hash = Hashfile(masterFile)
                            slave_hash = Hashfile(slaveFile)
                            if master_hash == slave_hash:
                                print('Duplicates found:')
                                print ('    ',masterFile)
                                print ('    ',slaveFile)
                                if deleteDuplicate :
                                    os.remove(slaveFile)
                            else:
                                print('Content differs:')
                                print ('    ',masterFile)
                                print ('    ',slaveFile)
                            print ('')

def RemoveEmptyFolders(path, removeRoot=False, removeHidden=False, removeDSstore=True):
    'Function to remove empty folders'
    if not os.path.isdir(path):
        return

    # remove empty subfolders
    files = os.listdir(path)
    if len(files):
        for f in files:
            fullpath = os.path.join(path, f)
            if os.path.isdir(fullpath):
                RemoveEmptyFolders(fullpath)
    
    # if folder empty, delete it
    files = os.listdir(path)
    #print ('path',path,files)
    if len(files) == 0:
        print ("Removing empty folder:", path)
        os.rmdir(path)
    elif len(files) == 1 and files[0] == '.DS_Store':
        os.remove(os.path.join(path,'.DS_Store'))
        os.rmdir(path)

                
if __name__ == "__main__":

    removeDSstore = True
    removeRoot = True
    removeHidden = False
    masterFolder = '/Volumes/karttur/GitHub/mbpro-shared/GitHub'
    slaveFolder = slaveRoot = '/Volumes/karttur/GitHub/mbpro-shared/GitHubx'
    checkHidden = False     
    deleteDuplicate = True  
    deleteHiddenDuplicate = False 


    MatchingFolders(masterFolder, slaveFolder, checkHidden, removeDSstore)
    
    RemoveEmptyFolders(slaveRoot, removeRoot, removeHidden)
    
    