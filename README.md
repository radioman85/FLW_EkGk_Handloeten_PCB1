### Kurs-Dok
https://docs.google.com/document/d/1QbJ0WCrbPe96hOyB1JiNt0ZYFWMCxjqOIoHpIzepziQ/edit?usp=drive_link

### Präsentation
https://docs.google.com/presentation/d/1JOqmXC7s-w-8xuSVpEcdlVL24fG4e7r5I_c3oc2PTqE/edit?usp=drive_link

### BOM
https://docs.google.com/spreadsheets/d/1WpgOzNOipdzf3TUjmOTJRN6nh91fH2xWKgcdvkkk7AQ/edit?usp=sharing

### Raspberry Pi Pico - MicroPython Firmware
1. Update firmware of the raspberry py pico by downloading the ".uf2" file from [micropython.org](https://micropython.org/download/RPI_PICO/)
2. Hold boot button and connect the raspi to the PC.
3. Drag and drop the .uf2 file to the raspi's drive.
   ... it will disconnect automatically => i.e. ready to get programmed.

### Python Script
1. Download the thonny app: https://thonny.org/.
2. Go to "Tools/Options...", enter "Interpreter" and select the interpreter for the raspberry pi pico and click "OK".
3. (Re-)Connect the raspberry (without pressing the boot button).
4. Click on the "Stop" button.
5. Load the script you want to download to the raspi.
6. Go to "Save as", where it asks for either save on PC or on Raspberry (if not asked, the raspberry is not connected correctly (its firmware may not be up-to-date)).
7. Select "Raspberry Pi".
8. Save it as "main.py" (it must be named as "main" else it wont auto-start after reboot)
9. Happy running :-)
