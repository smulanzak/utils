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
    subprocess.run([PREFIX, "install", "-y", "python3-pip", "curl", "git", "wget", "build-essential", "lldb", "htop"], check=True)

def install_brave_browser() -> None:
    subprocess.run("curl -fsS https://dl.brave.com/install.sh | sh", shell=True, check=True)

def print_install_visual_studio_code() -> None:
    message = """
    Install Visual Studio Code (Debian/Ubuntu):
      1. Download and run the .deb file from "https://code.visualstudio.com/Download".
      2. Run "sudo apt install ./code_*.deb"."""
    print(message)

def print_install_rust() -> None:
    message = """
    Install Rust:
      1. Run: "curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh".
      2. Run: "rustup component add rust-analyzer"."""
    print(message)

def print_install_go() -> None:
    message = """
    Install Go:
      1. Download the .tar.gz file from "https://go.dev/dl/".
      2. Run "sudo tar -C /usr/local -xzf <.tar.gz file>".

    Add Go to PATH (https://go.dev/doc/install):
      1. Open .bashrc by running "nano ~/.bashrc".
      2. Add the line "export PATH=$PATH:/usr/local/go/bin" at the bottom of .bashrc.
      3. Update the terminal by running "source ~/.bashrc".
      4. Confirm installation by running "go version".

    Install Delve:
      1. Run "go install github.com/go-delve/delve/cmd/dlv@latest"."""
    print(message)

def main() -> None:
    check_sudo()
    run_update()
    run_upgrade()
    install_misc()
    install_brave_browser()
    print_install_visual_studio_code()
    print_install_rust()
    print_install_go()

if __name__ == "__main__":
    main()
