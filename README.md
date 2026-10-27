# here-and-there

这里是统一的学习笔记仓库（here-and-there / h-a-t）。原来散落在 [dfx-note](https://github.com/darkframemaster/dfx-note) 和 [notes](https://github.com/darkframemaster/notes) 里的笔记已按原文件并入本仓库。已有的主题目录仍留在仓库根目录，内容未改。

This repository is the unified study-notes hub (here-and-there / h-a-t). Notes that lived in [dfx-note](https://github.com/darkframemaster/dfx-note) and [notes](https://github.com/darkframemaster/notes) are imported here as the original files. Existing topic directories stay at the repository root and are unchanged.

更早的简短说明仍在 [README.mkd](README.mkd)：各语言目录以语言命名，默认含安装说明（`README.mkd`），语法笔记常在 `language.mkd`；代码在 Ubuntu 16.04 LTS 下编写并测试；语言目录里的环境脚本请先阅读再运行。

The earlier short note remains in [README.mkd](README.mkd): language directories are named after the language and usually include install notes (`README.mkd`), with syntax often in `language.mkd`. The code was written and tested on Ubuntu 16.04 LTS. Read any environment shell scripts in those directories before running them.

## 已有主题 / Existing topics

只列仓库根目录下原有的主题文件夹。

Top-level topic folders that were already in this repository:

- [bash](bash/)
- [c](c/)
- [c++](c++/)
- [docker](docker/)
- [etcd](etcd/)
- [git](git/)
- [go](go/)
- [html&css](html%26css/)
- [js](js/)
- [just-for-fun](just-for-fun/)
- [linux](linux/)
- [mongo](mongo/)
- [nginx](nginx/)
- [php](php/)
- [python](python/)
- [reading_note](reading_note/)
- [redis](redis/)
- [ruby](ruby/)
- [scala](scala/)
- [SQL](SQL/)
- [svn](svn/)
- [tensorflow](tensorflow/)
- [tools](tools/)
- [university](university/)
- [web_roadmap](web_roadmap/)

其中 [web_roadmap](web_roadmap/) 是 Web 开发相关，[reading_note](reading_note/) 是读书笔记，[just-for-fun](just-for-fun/) 是随手写的代码，[university](university/) 是大学课程材料。

Among these, [web_roadmap](web_roadmap/) is about web development, [reading_note](reading_note/) holds book notes, [just-for-fun](just-for-fun/) is code written for fun, and [university](university/) holds university course materials.

## compute-networking

来源：[dfx-note](https://github.com/darkframemaster/dfx-note) 的 `master` 分支，`compute-networking/` 原样放到仓库根目录。文件名保持原样（含 `ComputerNetwoking.md` 的拼写）。

Imported from [dfx-note](https://github.com/darkframemaster/dfx-note) `master`. `compute-networking/` is copied to the repository root. Original filenames are kept, including the spelling of `ComputerNetwoking.md`.

- [ComputerNetwoking.md](compute-networking/ComputerNetwoking.md) — 计算机网络笔记（考试、面试，以及后来遇到的网络问题；整理自课件和《TCP/IP 详解：协议》）
- [HTTP.md](compute-networking/HTTP.md) — HTTP 链接与报文格式

- [ComputerNetwoking.md](compute-networking/ComputerNetwoking.md) — computer-networking notes (exams, interviews, and later day-to-day network questions; drawn from course notes and *TCP/IP Illustrated*)
- [HTTP.md](compute-networking/HTTP.md) — HTTP connections and message format

## sklearn

来源：[notes](https://github.com/darkframemaster/notes) 的 `master` 分支。`sklearn_tutorial/intro.ipynb` 放到 `sklearn/intro.ipynb`。

Imported from [notes](https://github.com/darkframemaster/notes) `master`. `sklearn_tutorial/intro.ipynb` is at `sklearn/intro.ipynb`.

- [intro.ipynb](sklearn/intro.ipynb)
  - 数据加载：`sklearn.datasets` 的 iris（150×4）和 digits
  - 标题「监督学习：从高维观察预测输出变量」；其后的代码单元是空的

- [intro.ipynb](sklearn/intro.ipynb)
  - Data loading: iris (150×4) and digits from `sklearn.datasets`
  - Heading “监督学习：从高维观察预测输出变量”; the code cell under it is empty

## 来源与相关仓库 / Sources and a related repo

| 仓库 | 关系 |
|------|------|
| [dfx-note](https://github.com/darkframemaster/dfx-note) | `compute-networking/` 的来源。笔记已并入本仓库，该仓库之后可以归档。 |
| [notes](https://github.com/darkframemaster/notes) | `sklearn/intro.ipynb` 的来源。笔记已并入本仓库，该仓库之后可以归档。 |
| [ml-math-notes](https://github.com/darkframemaster/ml-math-notes) | 相关但独立的项目，继续单独维护，**没有**导入本仓库。 |

| Repository | Relationship |
|------------|----------------|
| [dfx-note](https://github.com/darkframemaster/dfx-note) | Source of `compute-networking/`. Those notes now live here; that repo can be archived later. |
| [notes](https://github.com/darkframemaster/notes) | Source of `sklearn/intro.ipynb`. That notebook now lives here; that repo can be archived later. |
| [ml-math-notes](https://github.com/darkframemaster/ml-math-notes) | A related project that stays separate. Nothing from it is imported into this repository. |
