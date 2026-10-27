# opencv
...

##install in ubuntu 2015.04
[download opencv](http://opencv.org)

`sudo apt-get install build-essential libgtk*-dev libavcodec-dev libavformat-dev libjepg-dev libtiff*-dev cmake libswscale-dev libjasper-dev`

`cmake .`

**wait...**

`make`

`sudo make install`

**config library:**

`cd /etc/ld.so.conf.d`

`su`

`touch opencv.conf`

`echo "/usr/local/lib" >> opencv.conf`

`ldconfig`

`echo "PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig" >> /etc/bash.bashrc`

`echo "export PKG_CONFIG_PATH" >> /etc/bash.bashrc`

`exit`

**test:**

`cd /PATH/TO/OPENCV/samples/cpp/example_cmake`

`make`

`./opencv_example`

**makefile**

using command:

>g++ main.cpp -o main `pkg-config --cflags --libs opencv`

or cmake(CMakeList.txt):

`cmake_minimum_required(VERSION 2.8)`

`project(Hello)`

`find_package(OpenCV REQUIRED)`

`add_executable(Hello main.cpp)`

`target_link_libraries(Hello ${OpenCV_LIBS})`

## Run example
人脸检测示例在 [object-detection](object-detection/README.md)。原来的 `objectDetection.zip` 已拆成源码；级联 XML 用本机 OpenCV 自带的文件。

Face-detection sources live in [object-detection](object-detection/README.md). The old zip was unpacked to sources only; use the Haar cascades from your OpenCV install.

##enjoy your opencv！
[help](https://www.douban.com/note/478450231)
