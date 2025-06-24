# Paper 版本链接获取器

这是一个简单的Python脚本，用于获取Minecraft Paper服务端的所有版本下载链接。

## 功能特点

- 获取所有可用的Paper版本
- 自动排序（从高版本到低版本）
- 获取每个版本的最新构建下载链接
- 正确识别最新版本
- 将结果保存为JSON格式

## 安装要求

- Python 3.6+
- requests
- packaging

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

直接运行main.py即可：

```bash
python main.py
```

脚本会自动创建一个`paper-versions.json`文件，包含以下信息：
- latest: 最新版本号
- versions: 所有版本的下载链接（按版本号从高到低排序）

## 输出格式

```json
{
    "latest": "1.21.6",
    "versions": {
        "1.21.6": "https://api.papermc.io/v2/projects/paper/versions/1.21.6/builds/123/downloads/paper-1.21.6-123.jar",
        "1.21.5": "https://api.papermc.io/v2/projects/paper/versions/1.21.5/builds/456/downloads/paper-1.21.5-456.jar",
        ...
    }
}
```

## 错误处理

- 程序会处理网络错误和其他异常
- 支持通过Ctrl+C优雅退出
- 所有错误信息会被清晰地显示在控制台 