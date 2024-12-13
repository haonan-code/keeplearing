## 起因

Windows 平台执行下列代码没有问题

```python
cmd = '"{}" -i "{}" -show_entries stream=width,height -of csv=p=0:s=x -v error'.format(ffprobe_path, file_path)

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
```

同样代码在 Linux 平台则无法执行，需要给 `subprocess.Popen()` 函数加上 `shell = True` 参数即可运行成功

```python
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
```

## 原因

### Windows 平台：

- 在 `shell=False` 的情况下，`subprocess.Popen()` 仍然能够执行简单的字符串命令，因为 Windows 的实现会自动解析和查找可执行文件的路径。
- 因为 `CreateProcess`（Windows 的底层 API）支持直接运行命令字符串。

### Linux 平台：

- 在 `shell=False` 的情况下，`subprocess.Popen()` 需要一个命令列表（如 `["ls", "-l"]`），或者提供完整路径的可执行文件。
- 如果提供的是字符串命令（如 `ls -l | grep txt`），需要 `shell=True`，否则会抛出错误，因为 Linux 默认不会自动通过 shell 来解释命令字符串。

## 结论

本例中通过 ffprobe 获取视频尺寸的命令为字符串命令。Windows平台会自动解析传入的字符串命令，Linux 平台不支持自动解析字符串命令，需要添加 `shell=True` 参数通过 shell 来解释命令字符串。

## 扩展

### 参数 shell
 
shell 参数设置是否在单独的 shell 中执行命令。如果`shell=True`，则是派生一个新的 shell 来解释执行命令。如果你使用 Python 主要是为了增强它在大多数系统 shell 上提供的控制流，并且还想方便的访问 shell 特性，如 shell 的管道符、文件通配符、环境变量扩展或者 ~ 扩展到 home 目录等，这个参数将非常有用。

### 向 subprocess.Popen() 等类似函数传递命令方式：

#### 1. 简单命令字符串

定义：将一段完整的命令拼接成一个单独的字符串，例如:

```python
command = "ls -l | grep txt"
subprocess.Popen(command, shell=True)
```

特点：

- 包括可执行程序、参数、以及可能的 shell 特性（如管道 `|`、重定向 `>`、逻辑操作符 `&&` 等）。
- 只有在 `shell=True` 时才会通过系统的 shell（如 Linux 的 `/bin/sh` 或 Windows 的 `cmd.exe`）解析和执行。

优点：简洁，符合直接在终端输入命令的习惯

缺点：需要 shell=True 才能解析，存在命令注入风险，不推荐用于处理用户输入的动态内容。

#### 2. 命令列表

定义：将命令和其参数分开表示，每个部分作为一个列表项，列表中的第一个元素是要执行的可执行文件或程序。例如：

```python
command = ["ls", "-l"]
subprocess.Popen(command, shell=False)
```

特点：

- 适用于 `shell=False` 的场景。
- 不支持复杂的 shell 特性（如管道、重定向、逻辑操作符等）。
- 不依赖系统 shell，直接调用指定的程序。

优点：安全（避免命令注入风险），明确（不需要 shell 解析命令）。

缺点：不支持直接执行包含 shell 特性的复杂命令。

#### 3. 两者区别

| **特性**         | **简单命令字符串**              | **命令列表**          |
| -------------- | ------------------------ | ----------------- |
| **表示方式**       | 单一字符串                    | 列表，元素是程序和参数       |
| **Shell 特性支持** | 需要`shell=True` 支持        | 不支持 shell 特性      |
| **安全性**        | 有命令注入风险                  | 安全（避免注入，直接执行）     |
| **依赖**         | 依赖 shell （`shell=True`时） | 不依赖 shell（直接调用程序） |
| **执行方式**       | 由 shell 解析并运行            | 直接运行指定的可执行程序      |

#### 4. 使用场景

**使用简单命令字符串：**

- 需要利用 shell 特性（管道、重定向等）。
- 确定输入安全，命令不会受到用户动态输入影响。

**使用命令列表：**

- 避免命令注入风险（如用户提供的参数）。
- 运行简单的命令或程序，不需要 shell 特性。

## 参考
https://www.cnblogs.com/ywsun/p/13847879.html#!comments
