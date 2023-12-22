# 洛谷自动签到脚本

*Powered by Kieran Kihn*

## 开始之前

在使用本脚本之前请确保你已经安装了 `python3`，并且有一个文本编辑器，例如 `Visual Studio Code`，`notepad++`，或者记事本

本脚本的配置文件为 `json` 格式，格式如同 `config-example.json`，例如：

```js
{
    "token": [
        {
            "__client_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", // 你的洛谷账户 token
            "_uid": 123456                                             // 你的洛谷账户 uid
        },
        {
            "__client_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "_uid": 123456
        }
    ]
}
```

请先在浏览器中登录洛谷以获取你的账户 `token`，然后按照格式创建 `config.json` 文件，并填入你的 `token` 和 `uid`

## 快速开始

### 在 Windows 上部署脚本

1. 克隆仓库
```sh
$ git clone https://github.com/kierankihn/auto-checkin.git
```
2. 创建 config.json 文件
3. 安装依赖
```sh
pip install -r requirements.txt
```
4. 启动脚本
```sh
$ python ./main.py
```

- 你还可以使用 [`winsw`](https://github.com/winsw/winsw) 或者使用 `sc` 命令将本脚本注册为 Windows 服务，以实现开机自启 & 隐藏命令行窗口

### 在 Docker 内部署

在 Linux 系统中，我们推荐使用 `Docker` & `Docker Compose` 以实现快速部署

1. 在开始之前，请确保你已经安装了 `Docker` 和 `Docker Compose`
2. 创建文件夹
```sh
$ mkdir auto-checkin
$ cd auto-checkin
```
3. 创建 `config.json` 文件
4. 创建 `docker-compose.yaml` 文件
```yaml
version: '3'
services:
  auto-checkin:
    image: ghcr.io/kierankihn/auto-checkin:latest
    volumes:
      - ./config.json:/app/config.json
    environment:
      - TZ=Asia/Shanghai
```
5. 拉起容器
```sh
$ docker-compose up -d
```
6. 查看日志
```sh
$ docker-compose logs
```
7. 结束容器
```sh
$ docker-compose down
```