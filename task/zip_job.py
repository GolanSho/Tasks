import os
import sys
# Create an array a,b,c,d 
arr = ["a", "b", "c", "d"]

# Based on this array create txt files (a.txt, b.txt...)
for i in arr:
    f = open(f"{i}.txt","w+")
    f.close
 
# Make sure all txt files created, if not fail the script
for f in arr: 
    if os.path.isfile(f"{f}.txt"):
        print(f"File {f}.txt Created")
    else:
        print(f"File {f}.txt Not Created, exiting")
        sys.exit(1)

# Create zip files with names based on array + VERSION env variable, so each zip file will include one txt file inside:
# a_1.2.0.zip should include a.txt,
# b_1.2.0.zip should include b.txt
for z in arr:
    try:
        os.system(f"zip {z}_$VERSION.zip {f}.txt")
        os.system(f"echo {z}_$VERSION.zip Created")
    except Exception as e:
        print(f"Couldn't Create zip file of {f}.txt, error: {e}")
        sys.exit(1)

# Make sure all zip files are created, if not fail the script
