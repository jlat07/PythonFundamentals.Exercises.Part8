import os



def tree_branch(dirName):

    dirName = str(input('Input directory:'))
    
    lst_files = os.listdir(dirName)

    all_files = list()
   
    for entry in lst_files:

        try:
        
            fullPath = os.path.join(dirName, entry)

            if os.path.isdir(fullPath):

                all_files = all_files + getlst_files(fullPath)
        
            else:

                all_files.append(fullPath)

        except (OSError, TypeError, NameError):
                
            print(all_files)
 