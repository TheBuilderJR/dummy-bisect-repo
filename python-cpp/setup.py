from setuptools import setup, Extension

fastmath_ext = Extension(
    "_fastmath",
    sources=["src/_fastmath.cpp"],
    language="c++",
)

setup(
    name="fastmath",
    version="0.1.0",
    description="Fast math operations with C++ extensions",
    packages=["fastmath"],
    ext_modules=[fastmath_ext],
)
