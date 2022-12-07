#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <python3.4/Python.h>
#include <python3.4/object.h>
#include <python3.4/listobject.h>
#include <python3.4/listobject.h>
#define PY_SSIZE_T_CLEAN

/**
 * print_python_bytes - Prints some basic info about a Python bytes object
 * @p: A pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	int i, bytes_len, n;

	printf("[.] bytes object info\n");
	if ((p != NULL) && (p->ob_type != NULL) && ((p->ob_type)->tp_name != NULL)
		&& (strcmp((p->ob_type)->tp_name, "bytes") == 0))
	{
		bytes_len = (int)(((PyVarObject *)(p))->ob_size);
		n = bytes_len < 10 ? bytes_len : 9;
		printf("  size: %d\n", bytes_len);
		printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
		if (n > 0)
		{
			printf("  first %d bytes:", n + 1);
			for (i = 0; i < n + 1; i++)
			{
				printf(" %02x", (unsigned char)*(((PyBytesObject *)p)->ob_sval + i));
			}
			printf("\n");
		}
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_list - Prints some basic info about a Python list object
 * @p: A pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
	int i, list_len;
	PyObject *item = NULL;

	printf("[*] Python list info\n");
	if ((p != NULL) && (p->ob_type != NULL) && ((p->ob_type)->tp_name != NULL)
		&& (strcmp((p->ob_type)->tp_name, "list") == 0))
	{
		list_len = (int)(((PyVarObject *)(p))->ob_size);
		printf("[*] Size of the Python List = %d\n", list_len);
		printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
		for (i = 0; i < list_len; i++)
		{
			item = (PyObject *)*(((PyListObject *)p)->ob_item + i);
			printf("Element %d: %s\n", i, (item->ob_type)->tp_name);
			if ((item != NULL) && (item->ob_type != NULL)
				&& ((item->ob_type)->tp_name != NULL)
				&& (strcmp((item->ob_type)->tp_name, "bytes") == 0))
			{
				print_python_bytes(item);
			}
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}
}
