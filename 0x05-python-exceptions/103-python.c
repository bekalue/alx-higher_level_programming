/**    QUESTION

Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.
Python lists:
		Prototype: void print_python_list(PyObject *p);
		Format: see example
		If p is not a valid PyListObject, print an error message (see example)
Python bytes:
		Prototype: void print_python_bytes(PyObject *p);
		Format: see example
		Line “first X bytes”: print a maximum of 10 bytes
		If p is not a valid PyBytesObject, print an error message (see example)
Python float:
		prototype: void print_python_float(PyObject *p);
		Format: see example
		If p is not a valid PyFloatObject, print an error message (see example)
		Read /usr/include/python3.4/floatobject.h
About:
		Python version: 3.4
		You are allowed to use the C standard library
		Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
		You are not allowed to use the following macros/functions:
										Py_SIZE
										Py_TYPE
										PyList_Size
										PyList_GetItem
										PyBytes_AS_STRING
										PyBytes_GET_SIZE
										PyBytes_AsString
										PyBytes_AsStringAndSize
										PyFloat_AS_DOUBLE
										PySequence_GetItem
										PySequence_Fast_GET_SIZE
										PySequence_Fast_GET_ITEM
										PySequence_ITEM
										PySequence_Fast_ITEMS
NOTE:
	The python script will be launched using the -u option (Force stdout to be unbuffered).
	It is strongly advised to either use setbuf(stdout, NULL); or fflush(stdout) in your C functions IF you choose to use printf. The reason to that is that Pythonsprintand libCs printf don’t share the same buffer, and the output can appear disordered.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <float.h>
#include <sys/types.h>
#include <python3.4/Python.h>
#include <python3.4/object.h>
#include <python3.4/listobject.h>
#include <python3.4/floatobject.h>
#define PY_SSIZE_T_CLEAN

/**
 * print_python_bytes - Prints some basic info about a Python bytes object
 * @p: A pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	int i, bytes_len, n, error = 1;

	fflush(stdout);
	printf("[.] bytes object info\n");
	fflush(stdout);
	if ((p != NULL) && (p->ob_type != NULL)
		&& ((p->ob_type)->tp_name != NULL)
		&& (strcmp((p->ob_type)->tp_name, "bytes") == 0))
	{
		bytes_len = (int)(((PyVarObject *)p)->ob_size);
		n = bytes_len < 10 ? bytes_len : 9;
		printf("  size: %d\n", bytes_len);
		fflush(stdout);
		printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
		fflush(stdout);
		if ((n > 0) && (((PyBytesObject *)p)->ob_sval != NULL))
		{
			printf("  first %d bytes:", n + 1);
			fflush(stdout), error = 0;
			for (i = 0; i < n + 1; i++)
			{
				printf(" %02x", (unsigned char)*(((PyBytesObject *)p)->ob_sval + i));
				fflush(stdout);
			}
			printf("\n");
			fflush(stdout);
		}
	}
	if (error)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
	}
}

/**
 * print_python_float - Prints some basic info about a Python float object
 * @p: A pointer to the Python float object
 */
void print_python_float(PyObject *p)
{
	double val;
	char *buf = NULL;

	fflush(stdout);
	printf("[.] float object info\n");
	if ((p != NULL) && (p->ob_type != NULL)
		&& ((p->ob_type)->tp_name != NULL)
		&& (strcmp((p->ob_type)->tp_name, "float") == 0))
	{
		val = ((PyFloatObject *)p)->ob_fval;
		buf = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
		printf("  value: %s\n", buf);
		fflush(stdout);
	}
	else
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
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

	fflush(stdout);
	printf("[*] Python list info\n");
	fflush(stdout);
	if ((p != NULL) && (p->ob_type != NULL)
		&& ((p->ob_type)->tp_name != NULL)
		&& (strcmp((p->ob_type)->tp_name, "list") == 0))
	{
		list_len = (int)(((PyVarObject *)(p))->ob_size);
		printf("[*] Size of the Python List = %d\n", list_len);
		fflush(stdout);
		printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
		fflush(stdout);
		for (i = 0; (((PyListObject *)p)->ob_item != NULL) && (i < list_len); i++)
		{
			item = (PyObject *)*(((PyListObject *)p)->ob_item + i);
			printf("Element %d: %s\n", i, (item->ob_type)->tp_name);
			fflush(stdout);
			if ((item != NULL) && (item->ob_type != NULL)
				&& ((item->ob_type)->tp_name != NULL)
				&& (strcmp((item->ob_type)->tp_name, "bytes") == 0))
			{
				print_python_bytes(item);
			}
			else if ((item != NULL) && (item->ob_type != NULL)
				&& ((item->ob_type)->tp_name != NULL)
				&& (strcmp((item->ob_type)->tp_name, "float") == 0))
			{
				print_python_float(item);
			}
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
	}
}
