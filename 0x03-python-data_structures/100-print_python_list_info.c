#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <python3.4/python.h>
#include <python3.4/object.h>
#include <python3.4/listobject.h>
#define PY_SSIZE_T_CLEAN

/**
 * print_python_list_info - prints some basic info about a python list object
 * @p: A pointer to the python list object
 *
 * Decription - this file will be compiled as shared library with this command
 *              $ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl
 *              ,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4
 *              100-print_python_list_info.c
 */
void print_python_list_info(Pyobject *p)
{
	int i;
	int list_len = (int)PyList_size(p);
	int allocated_size = (int)((PyListobject *)p)->allocated);

	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", allocated_size);

	for (i = 0; i < list_len; i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
