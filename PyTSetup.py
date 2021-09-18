#!/usr/bin/python3
import os
import time
import sys
import pyfiglet
def slowprintmh(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 100)
os.system("clear")
def mhFig(s):
	return slowprintmh(f'\033[95m{pyfiglet.figlet_format(s)}\n\t[v2.0] By MohmadHabib\n  https:\\\github.com\mohmadhabib')
mhFig("PyT.Setup")

basicpackages = ['python','python2','clang','git','curl','wget','figlet','java','perl','nano','bash','openssl','openssh','w3m','libxml2','libxslt','fftw','freetype','pkg-config','libzmq','libpng','libcrypt']
pypacks = ['cython','requests', 'bs4', 'requests-html','pandas']
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

print (''' \033[95m
+--------------------------------------+
| This Tool Installs all Basic Packages |
+--------------------------------------+''')

slowprint(" - ".join(basicpackages))
slowprint('''\033[96m
This Command for access Storage in Termux
[00] termux-setup-storage''')
print ("                                            ")
choice = input("\033[93mDo You Want to Install All Packages [y/n] : ")
if choice in ['n','N'] : sys.exit()
if choice in ['y','Y']:
	os.system ("apt update")
	os.system("clear")
	os.system ("apt upgrade -y")
	os.system("clear")
	mhFig("PyT.Setup")
	[os.system(f"apt install {pack} -y; clear") for pack in basicpackages]
	os.system("pip --upgrade install pip")
	os.system("clear")
	mhFig("PyT.Setup")
print ("Allow the Button For Access the Storage in Termux")
time.sleep(2)
os.system ("termux-setup-storage")
time.sleep(2)
os.system("clear")
mhFig("PyT.Setup")
print("Here We Ask you if you need to install Python Packages")
print("The Packages are:")
slowprint(" - ".join(pypacks))
print("\n")
pipchoice = input("\033[93mDo you want To install The Most Used Python Packages [y/n]")
if pipchoice.lower() == 'n' : sys.exit()
if pipchoice.lower() == 'y' :
	os.system('LDFLAGS="-lm -lcompiler_rt" pip install jupyter')
	os.system("clear")
	os.system('CFLAGS="-O0" pip install lxml')
	os.system("clear")
	[os.system(f"pip install {pack}; clear") for pack in pypacks]
	os.system("clear")
	mhFig("PyT.Setup")
def slowprintf(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
print("\033[95m+-------------------------------------------------+")
slowprintf('''\033[95m|               Done By MohmadHabib              |
|           Visit My Github @mohmadhabib         |
|              For More Useful Tools!            |''')
print("+-------------------------------------------------+")

input("\n\nPress  enter to exit : ")