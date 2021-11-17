import locale
import ctypes
import subprocess

windll = ctypes.windll.kernel32
windll.GetUserDefaultUILanguage()
lang = locale.windows_locale[windll.GetUserDefaultUILanguage()]

data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("ibm850").split("\n")

if lang == "fr_FR":
    print("OS lang : fr_FR\n")
    wifis = [i.split(":")[1].strip('\r').strip() for i in data if "Profil Tous les utilisateurs" in i]
    for wifi in wifis:
        data = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi, "key=clear"]).decode("ibm850").split("\n")
        pw = [i.split(":")[1].strip('\r').strip() for i in data if "Contenu" in i]
        pw = pw[0] if pw else None
        print(("{:>20} : {}".format(wifi, pw)))
elif lang == "en_US":
    print("OS lang : en_US\n")
    wifis = [i.split(":")[1].strip('\r').strip() for i in data if "All User Profile" in i]
    for wifi in wifis:
        data = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi, "key=clear"]).decode("ibm850").split("\n")
        pw = [i.split(":")[1].strip('\r').strip() for i in data if "Key Content" in i]
        pw = pw[0] if pw else None
        print(("{:>20} : {}".format(wifi, pw)))
else:
    print("Unknown OS")