import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import ShiftRegisterKeys
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.handlers.sequences import send_string

# Pinout
PIN_DAT = board.D9
PIN_CLK = board.D8
PIN_LD = board.D7
NUM_KEYS = 63

class PherkV2(KMKKeyboard):
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
        # Physical Layout
        self.coord_mapping = [
            0, 4,  8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52,
            1, 5,  9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53,
            2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54,
            3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55,
                  56,   57,   58,   59,   60,   61,   62,
        ]

        # =============================================================
        # Keymap
        self.modules.append(Layers())

        MOD = KC.MO(1)

        SLBRC = send_string('[')
        SRBRC = send_string(']')
        CLBRC = send_string('{')
        CRBRC = send_string('}')

        _______ = KC.TRNS

        self.keymap = [
            # Base layer
            [
                KC.HOME, KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,
                KC.END,  KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.BSPC, KC.BSLS,
                KC.ENT,  KC.LCTL, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,
                _______, KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.CLCK,
                                  KC.LGUI,     KC.LALT,      MOD,         KC.SPC,       MOD,          KC.RALT,     KC.RCTL,
            ],
            # Mod layer
            [
                KC.PGUP, KC.ESC,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,
                KC.PGDN, _______, _______, _______, CLBRC,   CRBRC,   _______, KC.PGUP, KC.HOME, KC.UP,   KC.END,  _______, KC.DEL,  _______,
                _______, _______, _______, _______, SLBRC,   SRBRC,   _______, KC.PGDN, KC.LEFT, KC.DOWN, KC.RGHT, _______, _______, _______,
                _______, _______, _______, _______, _______, _______, _______, KC.INS,  KC.APP,  _______, _______, _______, _______, _______,
                                  _______,     _______,      _______,     _______,     _______,      _______,     _______,
            ],
        ]


if __name__ == '__main__':
    keyboard = PherkV2()
    keyboard.go()
