# this script show how to turn off internal display for mac when it is connected to an external display.
# it failed because the system disable the changing for protection. To change it require extra configuration and I decided not to mess up with it.

# external display only
sudo nvram boot-args="iog=0x0"
# then reboot

# recover internal display
sudo nvram -d boot-args
#then reboot
