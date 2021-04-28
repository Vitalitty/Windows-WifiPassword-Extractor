import subprocess

data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("ibm850").split("\n")

wifis = [i.split(":")[1].strip('\r').strip() for i in data if "Profil Tous les utilisateurs" in i]

if wifis:
    for wifi in wifis:
        data = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi, "key=clear"]).decode("ibm850").split("\n")
        pw = [i.split(":")[1].strip('\r').strip() for i in data if "Contenu de la clé" in i]
        pw = pw[0] if pw else None
        print(("{:>20} : {}".format(wifi, pw)))
else:
    wifis = [i.split(":")[1].strip('\r').strip() for i in data if "All User Profile" in i]
    for wifi in wifis:
        data = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi, "key=clear"]).decode("ibm850").split("\n")
        pw = [i.split(":")[1].strip('\r').strip() for i in data if "Key Content" in i]
        pw = pw[0] if pw else None
        print(("{:>20} : {}".format(wifi, pw)))