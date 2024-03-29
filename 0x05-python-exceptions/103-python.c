#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: PyObject representing a bytes object
 */
void print_python_bytes(PyObject *p)
{
	size_t b, i;
	char *str;
	
	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	
	if (PyBytes_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	
	str = ((PyBytesObject *)(p))->ob_sval, b = PyBytes_Size(p);
	printf("  size: %ld\n  trying string: %s\n", b, str);
	b >= 10 ? b = 10 : b++;
	printf("  first %ld bytes: ", b);
	
	for (i = 0; i < b - 1; i++)
	{
		printf("%02hhx ", str[i]);
	}
	
	printf("%02hhx\n", str[i]);
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: PyObject representing a float object
 */
void print_python_float(PyObject *p)
{
	char *str;
	double f;
	
	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	
	if (PyFloat_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	
	f = ((PyFloatObject *)(p))->ob_fval;
	str = PyOS_double_to_string(f, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

/**
 * print_python_list - Prints information about a Python list object
 * @p: PyObject representing a list object
 */
void print_python_list(PyObject *p)
{
	size_t a, size, i;
	const char *t;
	PyListObject *list;
	
	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	
	if (PyList_Check(p) == 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	
	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	a = list->allocated;
	printf("[*] Size of the Python List = %ld\n[*] Allocated = %li\n", size, a);
	for (i = 0; i < size; i++)
	{
		t = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %ld: %s\n", i, t);

		if (strcmp(t, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(t, "float") == 0)
			print_python_float(list->ob_item[i]);
	}

	fflush(stdout);
}
