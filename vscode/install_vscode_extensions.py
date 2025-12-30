import platform
import subprocess
import time

EXTENSIONS = {
    "Go": "golang.go",
    "Python": "ms-python.python",
    "rust-analyzer": "rust-lang.rust-analyzer",
    "Even Better TOML": "tamasfe.even-better-toml",
    "Highlight Trailing White Spaces": "ybaumes.highlight-trailing-white-spaces",
    "Markdown All in One": "yzhang.markdown-all-in-one",
    "CodeLLDB": "vadimcn.vscode-lldb"
}

def run_auto_install() -> None:
    print("The following extensions will be installed from CLI.")
    for name, extension in EXTENSIONS.items():
        print(f"- {name} ({extension}).")

    # Wait for VSCode to initialize
    launch_vscode()
    initialize_vscode()

    print()
    for _, extension in EXTENSIONS.items():
        subprocess.run(f"code --install-extension {extension}", shell=True)
    print("\nDone.")

def inform_user() -> None:
    print()
    for _ in range(3):
        print("IMPORTANT: do not close VSCode until the script has completed!")
        time.sleep(1)
    print()

def launch_vscode() -> None:
    print("\nLaunching VSCode...")
    inform_user()
    subprocess.run("code . &", shell=True, check=True)

def initialize_vscode() -> None:
    print("Initializing VSCode...")
    inform_user()
    while True:
        if platform.system() == "Windows":
            out = subprocess.run('tasklist /FI "IMAGENAME eq Code.exe"', shell=True, capture_output=True, text=True)
            if "Code.exe" in out.stdout:
                break
        else:
            out = subprocess.run("pgrep -f 'code --type=extensionHost'", shell=True, capture_output=True, text=True)
            if out.stdout.strip():
                break
        time.sleep(0.5) # Prevent CPU spin
    time.sleep(5) # Give VSCode a moment to finish initializing
    print("VSCode was successfully initialized.")

def main() -> None:
    run_auto_install()

if __name__ == "__main__":
    main()