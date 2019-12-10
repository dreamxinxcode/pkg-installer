import os

def main():
    pkg_file = open("pkgs.txt", "r")
    for pkg in pkg_file:
        os.system("sudo pacman -S %s" %pkg)

if(__name__ == "__main__"):
    main()
