// mylib.h
#include <Eigen/Dense>
#include <cmath>

using Eigen::Matrix, Eigen::Dynamic;
typedef Matrix<std::complex<double>, Eigen::Dynamic, Eigen::Dynamic> myMatrix;
class MyClass {

    int N;
    double a;
    double b;

public:

    Eigen::VectorXd v_data;
    Eigen::VectorXd v_gamma;

    MyClass(){}
    MyClass( double a_in, double b_in, int N_in) 
    {
        N = N_in;
        a = a_in;
        b = b_in;
    }

    void run() 
    { 
        v_data = Eigen::VectorXd::LinSpaced(N, a, b); 

        auto gammafunc = [](double it) { return std::tgamma(it); };
        v_gamma = v_data.unaryExpr(gammafunc);
    }
};
// pywrap.cpp
#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include "mylib.h"

namespace py = pybind11;
constexpr auto byref = py::return_value_policy::reference_internal;

PYBIND11_MODULE(MyLib, m) {
    m.doc() = "optional module docstring";

    py::class_<MyClass>(m, "MyClass")
    .def(py::init<double, double, int>())  
    .def("run", &MyClass::run, py::call_guard<py::gil_scoped_release>())
    .def_readonly("v_data", &MyClass::v_data, byref)
    .def_readonly("v_gamma", &MyClass::v_gamma, byref)
    ;
}

cmake_minimum_required(VERSION 3.10)

project(MyLib)
set(CMAKE_CXX_STANDARD 20)
set(PYBIND11_PYTHON_VERSION 3.6)
set(CMAKE_CXX_FLAGS "-Wall -Wextra -fPIC")

find_package(pybind11 REQUIRED)
find_package(Eigen3 REQUIRED)

pybind11_add_module(${PROJECT_NAME} pywrap.cpp)

target_compile_definitions(${PROJECT_NAME} PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
target_include_directories(${PROJECT_NAME} PRIVATE ${PYBIND11_INCLUDE_DIRS})
target_link_libraries(${PROJECT_NAME} PRIVATE Eigen3::Eigen)

import sys
sys.path.append("build/")
from MyLib import MyClass

import matplotlib.pyplot as plt

Simulation = MyClass(-4,4,1000)
Simulation.run()

plt.plot(Simulation.v_data, Simulation.v_gamma, \
"--", linewidth = 3, color=(1,0,0,0.6),label="Function Value")
plt.ylim(-10,10)
plt.xlabel("x")
plt.ylabel("($f(x) = \gamma(x)$)")
plt.title("(Gamma Function: $\gamma(z) = \int_0^\infty x^{z-1} e^{-x} dx$)",fontsize = 18);
plt.show()