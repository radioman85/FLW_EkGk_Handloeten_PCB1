import os
import fileinput

def search_and_modify(file_name, search_string):
    file_path = os.path.abspath(file_name)
    modified = False

    for line in fileinput.input(file_path, inplace=True):
        # Remove trailing whitespace and check if line ends with "hide"
        stripped_line = line.strip()
        if stripped_line.endswith("hide"):
            print(line, end='')  # Line already has "hide", don't modify
        elif search_string in line:
            # If the search string is found, add " hide" to the end of the line
            print(line.rstrip() + " hide")
            modified = True
        else:
            print(line, end='')

    if modified:
        print("Changes have been made to the file.")
    else:
        print("No changes were made to the file.")

if __name__ == "__main__":
    search_string = input("Enter the string to search for: ")
    kicad_pcb_file = input("Enter the PCB file name (in the same directory as the script): ")

    search_and_modify(kicad_pcb_file, search_string)
