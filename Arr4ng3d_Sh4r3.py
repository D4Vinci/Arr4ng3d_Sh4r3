import os,datetime,time

if os.name!="nt":
    print " [#] Sorry We Only Support Windows Right Now! [#]"
    print " \t\t\t[!] Stay Tuned :D [!]"
    exit(0)

def timed(SSID):
    string=raw_input("\n\t[!] String to add to password [Default:PythonControlled] : ")
    if string=="":
        string="PythonControlled"
    if len(string)<8:
        print " String must be longer than 8 chars"
        timed(SSID)
    timepass=time.ctime().split(" ")[3].split(":")[0]
    print "\n Now the password will be changed every hour [Now Be : {} ]".format(string+str(timepass))

    os.popen("netsh wlan set hostednetwork mode=allow ssid={} key={}".format(SSID,string+str(timepass)))
    os.popen("netsh wlan start hostednetwork")

    print "\n\t  [#] Hotspot Started [#]"
    print "\t[ Leave this script opened ]"
    while 1:
        try:
            print "."
            time.sleep(10)
            if time.ctime().split(" ")[3].split(":")[0]>timepass:
                timepass=time.ctime().split(" ")[3].split(":")[0]
                pwd=string+str(timepass)
                os.popen("netsh wlan set hostednetwork mode=allow ssid={} key={}".format(SSID,pwd))
                print "\t Password Changed"
        except:
            os.system("netsh wlan stop hostednetwork")
            exit(0)

def dated(SSID):
    string=raw_input("\n\t[!] String to add to password [Default:PythonControlled] : ")
    if string=="":
        string="PythonControlled"
    if len(string)<8:
        print " String must be longer than 8 chars"
        timed(SSID)
    timepass=datetime.datetime.now().strftime ("%d")
    print "\n Now the password will be changed every day [Now Be : {} ]".format(string+str(timepass))

    os.popen("netsh wlan set hostednetwork mode=allow ssid={} key={}".format(SSID,string+str(timepass)))
    os.popen("netsh wlan start hostednetwork")

    print "\n\t  [#] Hotspot Started [#]"
    print "\t[ Leave this script opened ]"
    while 1:
        try:
            print "."
            time.sleep(10)
            if datetime.datetime.now().strftime ("%d")>timepass:
                timepass=datetime.datetime.now().strftime ("%d")
                pwd=string+str(timepass)
                os.popen("netsh wlan set hostednetwork mode=allow ssid={} key={}".format(SSID,pwd))
                print "\t Password Changed"
        except:
            os.system("netsh wlan stop hostednetwork")
            exit(0)

def main():
    os.system("cls")
    print "\n\tWelcome to Arr4ng3d_Sh4r3 Python Script"
    print "\t   Share Wifi With Timed Password"
    print "\n Note : This script should be executed as admin to work\n"
    wifi_name=raw_input("Wifi Name :")
    print "\n\t\tChoose You Password Plan :"
    print "\t\t  1)Change password every hour for [Current Hour]"
    print "\t\t  2)Change password every day for [Current day date]"
    choice=input("\t[!] Choice : ")
    if choice==1:
        timed(wifi_name)
    elif choice==2:
        dated(wifi_name)
    else:
        print "[!]Please Enter a valid choice"
        main()

if __name__ == '__main__':
    main()
