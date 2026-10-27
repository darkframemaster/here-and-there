# Object detection

源码来自原来的 `objectDetection.zip`（OpenCV 的 facedetect 示例）。压缩包里的可执行文件，以及多份重复的 Haar / LBP cascade XML，没有再放进仓库。级联文件用本机 OpenCV 的 data 目录，常见路径是 `/usr/share/opencv/haarcascades/` 或 `/usr/share/opencv4/haarcascades/`。

Sources from the old zip (OpenCV facedetect samples). Compiled binaries and the duplicated cascade XML files were not kept. Use the cascades shipped with your OpenCV install.

编译与本目录其它 OpenCV 例子相同：

```bash
g++ file.cpp -o prog $(pkg-config --cflags --libs opencv)
```

## objectDetection.cpp / objectDetection2.cpp

这两个程序不读命令行。它们在当前目录按文件名加载级联，然后打开默认摄像头：

* `objectDetection.cpp` — `haarcascade_frontalface_alt.xml`、`haarcascade_eye_tree_eyeglasses.xml`
* `objectDetection2.cpp` — `lbpcascade_frontalface.xml`、`haarcascade_eye_tree_eyeglasses.xml`

把对应 XML 链接到当前目录后再运行。Symlink those files into the working directory before running.

## facedetect.cpp / ufacedetect.cpp

这两个程序接受 `--cascade`、`--nested-cascade`、`--scale`。旧笔记里的调用方式：

```bash
./facedetect --cascade="/usr/share/opencv/haarcascades/haarcascade_frontalface_alt_tree.xml" --nested-cascade="/usr/share/opencv/haarcascades/haarcascade_eye.xml" --scale=1.3
./ufacedetect --cascade="/usr/share/opencv/haarcascades/haarcascade_frontalface_alt_tree.xml" --nested-cascade="/usr/share/opencv/haarcascades/haarcascade_eye.xml" --scale=1.3
```
