#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints information about a Python list.
 * @p: Pointer to the PyObject representing a Python list.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size;

    /* Print basic information about the Python list */
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    /* Print detailed information about each element in the list */
	for (i = 0, size = PyList_Size(p); i < size; ++i)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
