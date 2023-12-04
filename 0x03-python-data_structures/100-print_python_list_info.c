#include <Python.h>

/**
 * print_python_list_info - a function to outputs basic info
 * about Python lists.
 * @p: a pointer to PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, Memalloc, m;
	PyObject *obj;

	size = Py_SIZE(p);
	Memalloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", Memalloc);

	for (m = 0; m < size; m++)
	{
		printf("Element %d: ", m);

		obj = PyList_GetItem(p, m);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
