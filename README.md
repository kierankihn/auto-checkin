# 洛谷自动签到脚本

*Powered by Kieran Kihn*

## 开始之前

本脚本由 Kieran Kihn 开发，使用 `Python` + `schedule` + `requests` 实现了洛谷的自动签到，防止你忘记签到而痛失连续签到日期

在默认情况下，本脚本会在每天 `10:00`（时区为 `Asia/Shanghai`，即 `UTC+8`）进行洛谷打卡，目前暂不支持修改签到时间

为了安全，本脚本不建议使用密码登录洛谷，而是使用 `token` + `uid` 的方式直接获取登录状态

你可以在 `Chrome` 中按下 F12 打开 `DevTools`，在 `Application（应用）> Cookie > https://luogu.com.cn` 中找到你的 `__client_id` 与 `_uid`

在使用本脚本之前请确保你有一个文本编辑器，例如 `Visual Studio Code`，`notepad++`，或者记事本

本脚本的配置文件为 `json` 格式，格式如同 `config-example.json`：

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

1. 下载最新的 Release 可执行文件
2. 创建 config.json 文件（按照上述格式）
3. 双击执行！
4. 你还可以使用 [`winsw`](https://github.com/winsw/winsw) 或者使用 `sc` 命令将本脚本注册为 Windows 服务，以实现开机自启 & 隐藏命令行窗口

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

## 构建

### 构建 Linux / Windows 可执行程序

1. 安装 Python
2. 克隆仓库
```sh
$ git clone https://github.com/kierankihn/auto-checkin.git
```
3. 安装依赖
```sh
$ pip install -r requirements-dev.txt
```
4. 打包程序
```sh
$ pyinstaller -F main.py
```

### 构建 Docker 镜像

1. 安装 Docker 和 Docker Compose
2. 克隆仓库
```sh
$ git clone https://github.com/kierankihn/auto-checkin.git
```
3. 打包镜像
```sh
$ docker build -t kierankihn/auto-checkin:latest .
```

## 开发

如果你遇到了任何问题，欢迎提出 issue，提出 issue 时请务必详细地描述你所遇到的状况，最好附上你的日志

如果你想为此项目做出共享，欢迎提交 Pull request

## To do list

- [x] 使用 Github Action 自动推送 Docker 镜像
- [ ] 允许用户在 config.json 中自定义每日签到时间（使用时间字面值 / cron 表达式）
- [ ] 增加打卡后向 Telegram bot / Server 酱 / PushDeer 推送打卡日志（打卡成功 / 失败，每日运势等）的功能
- [ ] 增加使用密码登录功能
- [ ] 增加 Github Action 部署方式