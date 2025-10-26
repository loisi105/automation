The Setup and intended use is explained below. Follow the setup instructions in the exact order.

Download python
1. download python from the link: https://www.python.org/downloads/
  Note: For development the Version 3.12. was used. 
2. follow the installer and check both boxes from the first screen

Download pip
1. Start cmd as Administrator
2. run the command:  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
3. run the command:  py get-pip.py
4. Add pip to Path -> see "configurePath.png" from the source folder

Download pillow
1. Start cmd as Administrator
2. run the command: pip install Pillow

Test if pillow is installed and working
1. Start a new cmd session
2. run the command: python
3. run the command: import PIL
4. run the command: PIL.__version__
5. the output should be '11.1.0' or higher

All library are now successfully installed.

---

The Program can now be executed via commandline.

A template of a script, which has the needed command in it, is in the source folder and is named "_start.bat".
Before "_start.bat" works as intended, the absolute path to the python file most likely has to be edited. 
