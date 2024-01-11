#include <Python.h>
/**
 * print_python_list - prints info about python list
 * @p: PyObject list
 */

void print_python_list(PyObject *p)
{
	int size, allocated, i;
	PyObject *objct;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		objct = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(objct)->tp_name);
	}
}
