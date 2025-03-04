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
4. In the app click on the "Stop" button.
5. Load the script you want to download to the raspi.
6. Go to "Save as", where it asks for either save on PC or on Raspberry (if not asked, the raspberry is not connected correctly (its firmware may not be up-to-date)).
7. Select "Raspberry Pi".
8. Save it as "main.py" (it must be named as "main" else it wont auto-start after reboot)
9. Happy running :-)

### Löten - Ausrüstung
 - Lötkolben (Link: [JBC CD-2BQF](https://shop.electronic-metals.ch/produkte/loettechnik/loetgeraete-ein-kanal/jbc/94951/jbc-kompakt-loetstation-cd-2bqf-wetec-edition?sPartner=10002?number=807278&gad_source=1&gclid=CjwKCAjwx-CyBhAqEiwAeOcTdfXDNTq5UXqakSejQxAiqUnyBB9TK4aIC8MYHQ78THFY60kKdBs1GRoCRy4QAvD_BwE), Handle (included): [T245](https://www.jbctools.com/t245-general-purpose-handle-product-45.html) , Spitzen (NOT included): [C245-030](https://shop.electronic-metals.ch/produkte/loettechnik/loet-entloetspitzen/jbc/c245-fuer-t245/rundform/8647/jbc-loetspitze-serie-c245-rundform?number=801290), -034, -906)
 - Lötzinn + Paste
 - 63% (Sn), 37% (Pb) (Link: [Lötdraht 0.7 mm](https://ch.farnell.com/multicore-loctite/d610scf222-250g/l-tdraht-60-40-0-7mm-250g/dp/454072), Link: [Paste - Chip Quik SMD291AX](https://ch.farnell.com/chip-quik/smd291ax/l-tpaste-no-clean-synthetisch/dp/3549310)) oder
 - 95,5% (Sn), 3,8% (Ag), 0,7% (Cu) (Link: [Lötdraht 0.7 mm](https://ch.farnell.com/multicore-loctite/d96scf222-250g/l-tdraht-105-0-7mm-250g/dp/454590), Link: [Chip Quik TS391SNL](https://ch.farnell.com/chip-quik/ts391snl/l-tpaste-no-clean-synthetisch/dp/3549323))
 - Lötflussmittel (Link: [Chip Quik SMD291](https://www.mouser.ch/ProductDetail/Chip-Quik/SMD291?qs=8BX3xQzFIvmwkympZqnNNA%3D%3D))
 - Lötmatte
 - Pinzetten (Link: [Weller Erem 7SASL, gebogen](https://ch.farnell.com/erem/7sasl/pr-zisionspinzette-gebogen-spitz/dp/2946763), Link: [Weller Erem 3SASL, gerade](https://ch.farnell.com/erem/3sasl/pinzette-120mm/dp/1014352))
 - Zahbüsrteli / Wattestäbli (Link: [M-Budget Zahnbürste](https://www.migros.ch/de/product/mo/96751))
 - Fläschli Isopropanol (Link: [Isopropanol 99,9 %](https://www.gerstaecker.ch/Isopropanol-99-9.html))
