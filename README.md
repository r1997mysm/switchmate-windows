# Switchmate on Windows

A controller for switchmate switches for the oppressed windows user. To address the problem of low energy bluetooth on windows, we can use the `bleak` package.  

### Installation:

Just download the code, change a few parameters and there you go.

### Instructions to use:

Here are the three parameters that may need adjustments. Below, I am referring to bleak's package.

`https://github.com/hbldh/bleak/tree/develop/examples`

#### address
This is the **MAC address** of the switch. You can find this check the settings in your phone app when you connect your phone to the switch. Otherwise, it should show up when you run bleak device discovery - `discover.py` (shown in bleak's project examples). The device may not show up as Switchmate, in my case, the device is named as **PLUS Location Systems Pty Ltd**.

#### SwitchService_UUID and SwitchService_hndl 
I am aware that the service uuid and handle could be different depending on the product line. Run bleaks's example for `service_explorer.py` (change the address in bleak's example to your product's address). Look for handle around 46 to 49, I believe, there is one `[Characteristic]` which is read/write and changes its value to `\x00` or `\x01` when you turn it on/off. Copy its ID and handle to `SwitchService_UUID` and `SwitchService_hndl`.

#### Hotkey for switch functions, etc.
For my use, I added hotkeys at the last few lines. You can change it however you want.  

### Note about delays and reconnecting:

The code automatically disconnects and connects everytime we switch. It causes some delay due to reconnecting with the device. One way you can change this is to change lines `27-34` into a infinite loop. Everytime the command `async with BleakClient(address) as client:` ends, the device is disconnected. However, keeps the device connected all the time will probably make the battery run out faster 

#### Tested on Windows 10 with Switchmate toggle switch
