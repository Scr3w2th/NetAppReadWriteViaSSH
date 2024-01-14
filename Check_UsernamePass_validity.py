import paramiko
import os.path
import time
import sys
import re

# Check Username and Password file validity
# Prompt user for file
user_file = input("\n# Enter user file path and name (e.g. D:\MyApps\myfile.txt): ")

# Verify the validity of the Username and Password file
if os.path.isfile(user_file) == True:
    print("\n* Username and Password file is valid :)\n")
    
else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(user_file))
    sys.exit()
    
# Checking commands file.
# Prompt user for input
cmd_file = input("\n Enter commands file path and name (e.g. D:\MyApps\myfile.txt): ")

# Verify validity of COMMANDS FILE
if os.path.isfile(cmd_file) == True:
    print("\n* Command file is valid :)\n")
    
else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(cmd_file))
    sys.exit()
    
