import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid
import keypad

PIN_DAT = board.D9
PIN_CLK = board.D8
PIN_LD = board.D7
NUM_KEYS = 63
KEY_NUMBER_WIN = 56

k = keypad.ShiftRegisterKeys(
    clock=PIN_CLK,
    data=PIN_DAT,
    latch=PIN_LD,
    key_count=NUM_KEYS,
    value_to_latch=True,
    value_when_pressed=False,
)

event = k.events.get()
if not (event and event.key_number == KEY_NUMBER_WIN):
    storage.disable_usb_drive()
    usb_cdc.disable()
    usb_hid.enable(boot_device=1)