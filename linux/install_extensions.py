import subprocess
import os
import sys

PREFIX = "apt-get"

def check_sudo() -> None:
    if os.geteuid() != 0:
        print("Please run this script with sudo.")
        sys.exit(1)

def run_update() -> None:
    subprocess.run([PREFIX, "update"], check=True)

def run_upgrade() -> None:
    subprocess.run([PREFIX, "upgrade", "-y"], check=True)

def install_misc() -> None:
    subprocess.run([PREFIX, "install", "-y", "python3-pip", "curl", "git", "wget", "build-essential", "lldb"], check=True)

def install_rust() -> None:
    subprocess.run("curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh -s -- -y", shell=True, check=True)
    subprocess.run(["bash", "-lc", "rustup component add rust-analyzer"], check=True)

def install_brave_browser() -> None:
    subprocess.run("curl -fsS https://dl.brave.com/install.sh | sh", shell=True, check=True)

def print_reminders() -> None:
    print("Remember to manually install Visual Studio Code (https://code.visualstudio.com/Download).")
    print("Remember to manually install Go (https://go.dev/dl/).")

def main() -> None:
    check_sudo()
    run_update()
    run_upgrade()
    install_misc()
    install_brave_browser()
    install_rust()
    print_reminders()

if __name__ == "__main__":
    main()
