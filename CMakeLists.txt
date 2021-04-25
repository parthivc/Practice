cmake_minimum_required(VERSION 3.17)
project(Coding\ Practice)

set(CMAKE_CXX_STANDARD 14)
include_directories(. )



add_executable(
        main ${PROJECT_SOURCE_DIR}/main.cpp
        # main ${PROJECT_SOURCE_DIR}/Assessments/hrtOA.cpp
)