import array
import rp2
from machine import Pin
from time import sleep_ms, ticks_ms, ticks_diff
import uasyncio as asyncio
import math

# Configuration parameters
NUM_LEDS = 3  # Number of WS2812 LEDs
WS2812_PIN_NUM = 8  # Pin connected to the WS2812 (GPIO8)
NUM_DEBUG_LEDS = 6  # Number of debug LEDs
DEBUG_PIN_NUMS = [0, 1, 2, 3, 4, 5]  # GPIO pins connected to the debug LEDs
BRIGHTNESS_PERIOD_MS = 10 * 1000  # Duration for a full brightness cycle in milliseconds

# Define the PIO program to control the WS2812 LEDs
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label('bitloop')
    out(x, 1).side(0)  [T3 - 1]
    jmp(not_x, 'do_zero').side(1)  [T1 - 1]
    jmp('bitloop').side(1)  [T2 - 1]
    label('do_zero')
    nop().side(0)  [T2 - 1]
    wrap()

# Create the StateMachine with the ws2812 program, outputting on GPIO8 (pin 11)
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(WS2812_PIN_NUM))

# Start the StateMachine
sm.active(1)

# Set up the debug LEDs
debug_leds = [Pin(pin_num, Pin.OUT) for pin_num in DEBUG_PIN_NUMS]

# Function to update the WS2812 LED strip
def ws2812_write(led_data):
    # Create an array of LED values
    ar = array.array("I", led_data)
    # Write the data to the StateMachine
    sm.put(ar, 8)
    sleep_ms(1)  # Pause for a short while to ensure the data is latched

# Function to convert RGB to GRB
def rgb_to_grb(r, g, b):
    return (g << 16) | (r << 8) | b

# Function to generate color from hue
def hsv_to_rgb(hue, saturation, value):
    # Convert HSV to RGB with dimming factor
    if saturation == 0.0:
        return (value, value, value)
    i = int(hue * 6.0)  # Sector 0 to 5
    f = (hue * 6.0) - i
    p = value * (1.0 - saturation)
    q = value * (1.0 - (saturation * f))
    t = value * (1.0 - (saturation * (1.0 - f)))
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

# Asynchronous function to create a comet effect
async def comet_effect():
    tail_length = 3  # Number of LEDs in the tail
    delay = 100      # Delay between LED changes in milliseconds
    while True:
        for i in range(NUM_DEBUG_LEDS):
            # Turn off all LEDs
            for led in debug_leds:
                led.off()

            # Light up the comet tail
            for j in range(tail_length):
                index = (i - j + NUM_DEBUG_LEDS) % NUM_DEBUG_LEDS
                debug_leds[index].on()

            # Pause for a short while
            await asyncio.sleep_ms(delay)

# Asynchronous function to create a smooth color transition effect with unique starting colors and oscillating brightness
async def smooth_color_transition_with_oscillating_brightness():
    start_hues = [0.0, 0.33, 0.67]  # Different starting points in hue spectrum
    delay = 50  # Adjust the speed of color transition in milliseconds
    start_time = ticks_ms()  # Get the current time in milliseconds

    while True:
        current_time = ticks_ms()  # Get the current time in milliseconds
        elapsed_time = ticks_diff(current_time, start_time)  # Calculate elapsed time
        brightness = (math.sin(2 * math.pi * (elapsed_time / BRIGHTNESS_PERIOD_MS)) + 1) / 2  # Oscillate between 0 and 1

        # Calculate current hue for each LED
        led_colors = []
        for i, start_hue in enumerate(start_hues):
            hue = (start_hue + (elapsed_time / 255.0) % 1.0)
            r, g, b = hsv_to_rgb(hue, 1.0, brightness)  # Apply oscillating brightness
            grb_color = rgb_to_grb(int(r * 255), int(g * 255), int(b * 255))
            led_colors.append(grb_color)

        # Update the WS2812 LEDs with the new colors
        ws2812_write(led_colors)
        # Pause for a short while
        await asyncio.sleep_ms(delay)

# Main asynchronous function to run both effects
async def main():
    # Run both effects concurrently
    await asyncio.gather(
        comet_effect(),
        smooth_color_transition_with_oscillating_brightness()
    )

# Run the main function
asyncio.run(main())
