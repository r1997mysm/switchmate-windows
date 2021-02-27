import asyncio
import platform

from bleak import BleakClient, BleakScanner



address = "F2:CD:ED:18:5F:93"

SwitchService_UUID = "a22b0090-ebdd-49ac-b2e7-40eb55f5d0ab"
SwitchService_hndl = 45

OFF = b'\x00'
ON  = b'\x01'


import platform
import asyncio
import logging

from bleak import BleakClient


async def run(address, debug=False):

    async with BleakClient(address) as client:
        x = await client.is_connected()

        if bytes(await client.read_gatt_char(SwitchService_UUID)) == OFF:
            await client.write_gatt_char(SwitchService_UUID, ON)
            print("ON")
        else:
            await client.write_gatt_char(SwitchService_UUID, OFF)
            print("OFF")


global loop
loop = asyncio.get_event_loop()

def SWITCH():
    global loop

    
    while 1:
        try:
            loop.run_until_complete(run(address))
            break
        except:
            pass
    return



import keyboard as kb


kb.add_hotkey("ctrl+`", SWITCH, args= () )
kb.wait("ctrl+esc")
