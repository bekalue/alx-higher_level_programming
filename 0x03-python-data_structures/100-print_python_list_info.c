#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include "python.h"

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
