import subprocess

EXTENSIONS = [
    "golang.go",
    "ms-python.python",
    "rust-lang.rust-analyzer",
    "tamasfe.even-better-toml",
    "vadimcn.vscode-lldb",
    "ybaumes.highlight-trailing-white-spaces",
    "yzhang.markdown-all-in-one"
]

def main() -> None:
    for extension in EXTENSIONS:
        subprocess.run(f"code --install-extension {extension}", shell=True)

if __name__ == "__main__":
    main()