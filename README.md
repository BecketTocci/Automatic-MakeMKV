# Automatic-MakeMKV
A semi-automatic DVD drive ripper. Cannot handle multiple disk drives at the moment.
# Usage
Run `main.py` and enter the requested info.
Example:
![image](https://github.com/user-attachments/assets/15676fae-1015-41e9-b458-a827538a6c84)

# Installation
First, clone this repo. Then install MakeMKV and its python wrapper.
The python wrapper can be found here: https://pypi.org/project/makemkv/.
Then, run `main.py`.

# Planned changes
Ask which DVD drive to use, default to drive 0 if no input.
If a rip fails and the user restarts, all finished rips get ignored and we don't try to rip them again.
