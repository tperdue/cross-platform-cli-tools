import os
import subprocess

tools_dir = "tools"
dist_dir = "dist"

os.makedirs(dist_dir, exist_ok=True)

for tool in os.listdir(tools_dir):
    if tool.endswith(".py"):
        script_path = os.path.join(tools_dir, tool)
        output_path = os.path.join(dist_dir, os.path.splitext(tool)[0])
        print(f"Building {tool}...")
        subprocess.run(["pyinstaller", "--onefile", "--distpath", dist_dir, script_path])
