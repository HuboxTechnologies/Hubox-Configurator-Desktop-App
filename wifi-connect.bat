@echo off

Rem :====================================================
Rem : Script to write wifi credentials to a settings.ini
Rem : Command prompt
Rem :====================================================

echo ====================================================
echo               HUBOX NETWORK SETTINGS
echo ====================================================
echo.

Rem : Input to user
set /p ssid_name=Wifi SSID:
set /p password=Password:

echo.
echo Writing credentials on settings.ini file.
Rem : Writing file
echo [network] >> settings.ini
echo wifi_network=%ssid_name% >> settings.ini
echo wifi_password=%password% >> settings.ini

echo.
echo Done.

PAUSE






