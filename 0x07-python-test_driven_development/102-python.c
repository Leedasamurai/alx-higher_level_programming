#include <pyconfig.h>

/**
 * print_python_string - prints python string
 * p: object python object
 */

void print_python_string(PyObject *p);

void print_python_string(PyObject *p)
{
	Py_ssize_t i, length;
	Py_UNICODE *unicode_str;
	PyCompactUnicodeObject *compact_unicode;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	compact_unicode = (PyCompactUnicodeObject *)p;

	printf("  type: compact unicode object\n");

	length = compact_unicode->length;
	unicode_str = compact_unicode->utf16;
	printf("  length: %ld\n", length);
	printf("  value: ");

	for (i = 0; i < length; i++)
	{
		printf("%c", unicode_str[i]);
	}

	printf("\n");
}

