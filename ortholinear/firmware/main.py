import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import ShiftRegisterKeys
from kmk.keys import KC
from kmk.modules.layers import Layers

# Pinout
PIN_DAT = board.D9
PIN_CLK = board.D8
PIN_LD = board.D7
NUM_KEYS = 59


class HepOrtholinear(KMKKeyboard):
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
            0, 4,  8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 53,
               5,  9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 54,
               6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50,
               7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55,
                   1,  2,          3, 56,     57, 58,
        ]

        # =============================================================
        # Keymap
        self.modules.append(Layers())

        MOD = KC.MO(1)
        NUMPAD = KC.TG(2)

        _______ = KC.TRNS

        self.keymap = [
            # Base layer
            [
                KC.ESC,  KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC,
                         KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC,
                         KC.LCTL, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.ENT,
                         KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.NO,
                                  KC.LGUI, KC.LALT,                   MOD,     KC.SPC,           KC.RALT, KC.RCTL,
            ],
            # Mod layer
            [
                _______, _______, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.DEL,
                         _______, _______, _______, _______, _______, _______, KC.PGUP, KC.HOME, KC.UP,   KC.END,  _______, _______, _______,
                         KC.CLCK, _______, _______, _______, NUMPAD,  _______, KC.PGDN, KC.LEFT, KC.DOWN, KC.RGHT, _______, KC.QUOT,
                         _______, _______, _______, _______, _______, _______, KC.INS,  KC.APP,  _______, _______, KC.BSLS, _______, _______,
                                  _______, _______,                   _______, _______,          _______, _______,
            ],
            # Numpad layer
            [
                _______, _______, _______, _______, _______, _______, _______, _______, KC.N7,   KC.N8,   KC.N9,   KC.PSLS, _______, _______, _______,
                         _______, _______, _______, _______, _______, _______, _______, KC.N4,   KC.N5,   KC.N6,   KC.PAST, _______, _______,
                         _______, _______, _______, _______, _______, _______, _______, KC.N1,   KC.N2,   KC.N3,   _______, _______, 
                         _______, _______, _______, _______, _______, _______, _______, KC.N0,   _______, _______, _______, _______, _______,
                                  _______, _______,                   _______, _______,          _______, _______,
            ],
        ]


if __name__ == '__main__':
    keyboard = HepOrtholinear()
    keyboard.go()
