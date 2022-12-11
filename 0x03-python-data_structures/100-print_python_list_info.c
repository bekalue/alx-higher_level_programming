/**
 * CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language.
 * Since we now know a bit of C, we can look at what is happening under the hood of Python. Let’s have fun with Python and C, and let’s look at what makes Python so easy to use.
 * 
 * All your files will be interpreted/compiled on Ubuntu 14.04 LTS
 * 
 * 
 * Create a C function that prints some basic info about Python lists.
 * 
 * Prototype: void print_python_list_info(PyObject *p);
 * Format: see example
 * Python version: 3.4
 * Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
 * OS: Ubuntu 14.04 LTS
 * Start by reading:
 * 			listobject.h
 * 			object.h
 * 			Common Object Structures(python documentation)
 * 			List Objects(python documentation)
 */
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <Python.h>
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
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, i;
	PyObject *object;
	struct _typeobject *type;
	if (strcmp(p->ob_type->tp_name, "list") == 0)
	{
		list = (PyListObject *)p;
		size = list->ob_base.ob_size;
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);
		for (i = 0; i < size; i++)
		{
			object = list->ob_item[i];
			type = object->ob_type;
			printf("Element %ld: %s\n", i, type->tp_name);
		}
	}
}
