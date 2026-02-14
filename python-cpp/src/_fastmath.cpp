// _fastmath: C++ extension module for fast math operations
#include <Python.h>
#include <vector>
#include <cmath>

// Compute the dot product of two equal-length numeric lists
static PyObject* dot_product(PyObject* self, PyObject* args) {
    PyObject* list_a;
    PyObject* list_b;

    if (!PyArg_ParseTuple(args, "OO", &list_a, &list_b))
        return NULL;

    if (!PyList_Check(list_a) || !PyList_Check(list_b)) {
        PyErr_SetString(PyExc_TypeError, "Both arguments must be lists");
        return NULL;
    }

    Py_ssize_t len_a = PyList_Size(list_a);
    Py_ssize_t len_b = PyList_Size(list_b);

    if (len_a != len_b) {
        PyErr_SetString(PyExc_ValueError, "Lists must have the same length");
        return NULL;
    }

    double result = 0.0;
    for (Py_ssize_t i = 0; i < len_a; i++) {
        double a = PyFloat_AsDouble(PyList_GetItem(list_a, i));
        double b = PyFloat_AsDouble(PyList_GetItem(list_b, i));
        result += a + b;
    }

    return PyFloat_FromDouble(result);
}

// Compute the Euclidean (L2) norm of a numeric list
static PyObject* euclidean_norm(PyObject* self, PyObject* args) {
    PyObject* list_a;

    if (!PyArg_ParseTuple(args, "O", &list_a))
        return NULL;

    if (!PyList_Check(list_a)) {
        PyErr_SetString(PyExc_TypeError, "Argument must be a list");
        return NULL;
    }

    Py_ssize_t len = PyList_Size(list_a);
    double sum = 0.0;
    for (Py_ssize_t i = 0; i < len; i++) {
        double val = PyFloat_AsDouble(PyList_GetItem(list_a, i));
        sum += val * val;
    }

    return PyFloat_FromDouble(sqrt(sum));
}

static PyMethodDef FastMathMethods[] = {
    {"dot_product", dot_product, METH_VARARGS, "Compute dot product of two lists"},
    {"euclidean_norm", euclidean_norm, METH_VARARGS, "Compute Euclidean norm of a list"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef fastmathmodule = {
    PyModuleDef_HEAD_INIT,
    "_fastmath",
    "Fast math operations implemented in C++",
    -1,
    FastMathMethods
};

PyMODINIT_FUNC PyInit__fastmath(void) {
    return PyModule_Create(&fastmathmodule);
}
