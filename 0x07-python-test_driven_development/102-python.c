#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <python3.4/Python.h>
#include <python3.4/object.h>
#include <python3.4/unicodeobject.h>
#define PY_SSIZE_T_CLEAN

/**
 * print_python_string - Prints some basic info about a Python string object
 * @p: A pointer to the Python string object
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t str_len;
	Py_UNICODE *str = NULL;
	char *fmt_str = "  value: %ls\n";

	fflush(stdout);
	printf("[.] string object info\n");
	fflush(stdout);
	if ((p != NULL) && (p->ob_type != NULL)
		&& ((p->ob_type)->tp_name != NULL)
		&& (strcmp((p->ob_type)->tp_name, "str") == 0))
	{
		str = PyUnicode_AsWideCharString(p, &str_len);
		printf("  type: %s%s\n",
			   ((PyASCIIObject *)p)->state.compact ? "compact " : "",
			   ((PyASCIIObject *)p)->state.ascii ? "ascii" : "unicode object");
		fflush(stdout);
		printf("  length: %d\n", (int)str_len);
		fflush(stdout);
		printf(fmt_str, str);
		fflush(stdout);
		PyMem_Free(str);
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
		fflush(stdout);
	}
}
