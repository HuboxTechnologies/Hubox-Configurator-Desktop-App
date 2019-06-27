# Get Wi-Fi SSID and password from user
ssid = input("Wi-Fi SSID: ")
password = input("Wi-Fi Password: ")

# Read settings.ini file and fetch every line in lines list
with open("settings.ini", "r") as f:
    lines = f.readlines()

# Write settings.ini with Wi-Fi SSID and password
with open("settings.ini", "w") as f:
    for line in lines:
        if line.startswith("wifi_network = "):
            f.write(f"wifi_network = {ssid}\n")
        elif line.startswith("wifi_password = "):
            f.write(f"wifi_password = {password}\n")
        else:
            f.write(line)