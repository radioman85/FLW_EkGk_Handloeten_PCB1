import array
import rp2
from machine import Pin
from time import sleep_ms, ticks_ms, ticks_diff
import uasyncio as asyncio
import math


# ============================================================
# Configuration parameters
# ============================================================

NUM_LEDS = 3                    # Number of WS2812 LEDs
WS2812_PIN_NUM = 8              # GPIO pin connected to WS2812

NUM_DEBUG_LEDS = 6              # Number of debug LEDs
DEBUG_PIN_NUMS = [0, 1, 2, 3, 4, 5]

BRIGHTNESS_PERIOD_MS = 10 * 1000  # Full brightness cycle: 10 seconds


# ============================================================
# WS2812 PIO program
# ============================================================

@rp2.asm_pio(
    sideset_init=rp2.PIO.OUT_LOW,
    out_shiftdir=rp2.PIO.SHIFT_LEFT,
    autopull=True,
    pull_thresh=24
)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3

    wrap_target()

    label('bitloop')

    out(x, 1).side(0) [T3 - 1]
    jmp(not_x, 'do_zero').side(1) [T1 - 1]
    jmp('bitloop').side(1) [T2 - 1]

    label('do_zero')
    nop().side(0) [T2 - 1]

    wrap()


# ============================================================
# Create WS2812 StateMachine
# ============================================================

sm = rp2.StateMachine(
    0,
    ws2812,
    freq=8_000_000,
    sideset_base=Pin(WS2812_PIN_NUM)
)

sm.active(1)


# ============================================================
# Debug LEDs
# ============================================================

debug_leds = [
    Pin(pin_num, Pin.OUT)
    for pin_num in DEBUG_PIN_NUMS
]


# ============================================================
# Pico onboard LED
# ============================================================

# "LED" automatically refers to the onboard LED on the Pico.
# This works on the standard Raspberry Pi Pico/Pico W
# MicroPython builds that expose the onboard LED this way.

pico_led = Pin("LED", Pin.OUT)


# ============================================================
# WS2812 functions
# ============================================================

def ws2812_write(led_data):
    """
    Send color data to the WS2812 LEDs.
    """

    ar = array.array("I", led_data)

    sm.put(ar, 8)

    # Short delay to ensure the data is latched
    sleep_ms(1)


def rgb_to_grb(r, g, b):
    """
    Convert RGB values to the GRB format required by WS2812.
    """

    return (g << 16) | (r << 8) | b


# ============================================================
# HSV to RGB conversion
# ============================================================

def hsv_to_rgb(hue, saturation, value):
    """
    Convert HSV values to RGB.

    hue:
        0.0 - 1.0

    saturation:
        0.0 - 1.0

    value:
        0.0 - 1.0
    """

    if saturation == 0.0:
        return (value, value, value)

    i = int(hue * 6.0)

    f = (hue * 6.0) - i

    p = value * (1.0 - saturation)

    q = value * (1.0 - (saturation * f))

    t = value * (
        1.0 - (saturation * (1.0 - f))
    )

    i = i % 6

    if i == 0:
        return (value, t, p)

    if i == 1:
        return (q, value, p)

    if i == 2:
        return (p, value, t)

    if i == 3:
        return (p, q, value)

    if i == 4:
        return (t, p, value)

    if i == 5:
        return (value, p, q)


# ============================================================
# Comet effect for GPIO 0-5
# ============================================================

async def comet_effect():

    tail_length = 3

    delay = 100  # milliseconds

    while True:

        for i in range(NUM_DEBUG_LEDS):

            # Turn off all debug LEDs
            for led in debug_leds:
                led.off()

            # Light up the comet tail
            for j in range(tail_length):

                index = (
                    i - j + NUM_DEBUG_LEDS
                ) % NUM_DEBUG_LEDS

                debug_leds[index].on()

            # Wait before moving the comet
            await asyncio.sleep_ms(delay)


# ============================================================
# WS2812 smooth color transition
# ============================================================

async def smooth_color_transition_with_oscillating_brightness():

    # Different starting hue for each WS2812
    start_hues = [
        0.0,
        0.33,
        0.67
    ]

    # Update interval
    delay = 50

    # Record starting time
    start_time = ticks_ms()

    while True:

        current_time = ticks_ms()

        elapsed_time = ticks_diff(
            current_time,
            start_time
        )

        # ----------------------------------------------------
        # Oscillating brightness
        #
        # Goes smoothly:
        # 0 -> 1 -> 0
        #
        # over BRIGHTNESS_PERIOD_MS
        # ----------------------------------------------------

        brightness = (
            math.sin(
                2 * math.pi *
                (
                    elapsed_time /
                    BRIGHTNESS_PERIOD_MS
                )
            ) + 1
        ) / 2

        # List containing colors for all WS2812 LEDs
        led_colors = []

        for i, start_hue in enumerate(start_hues):

            # Continuously rotate through the hue spectrum
            hue = (
                start_hue +
                (elapsed_time / 255.0)
            ) % 1.0

            # Convert HSV to RGB
            r, g, b = hsv_to_rgb(
                hue,
                1.0,
                brightness
            )

            # Convert 0.0-1.0 RGB to 0-255
            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)

            # Convert RGB to WS2812 GRB format
            grb_color = rgb_to_grb(
                r,
                g,
                b
            )

            led_colors.append(grb_color)

        # Send colors to WS2812 LEDs
        ws2812_write(led_colors)

        # Wait before next update
        await asyncio.sleep_ms(delay)


# ============================================================
# Pico onboard LED blink
# ============================================================

async def blink_pico_led():

    while True:

        # Turn onboard LED ON
        pico_led.on()

        # Keep it on for 500 ms
        await asyncio.sleep_ms(500)

        # Turn onboard LED OFF
        pico_led.off()

        # Keep it off for 500 ms
        await asyncio.sleep_ms(500)


# ============================================================
# Main asynchronous function
# ============================================================

async def main():

    # Run all three effects concurrently
    await asyncio.gather(

        # GPIO 0-5 comet effect
        comet_effect(),

        # WS2812 color/brightness effect
        smooth_color_transition_with_oscillating_brightness(),

        # Pico onboard LED blinking
        blink_pico_led()
    )


# ============================================================
# Start everything
# ============================================================

asyncio.run(main())