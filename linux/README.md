# 本次 linux 操作基于 centos

# 1. 查看 centos 的 ssh 服务是否开启
```bash
rpm -qa|grep -E "openssh"
# 如果 结果如下
# [root@localhost ~]# rpm -qa|grep -E "openssh"
# openssh-clients-7.4p1-21.el7.x86_64
# openssh-server-7.4p1-21.el7.x86_64
# openssh-7.4p1-21.el7.x86_64
# 则说明已经安装了 ssh 服务
# 否则需要安装 openssh --->  yum install openssh-server -y
```
# 2. linux 常用命令
```text
uname 的食用方法
SYNOPSIS
       uname [OPTION]...

DESCRIPTION
       Print certain system information.  With no OPTION, same as -s.
       输出特定的系统信息，如果使用命令的时候不提供任何 option(选项的时候),与 -s 选项输出的相同
       -a, --all
              print all information, in the following order, except omit -p and -i if unknown
              输出所有信息，对于以下命令，除非省略 -p 和 -i （如果不知道）
              如 Linux ubuntu 5.4.0-150-generic #167~18.04.1-Ubuntu SMP Wed May 24 00:51:42 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux

       -s, --kernel-name
              print the kernel name
              输出内核名字
              如 Linux

       -n, --nodename
              print the network node hostname
              输出网络网络节点的主机名
              如 ubuntu

       -r, --kernel-release
              print the kernel release
              输出系统内核的版本信息
              如 5.4.0-150-generic
       -v, --kernel-version
              print the kernel version
              输出内核版本
              如 #167~18.04.1-Ubuntu SMP Wed May 24 00:51:42 UTC 2023

       -m, --machine
              print the machine hardware name

       -p, --processor
              print the processor type (non-portable)

       -i, --hardware-platform
              print the hardware platform (non-portable)

       -o, --operating-system
              print the operating system




```