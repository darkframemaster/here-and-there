# here-and-there

Hao Xue（[darkframemaster](https://github.com/darkframemaster)）的个人学习笔记。按主题分目录，从这里进。

Personal study notes (h-a-t). Topics are folders; this page is the index.

笔记是随手记的，不是教程。不少安装脚本写于 Ubuntu 16.04，包名已经过时，**运行前先打开看一遍**。

These are working notes, not a tutorial. Several install scripts target Ubuntu 16.04 and are stale — read them before you run them.

机器学习数学在独立项目 `ml-math-notes`，不放进本仓库。

Math notes for machine learning stay in the separate `ml-math-notes` project and are not vendored here.

## 语言 / Languages

* **[bash](bash/README.mkd)** — 循环、算术、echo 等小脚本。Tiny shell scripts.
* **[c](c/)** — `helloworld.c`，[basic-knowledge](c/basic-knowledge/1.gcc和编译/gcc.mkd)（GCC 阶段、glibc），[os/little_or_big.c](c/os/little_or_big.c)（字节序），[string](c/string/sub_str.c)。
* **[c++](c++/)** — `helloworld.cpp`，[basic](c++/basic/cin_cout.cpp)，[CCF 题](c++/CCF-C++/README.md)，[OpenCV](c++/opencv/README.md)（第一章图像练习与 [人脸检测源码](c++/opencv/object-detection/README.md)）。
* **[go](go/README.mkd)** — 安装与 [gotour/basic](go/gotour/basic/start.go)。入口笔记的标题曾经误写成 Ruby，已改正。
* **[js](js/README.mkd)** — JavaScript 语法笔记。
* **[php](php/README.mkd)** — 语言笔记、[Magento 2](php/Magento/README.mkd)、[Pagekit](php/pagekit/README.mkd)。
* **[python](python/README.mkd)** — 语言、Django、pygame、多进程，以及 socket / 爬虫练习。PyLucene 安装笔记也在这里。
* **[ruby](ruby/README.mkd)** — 语法小例子与 [Rails 博客笔记](ruby/rails/readme.mkd)。
* **[scala](scala/README.mkd)** — Ubuntu 安装与 `helloworld.scala`。

## 计算机网络 / Networking

来自 [dfx-note](https://github.com/darkframemaster/dfx-note)。原先的 `ComputerNetwoking.md` 已改名为 `computer-networking.md`；`HTTP.md` 并进应用层，没有另留一篇。

Imported from dfx-note. `ComputerNetwoking.md` is now `computer-networking.md`. `HTTP.md` is folded into the application-layer section.

* **[compute-networking/computer-networking.md](compute-networking/computer-networking.md)** — 分层、应用层（含 HTTP 报文）、运输层、网络层（IP、NAT、ARP）、链路层。整理自课件和《TCP/IP 详解：协议》。
* **[python/computer-networking](python/computer-networking/README.md)** — 同一主题下的 Python socket 与爬虫练习。Textbook outline and the Python labs stay in separate folders.

## 数据 / Data

* **[SQL](SQL/README.mkd)** — SQL 语句备忘，以及 [PostgreSQL](SQL/postgreSQL/README.mkd)（索引、锁、过滤、性能、[FQA](SQL/postgreSQL/FQA.md)）。
* **[mongo](mongo/mongo.md)** — [操作](mongo/operation.md)、[索引](mongo/Indexes.md)、[explain](mongo/Explain.md)、[副本集](mongo/replica_set.md)、[主从](mongo/master-slave.md)、[分片](mongo/shard.md)、[FQA](mongo/FQA.md)、[问题清单](mongo/Question.md)。
* **[redis](redis/README.mkd)** — Redis 3.2 源码安装笔记。

## 系统与工具 / Systems and tools

* **[docker](docker/docker.md)** — 安装与常用命令。`Dockerfile` 在同目录。
* **[etcd](etcd/README.md)** — 是什么、Docker / 直接安装、本地集群脚本。
* **[nginx](nginx/nginx.mkd)** — 安装、启停、站点配置（样例 [nginx/example](nginx/example)）。
* **[linux](linux/Screen.md)** — GNU Screen 快捷键。
* **[git](git/git.mkd)** — 工作区、暂存区、常用命令。
* **[svn](svn/README.mkd)** — 安装与 checkout / commit。
* **[tools/wireShark_INS.sh](tools/wireShark_INS.sh)** — Wireshark 安装脚本（写死了用户名，先读再跑）。

## Web

* **[html-css](html-css/html.mkd)** — HTML 与 [CSS](html-css/css.mkd)，附一个静态页。目录原先叫 `html&css`。
* **[web_roadmap](web_roadmap/roadmap.mkd)** — 学习路线链接。[动态网站笔记](web_roadmap/build_dynamic_website/dynamic-web-design.mkd) 与 lecture 示例，[书签汇总](web_roadmap/Marked.md)。

## 机器学习 / Machine learning

* **[tensorflow](tensorflow/README.mkd)** — 很早的安装笔记，以及 [basic](tensorflow/basic/variable.py) 里的 variable / session / feed 示例。
* **[sklearn/intro.ipynb](sklearn/intro.ipynb)** — 来自 [notes](https://github.com/darkframemaster/notes)。加载 iris（150×4）和 digits，并画出最后一张数字图。标题「监督学习：从高维观察预测输出变量」下面的代码单元是空的，没有补写。
* `ml-math-notes` 保持独立，不要合并进来。和 TensorFlow 笔记内容不重叠，所以 sklearn 单独放。

`sklearn/intro.ipynb` loads iris and digits, then stops. The supervised-learning cell is empty and was left empty. Do not merge `ml-math-notes` into this repo.

## 课程、阅读、杂项 / Courses, reading, misc

课程和阅读笔记尽量原样保留。University and reading notes are kept as-is unless a file was empty or a duplicate.

* **[university](university/)** — [软件工程](university/software-engineering/software-engineering.md)、[编译原理](university/编译原理/编译原理.md)、[数据库](university/数据库/DB.md)、[系统分析与设计](university/系统分析与设计/系统分析与设计.mkd)、[密码学](university/密码学/Cryptography.mkd)、[术语](university/hotword.mkd)。课件 ppt/pptx 仍在对应目录。
* **[reading_note/sicp.mkd](reading_note/sicp.mkd)** — SICP 题词。
* **[just-for-fun](just-for-fun/)** — [OpenGL 小游戏](just-for-fun/a-game-of-opengl-master/main.cpp)、[图片转字符](just-for-fun/pic-python/readme.mkd)。

## 环境脚本 / Environment scripts

仍保留、但针对旧 Ubuntu 的安装脚本：

Still in the tree, aimed at old Ubuntu releases:

* `php/setPHP.sh`、`php/setPHP_5.sh`、`php/Magento/setUp.sh`
* `python/setPython.sh`、`python/setPython2.sh`、`python/setPython_15.sh`
* `docker/setup.sh`、`etcd/install.sh`、`tools/wireShark_INS.sh`

`SQL/uninstallMysql.sh` 已删除。它会递归删掉 MySQL 数据目录，并卸载 AppArmor。

`SQL/uninstallMysql.sh` was removed. It recursively deleted the MySQL data directory and uninstalled AppArmor.
