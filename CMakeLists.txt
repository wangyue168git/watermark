set(OpenCV_DIR /opt/homebrew/Cellar/opencv/4.5.5_3)
add_executable(MyExecutable dct_c.cpp)
find_package(OpenCV REQUIRED)