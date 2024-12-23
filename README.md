# Cross Platform Command Tools 🚀

### Overview
The inspiration for this project came when my MacBook died, forcing me to code on a Windows machine. One of my favorite commands on macOS was `tree`, which displays directory structures beautifully. Unfortunately, the Windows equivalent didn’t quite meet my needs. So, I decided to build my own version of `tree` in Python and compile it into an executable.

This project hopes to assist Python developers who need to create and carry custom command-line tools across different operating systems. By providing a Python-based framework, it ensures these tools are both portable and easy to use.

---

## Project Structure 📁
The project is organized as follows:

```
project_root/
├── tools/                 # Directory containing individual tool scripts
│   ├── tree.py           # Example tool: directory tree printer
│   └── other_tool.py     # Placeholder for additional tools
├── build_executable.py   # Script for building tools into executables
├── setup.py              # Setup script for installation
└── README.md             # Project documentation
```
- **tools/**: Contains the individual Python scripts for tools.
- **build_executable.py**: Automates the process of building tools into standalone executables.
- **setup.py**: Defines the installation process and command-line entry points.
- **README.md**: You're reading it!

---

## Installation & Setup ⚙️

### Prerequisites
- Python 3.6 or later
- pip (Python package manager)

### Clone the Repository
```bash
git clone https://github.com/yourusername/cross-platform-command-tools.git
cd cross-platform-command-tools
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Build Tools into Executables 🛠️
To convert Python scripts into standalone executables:

1. Run the build script:
   ```bash
   python build_executable.py
   ```
2. The executables will be generated in the `dist/` directory.

---

## Install Tools on Your System 📂

### Windows
1. Move the executable to a directory in your PATH (e.g., `C:\Windows\System32`).
   ```powershell
   move dist\treey.exe C:\Windows\System32
   ```
2. Verify installation by running the command:
   ```powershell
   treey --help
   ```

### macOS/Linux
1. Move the executable to `/usr/local/bin`:
   ```bash
   sudo mv dist/treey /usr/local/bin
   ```
2. Verify installation by running the command:
   ```bash
   treey --help
   ```

---

## Project Status & Collaboration 💤
I'll try to keep this projected updated and well maintained as possible. Feel free to fork it, adapt it, or use it however you like. Giving credit is appreciated but not required. Make it your own! 🌟

---

## Contact Me 📧
I created this project to showcase my skills and build a portfolio. If you have any questions, would like to collaborate on projects, or discuss employment opportunities, feel free to reach out!

- **Email**: your.email@example.com
- **GitHub**: [tperdue](https://github.com/tperdue)
- **LinkedIn**: [Tim Perdue](https://www.linkedin.com/in/tperdue/)

Looking forward to connecting with you! ✨

