# importing some libs
import subprocess
import time

# running the command \clear in the terminal to clear any text before the script running
subprocess.run('clear', shell=True)
# messages dict to show the text correctly
# NOTE the \033[1;31;40m] is the color code and stype in ANSI coloring system
msg = {
    "name": ("\033[4;41;40m",
    " \033[1;31;40m __  _    ___  ____    ___   _      ____   _____",
"\033[1;31;40m |  l/ ]  /  _]|    \  /   \ | T    l    j / ___/",
"\033[1;31;40m |   /  /  [_ |  D  )Y     Y| |     |  T (   \_" ,
"\033[1;31;40m |    \ Y    _]|    / |  O  || l___  |  |  \__  T",
"\033[1;31;40m |     Y|   [_ |    \ |     ||     T |  |  /  \ |",
"\033[1;31;40m |  .  ||     T|  .  Yl     !|     | j  l  \    |",
"\033[1;31;40m l__j\_jl_____jl__j\_j \___/ l_____j|____j  \___j\033[0;40m"),

    "credits": ("\033[40m _________________________",
    "\033[1;32;40m Author: Kerolis",
    "\033[1;33;40m Project: Test",
    "\033[0;40m _________________________")
}

# printing our name and credits correctly to not be horrible looking
for name in msg["name"]:
    print(name)
for name in msg["credits"]:
    print(name)
# sleep func to make the code look cooler
time.sleep(0.5)
# text to user
print("Check my\n1 \033[1;30;40mGitHub \033[0;40mRepositry\n2 \033[1;36;40mTwitter \033[0;40mAccount\n3 \033[1;34;40mTelegram \033[0;40mAccount")
print("Type 1/2/3 or exit to close:\n")

while True:
    # getting user_input
    x = input("")
    # comparing user_input to specific Values
    if x == "1":
        print("\n(\033[1;30;40mhttps://github.com/PythonNoob999/My_Python_Traning\033[0;40m)\n")
    elif x == "2":
        print("\n(\033[1;36;40mhttps://twitter.com/Kerolis35440880\033[0;40m)\n")
    elif x == "3":
        print("\n(\033[1;34;40mhttps://t.me/kerolis55463\033[0;40m)\n")
    # exit the script  
    elif x.lower() == "exit":
        break
    else:
        print("Please Type Vaild Num")