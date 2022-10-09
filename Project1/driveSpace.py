import shutil

def formatsize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        return "error"

    if kb>= 1024:
        Mb = kb / 1024
        if Mb >= 1024:
            Gb = Mb / 1024
            if Gb >= 1024:
                Tb = Gb / 1024
                return "%.2fTb" % (Tb)
            else:
                return "%.2fGb" % (Gb)
        else:
            return "%.2fMb" % (Mb)
    else: 
        return "%.2fKb" % (kb)

x=False
while x==False:
    try:
        driveinfo = shutil.disk_usage(input("Enter Drive letter (ex. C:\\): "))
        freespace = formatsize(driveinfo[2])
        x = True
    except:
        print("That drive does not exist")
else:
    x = True
print(freespace) 
       
##Source https://www.tutorialexample.com/a-simple-guide-to-python-get-disk-or-directory-total-space-used-space-and-free-space-python-tutorial/


    