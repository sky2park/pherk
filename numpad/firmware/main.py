import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import ShiftRegisterKeys
from kmk.keys import KC

# Pinout
PIN_DAT = board.D9
PIN_CLK = board.D8
PIN_LD = board.D7
NUM_KEYS = 17


class HepNumPad(KMKKeyboard):
    def __init__(self):
        # =============================================================
        # Scanner: 74HC165 scan chain
        self.matrix = ShiftRegisterKeys(
            clock=PIN_CLK,
            data=PIN_DAT,
            latch=PIN_LD,
            key_count=NUM_KEYS,
            value_to_latch=True,
            value_when_pressed=False,
            interval=0.02,
            max_events=64
        )

        # =============================================================
        # Layout
        self.coord_mapping = [
            0, 7, 8, 15,
            1, 6, 9, 14,
            2, 5, 10,
            3, 4, 11, 13,
            16,   12
        ]

        # =============================================================
        # Keymap
        self.keymap = [
            [
                KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS,
                KC.P7,   KC.P8,   KC.P9,   KC.PPLS,
                KC.P4,   KC.P5,   KC.P6,
                KC.P1,   KC.P2,   KC.P3,   KC.PENT,
                KC.P0,            KC.PDOT,
            ],
        ]

if __name__ == '__main__':
    keyboard = HepNumPad()
    keyboard.go()
