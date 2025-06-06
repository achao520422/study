
# 1. docker install （ubuntu）

```bash
# 1. 卸载旧版本的docker
sudo apt purge docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras

sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd



# 2. 更新软件包并安装必要软件
sudo apt update
sudo apt install apt-transport-https curl

# 3. 导入 docker 官方的 GPG 密钥
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg


# 4. 添加 docker 镜像仓库
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 5. 更新软件包列表
sudo apt update

# 6. 安装 docker
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# docker-ce：Docker Engine。
# docker-ce-cli：用于与 Docker 守护进程通信的命令行工具。
# containerd.io：管理容器生命周期的容器运行时环境。
# docker-buildx-plugin：增强镜像构建功能的 Docker 扩展工具，特别是在多平台构建方面。
# docker-compose-plugin：通过单个 YAML 文件管理多容器 Docker
应用的配置管理插件。


# 7. 检查 docker 运行状态
sudo systemctl is-active docker

# 8. 替换国内镜像源
sudo vim /etc/docker/daemon.json

{
  "registry-mirrors": [
    "https://docker.m.daocloud.io",
    "https://mirror.baidubce.com",
    "http://hub-mirror.c.163.com",
    "https://znuzjio7.mirror.aliyuncs.com"
  ]
}



# 8. 重启 docker 服务
sudo systemctl daemon-reload
sudo systemctl restart docker

# 9. 查看 docker 信息
sudo docker info


# 10. 运行非 root 用户使用 docker 命令
sudo usermod -aG docker ${USER}
```
# 2. docker常用命令
```bash
docekr --help 获取全局指令帮助
docker run --help 直接在具体指令后加上 --help 获取特定指令的帮助
docker help <command> 可以直接在后面跟上命令获取帮助
docker --version 检查 docker 的版本
systemctl restart docker 重启 docker 服务
docker search <image-name> 镜像搜索
docker pull <image-name or image-id>:<version> 拉取镜像
docker images 列出镜像
docker rmi <image-name> 删除镜像
docekr rmi -f <image-name or image-id> 如果有基于该镜像正在运行的容器的时候，要先停止并删除容器，或者使用 -f 强制删除
docker run -d --name <container-name> <images-name> 创建并启动容器
docker ps -a 查看所有容器，包括停止的容器
docker ps 之查看运行中的容器
docker stop <container-id or container-name> 停止正在运行的容器
docker start <container-id or container-name> 启动正在运行的容器
docker restart <container-id or container-name> 重启正在运行的容器
docker exec -it <container-id or container-name> /bin/bash 进入容器
docker logs <container-id or container-name> 查看容器日志
docker rm <container-id or container-name> 删除容器
docker rm -f <container-id or container-name> 强制删除正在运行的容器
docker network ls 列出 docker 网络
docker network create <network-name> 创建自定义网络
docker network connect <network-name> <container-name> 连接容器到自定义网络
docekr network disconnect <network-name> <container-name> 断开容器与网络的连接
dcoekr system df 查看系统资源使用情况
docker system prune 清理未使用的数据
docker system prune -a 删除所有未被使用的数据
```

# 2. doker 拉取和部署 mysql
```bash
docker pull mysql   # 默认拉取最新版本 mysql

docker run -d --restart always
```


# docker 手札
```
# 查看 docker 的所有镜像
docker images
docker image ls

# 查看 docker 的所有容器
docker container ls -a
docker ps -a


# 创建镜像
docker commit container name/image
docker build


# 安装 docker 虚拟机
yum -y update
yum install -y docker


# docker 查询镜像
docker search <image-name>


# 拉取镜像
docker pull <image-naem>:<tag>


# docker 容器操作
docker pause <container-id>
docker unpause <container-id>
docker stop <container-id>
# -t:停止容器前等待的时间（默认10秒）


docker start -i <container-id>
# -i:启动容器并进入交互模式
# -a:连接容器并打印输出或错误


docker restart <container-id>
# -t:停止容器前等待的时间（默认10秒）


docekr exec -it <container-id> bash
docekr exec -it --user root <container-id> bash

doker port <container-id> # 查看容器端口映射
docker logs <container-id> # 查看容器运行日志
docker top <container-id>  # 查看容器中的进程

docker stats 查看 docker 运行状态


docekr update --ressart always <container-id>


创建docker内部网段


docker network create --subnet=172.18.0.0/24 net1
# --subnet=172.18.0.0/24:给创建的网段指定IP


查看docker内部网段


docker network inspect net1


查看docker内部的所有网段


docker network ls

删除docker内部网段

docker network rm net1
```