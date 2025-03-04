### Präsentation
[FabLab - Handlötkurs 02-2025.pdf](https://github.com/user-attachments/files/19078771/FabLab.-.Handlotkurs.02-2025.pdf)

### BOM
Currently unavailable

### Programming Pi Pico
## 1. Update MicroPython Firmware
1. Update firmware of the raspberry py pico by downloading the ".uf2" file from [micropython.org](https://micropython.org/download/RPI_PICO/)
2. Hold boot button and connect the raspi to the PC.
3. Drag and drop the .uf2 file to the raspi's drive.
   ... it will disconnect automatically => i.e. ready to get programmed.

## 2. Python Script
Be aware that the thonny app may not work perfectly. You may always need to "re"-open the code befor download it. 
1. Download the thonny app: https://thonny.org/.
2. Go to "Tools/Options...", enter "Interpreter" and select the interpreter for the raspberry pi pico and click "OK".
3. (Re-)Connect the raspberry (without pressing the boot button).
4. Click on the "Stop" button.
5. Load the script you want to download to the raspi.
6. Go to "Save as", where it asks for either save on PC or on Raspberry (if not asked, the raspberry is not connected correctly (its firmware may not be up-to-date)).
7. Select "Raspberry Pi".
8. Save it as "main.py" (it must be named as "main" else it wont auto-start after reboot)
9. Happy running :-)
