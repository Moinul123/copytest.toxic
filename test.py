").center(columns + 10))    print(("\033[92mAmount  : \033[37m" + amount).center(columns + 10))
    print("\033[92mProcess : \033[37mStarted               ".center(columns + 10))    print("\033[92mNote    : \033[37mPress ctrl + z To Stop".center(columns + 10))
    print("\033[95m-" * (columns), end = "")    print("\n")

#Check SMS Sent and Processdef check(sent):
    amount = main.amount    delay = main.delay
        localTime = time.localtime()
    current_time = time.strftime("%I:%M:%S", localTime)
    print(f"\r\033[92m    [\033[94m {current_time} \033[92m] Message Sent : \033[94m[\033[37m{sent}\033[94m]\033[37m", end="")    
    if (sent == amount):        psb("\n\n\033[92m    [\033[37m*\033[92m] Bombing Finished!")
        psb("\033[92m    [\033[37m*\033[92m] Amount : \033[37m" + str(amount))        psb("\033[92m    [\033[37m*\033[92m] Target : \033[37m0" + main.number)
        psb("\033[92m    [\033[37m*\033[92m] From   : \033[37mToxicBomber\n")        time.sleep(0.6)
        print("\033[92m[\033[93m★\033[92m] Thanks For Using Our Tool \033[92m[\033[93m★\033[92m]".center(columns + 30))        print("\033[37m")
                return True
    else:        time.sleep(delay)
        return False
#Get Target Number
def getNumber():    number = input("\n    \033[92m[\033[37m*\033[92m] \033[37mEnter Target (\033[92mWithout +88\033[37m):> \033[37m")
    if not number.isdigit():        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Enter a Correct Number!")
        number = getNumber()    if not (len(number) == 11):
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Enter 11 Digit Number!")        number = getNumber()
        return number

#Main    def main():
    number = getNumber()    number = number[-10:]
    main.number = number    
    amount = input("    \033[92m[\033[37m*\033[92m] \033[37mEnter Amount (\033[92mDefault: 10\033[37m):> \033[37m")
    try:        amount = int(amount)
    except:        amount = 10
    
    main.amount = amount    
    delay = input("    \033[92m[\033[37m*\033[92m] \033[37mEnter Time(\033[92mSec\033[37m) Delay (\033[92mDefault: 2s\033[37m):> \033[37m")    try:
        delay = int(delay)    except:
        delay = 2    
    main.delay = delay    
    time.sleep(1)
    logo()    banner()
    sent = 0    
    items = RUNNABLE_ITEMS    finished = False
        # Running through all apis using Global Variables
    allFuncs = globals()    if check(sent):
        sys.exit()    
    while True:        for i in range(1, items+1):
            success = allFuncs"api_"+str(i)            if (success):
                sent += 1
                if(check(sent)):                    finished = True
                    break            
        if (finished):            break

# Start Ruuning Toolif (__name__ == "__main__"):
    checkPy()    from more.data import *
    logo()    update()
    main()
