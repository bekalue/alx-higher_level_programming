#!/usr/bin/bash
# set PY_BIN_PATH /usr/bin/python3.4
# set PY_INC_PATH /usr/include/python3.4
set PY_BIN_PATH ~/apps/Python-3.4.10/python
set PY_INC_PATH ~/apps/Python-3.4.10/Include/:"$HOME/apps/Python-3.4.10/"
gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I$PY_INC_PATH 102-python.c
# [ $status -eq 0 ] && $PY_BIN_PATH ./102-python.py
