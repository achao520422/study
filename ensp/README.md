# 路由信息协议（RIP）--->路由
```text
是内部网关协议中使用较为广泛的协议，它是一种分布式、基于距离向量的路由选择协议。

RIP将路由控制信息（30秒1次）向全网广播。如果没有收到路由控制信息，连接就会断开。
不过，这可能是丢包导致的，因此规定RIP等待5次。如果等了6次（180秒）仍未收到路由信息，才会真正关闭连接。

RIP基于距离向量算法决定路径。距离的单位为“跳数。跳数是指所经过路由的个数。RIP希望尽可能少的通过路由器将数据包转发到目标IP地址。

```
![rip toop 图](https://raw.githubusercontent.com/achao520422/study/refs/heads/main/ensp/image/rip.png)
```rip 配置过程
AR1:
rip <ripName>
version <version>
network 192.168.4.0
network 192.168.3.0
network 192.168.5.0

AR2:
rip <ripName>
version <version>
network 192.168.1.0
nwtwork 192.168.4.0

AR3:
rip <ripName>
version <version>
network 192.168.5.0
network 192.168.2.0
```
# stp 生成树协议 --->交换机
```text 什么是stp
是一种网络协议，旨在防止局域网（LAN）中出现环路。它通过在交换机之间传递特殊的消息（称为BPDU，桥协议数据单元），来发现并阻塞冗余路径，从而确保网络中只存在一条逻辑上的无环路径。这有助于避免广播风暴和MAC地址表不稳定等问题。

IEEE 802.1D是最初定义STP的标准，随着时间的发展，出现了RSTP（快速生成树协议，Rapid Spanning Tree Protocol）作为对原始STP的改进版本，提供了更快的收敛速度。之后还有MSTP（多实例生成树协议，Multiple Spanning Tree Protocol），允许在一个网络中运行多个生成树实例，每个实例可以关联一组VLAN，进一步优化了网络资源的利用。

STP的基本工作原理包括选举根桥（Root Bridge）、计算到根桥的最低成本路径、选择指定端口和非指定端口等步骤。端口状态有五种：Disabled、Blocking、Listening、Learning、Forwarding，不同状态下端口执行不同的操作以实现网络的自我调整和保护。
```

![stp 拓扑](https://raw.githubusercontent.com/achao520422/study/refs/heads/main/ensp/image/stp.png)
```stp 配置过程
1. 开启 stp
stp enable
2. 修改为 stp 模式(默认是mstp)
stp mode stp
3.查看 stp 信息
display stp brief
4. 修改桥的优先级（数值越小优先级越大）
stp priority 4096 （范围为 0-65535 且为 4096 的整数倍）
也可以 stp root primary   相当于 stp priority 0
```