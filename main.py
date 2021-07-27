from re import T
from typing import Sized
import pyfiglet , socket , os , wmi , time , sys , colorama , socket , subprocess
import speedtest
from colorama import Fore, Back, Style
from getmac import get_mac_address as gma
colorama.init(autoreset=True)

index = pyfiglet.figlet_format("PcTools" , font = "banner3-D")
print(Fore.RED + index + "                        Powered By codervserror" ,Fore.GREEN + """

System info(1)                  Network SpeedTest(4)
System network info(2)          Software exit(0)
Saved network information(3)    Instagram:@codervserror
""")

while True:
    
    target = input("Target number:")

    if target == "0":
        exit()
    elif target == "1":
        print("Loading system information...")
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write(Fore.GREEN + "\r" + animation[i % len(animation)])
            sys.stdout.flush()
    
        print("\n")

        computer = wmi.WMI()
        computer_info = computer.Win32_ComputerSystem()[0]
        os_info = computer.Win32_operatingSystem()[0]
        proc_info = computer.Win32_processor()[0]
        gpu_info = computer.Win32_VideoController()[0]

        os_name = os_info.Name.encode("utf-8").split(b"|")[0]
        os_version = " ".join([os_info.Version, os_info.BuildNumber])
        system_ram = float(os_info.TotalVisibleMemorySize) / 1048576 #KB to GB

        print(Fore.RED + "OS Name: {0}".format(os_name))
        print(Fore.RED + "OS Version: {0}".format(os_version))
        print(Fore.RED + "RAM: {0}".format(system_ram))
        print(Fore.RED + "Grapich Card: {0}".format(gpu_info.Name))

    elif target == "2":
        print("Loading system network information...")
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write(Fore.GREEN + "\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")

        print(Fore.RED + "İp Adress:",socket.gethostbyname(socket.gethostname()))
        print(Fore.RED + "Mac Adress:",gma())
    
    elif target == "3":

        print("Loading saved network information...")
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write(Fore.GREEN + "\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")

        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print (Fore.RED + "{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print(Fore.RED + "{:<30}|  {:<}".format(i, ""))
    
    elif target == "4":
     print("Network Speed​​Test starts:")

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
     animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

     for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write(Fore.GREEN + "\r" + animation[i % len(animation)])
        sys.stdout.flush()

     print("\n")
     speedtester = speedtest.Speedtest()
     donwloadspeed  = speedtester.download()/(1025 * 1025)
     uploadspeed = speedtester.upload()/(1025 * 1025)

     print(Fore.RED + "Download Speed",donwloadspeed,"Mbps:")
     print(Fore.RED + "Upload Speed",uploadspeed,"Mbps:")
    
    else:
        print(Fore.RED + "There is no such option, please try again !")