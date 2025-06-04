# 交换机远程登陆
![remote login toop](https://raw.githubusercontent.com/achao520422/study/refs/heads/main/ensp/image/%E8%BF%9C%E7%A8%8B%E7%99%BB%E9%99%86toop.png)

![cloud 01](https://raw.githubusercontent.com/achao520422/study/refs/heads/main/ensp/image/%E4%BA%91%E8%AE%BE%E5%A4%8701.png)

![remote login toop](https://raw.githubusercontent.com/achao520422/study/refs/heads/main/ensp/image/%E4%BA%91%E8%AE%BE%E5%A4%8702.png)

```配置
交换机远程登陆 aaa

1. 配置vlan ip
[Huawei]int vlan 1
[Huawei-Vlanif1]ip add 192.168.34.11 255.255.255.0

2. 配置接口
[Huawei]int e0/0/1
[Huawei-Ethernet0/0/1]port link-type access

3. 配置 aaa
[Huawei]aaa
[Huawei-aaa]local-user chaoarron password cipher 147258369  # 添加一个用户
[Huawei-aaa]local-user chaoarron service-type telnet # 设置用户登陆协议未telnet

4. 配置登陆
[Huawei]user-interface vty 0 4
[Huawei-ui-vty0-4]authentication-mode aaa
[Huawei-ui-vty0-4]user privilege level 15
[Huawei-ui-vty0-4]protocol inbound telnet

5. 开启 telnet （可选）
[Huawei]telnet server enable




telnet password 远程登陆


1. 配置vlan ip
[Huawei]int vlan 1
[Huawei-Vlanif1]ip add 192.168.34.11 255.255.255.0

2. 配置接口
[Huawei]int e0/0/1
[Huawei-Ethernet0/0/1]port link-type access

3. 配置 password 登陆
[Huawei]user-interface vty 0 4
[Huawei-ui-vty0-4]authentication-mode password
[Huawei-ui-vty0-4]set authentication password cipher 147258369
[Huawei-ui-vty0-4]user privilege level 15
```
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
# OSPF 内部网关协议 --->路由

```什么是ospf
OSPF（Open Shortest Path First，开放式最短路径优先）是一种用于互联网协议（IP）网络的内部网关协议（IGP），主要用于在单一自治系统（AS, Autonomous System）内决策路由。它是一个基于链路状态算法的路由协议，通过交换链路状态信息来构建网络拓扑图，并根据该拓扑计算出到达各个目的网络的最短路径树，从而确定最佳路由。

以下是OSPF的一些关键特点：

链路状态路由协议：与距离矢量协议不同，OSPF路由器之间交换的是链路状态公告（LSA, Link State Advertisement），这些信息描述了网络中的链路状态和成本，使得每个路由器可以构建一个完整的网络拓扑图。
分层结构：OSPF支持将网络划分为不同的区域（Area），包括一个主干区域（Area 0）和多个非主干区域。这种设计有助于简化大规模网络中的路由管理，同时减少路由更新对网络资源的消耗。
快速收敛：当网络拓扑发生变化时，OSPF能够迅速检测到变化并通过扩散过程通知整个网络，实现快速的路由收敛。
支持VLSM/CIDR：OSPF支持可变长子网掩码（VLSM）和无类别域间路由（CIDR），允许在同一网络中更灵活地分配IP地址空间。
认证机制：为了增强安全性，OSPF支持报文验证功能，可以配置简单密码或MD5认证来保护路由信息交换的安全性。
负载均衡：OSPF可以在多条等价路径上进行负载均衡，提高网络的利用率和可靠性。
总之，OSPF是一个强大而灵活的路由协议，适用于中大型网络，提供了高效、可靠的路由选择解决方案。
```
![ospf toop](https://raw.githubusercontent.com/achao520422/study/32fe5869cab601a3f6cab544b529190971f3bad1/ensp/image/ospf.png)
```配置流程
1. 配置 ospf 进程以及路由 Id
ospf 1 router-id 1.1.1.1
2. 配置 area
area 0 （0表示主干区域）
3. 配置 network ->直连网段
network 192.168.1.0 0.0.0.255 需要使用反掩码



AR1:
<Huawei>u t m
<Huawei>system-view
[Huawei]sys R1
[R1-ospf-1]int g0/0/0
[R1-GigabitEthernet0/0/0]ip address 10.10.3.1 24
[R1-GigabitEthernet0/0/0]int g0/0/1
[R1-GigabitEthernet0/0/1]ip address 10.10.2.2 24
[R1-GigabitEthernet0/0/1]q

# ospf配置
[R1]ospf 1 router-id 1.1.1.1
[R1-ospf-1]area 0
[R1-ospf-1-area-0.0.0.0]network 10.10.2.0 0.0.0.255
[R1-ospf-1-area-0.0.0.0]network 10.10.3.0 0.0.0.255




AR2：
<Huawei>u t m
Info: Current terminal monitor is off.
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]sys R2
[R2]int g0/0/0
[R2-GigabitEthernet0/0/0]ip add 10.10.3.2 24
[R2-GigabitEthernet0/0/0]int g0/0/1
[R2-GigabitEthernet0/0/1]ip add 10.10.4.1 24
[R2-GigabitEthernet0/0/1]q
[R2]ospf 1 router-id 2.2.2.2
[R2-ospf-1]area 0
[R2-ospf-1-area-0.0.0.0]network 10.10.3.0 0.0.0.255
[R2-ospf-1-area-0.0.0.0]network 10.10.4.0 0.0.0.255
[R2-ospf-1-area-0.0.0.0]


AR3既要配置主干网，也要配置边界网



AR3:
<Huawei>u t m
Info: Current terminal monitor is off.
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]sys R3
[R3]int g0/0/0
[R3-GigabitEthernet0/0/0]ip add 10.10.4.2 24
[R3-GigabitEthernet0/0/0]int g0/0/1
[R3-GigabitEthernet0/0/1]ip add 10.10.10.1 24
[R3-GigabitEthernet0/0/1]int g0/0/2
[R3-GigabitEthernet0/0/2]ip add 10.10.8.1 24
[R3-GigabitEthernet0/0/2]int g2/0/0
[R3-GigabitEthernet2/0/0]ip address 10.10.5.1 24
[R3-GigabitEthernet2/0/0]q

[R3]ospf 1 router-id 3.3.3.3
[R3-ospf-1]area 0
[R3-ospf-1-area-0.0.0.0]network 10.10.5.0 0.0.0.255
[R3-ospf-1-area-0.0.0.0]network 10.10.4.0 0.0.0.255



AR4:
<Huawei>u t m
[Huawei]sys R4
[R4]int g0/0/0
[R4-GigabitEthernet0/0/0]ip add 10.10.2.1 24
[R4-GigabitEthernet0/0/0]int g0/0/1
[R4-GigabitEthernet0/0/1]ip add 10.10.5.2 24
[R4-GigabitEthernet0/0/1]int g0/0/2
[R4-GigabitEthernet0/0/2]ip add 10.10.1.2 24
[R4-GigabitEthernet0/0/2]q

[R4]ospf 1 rou
[R4]ospf 1 router-id 4.4.4.4
[R4-ospf-1]area 0
[R4-ospf-1-area-0.0.0.0]network 10.10.2.0 0.0.0.255
[R4-ospf-1-area-0.0.0.0]network 10.10.5.0 0.0.0.255
[R4-ospf-1-area-0.0.0.0]network 10.10.1.0 0.0.0.255
[R4-ospf-1-area-0.0.0.0]q



AR5:

<Huawei>u t m
Info: Current terminal monitor is off.
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]sys R5
[R5]int g0/0/0
[R5-GigabitEthernet0/0/0]ip add 10.10.6.2 24
[R5-GigabitEthernet0/0/0]int g0/0/1
[R5-GigabitEthernet0/0/1]ip add 10.10.9.1 24
[R5-GigabitEthernet0/0/1]q
[R5]ospf 1 router-id 5.5.5.5
[R5-ospf-1]area 1
[R5-ospf-1-area-0.0.0.1]network 10.10.6.0 0.0.0.255
[R5-ospf-1-area-0.0.0.1]network 10.10.9.0 0.0.0.255


AR6:
<Huawei>u t m
Info: Current terminal monitor is off.
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]sys R6
[R6]int g0/0/0
[R6-GigabitEthernet0/0/0]ip add 10.10.9.2 24
[R6-GigabitEthernet0/0/0]int g0/0/1
[R6-GigabitEthernet0/0/1]ip add 10.10.8.2 24
[R6-GigabitEthernet0/0/1]int g0/0/2
[R6-GigabitEthernet0/0/2]ip add 10.10.10.2 24
[R6-GigabitEthernet0/0/2]q




[R6]ospf 1 router-id 6.6.6.6
[R6-ospf-1]area 1
[R6-ospf-1-area-0.0.0.1]network 10.10.9.0 0.0.0.255
[R6-ospf-1-area-0.0.0.1]network 10.10.8.1 0.0.0.255
[R6-ospf-1-area-0.0.0.1]network 10.10.10.0 0.0.0.255
[R6-ospf-1-area-0.0.0.1]q

```



# BGP 边界网关协议 ---> 路由
```什么是边界网关协议
BGP（Border Gateway Protocol）是一种路径矢量路由协议，用于在不同的自治系统（AS）间交换路由信息，并决定数据传输的最佳路径。
```

![bgp toop](https://raw.githubusercontent.com/achao520422/study/refs/heads/main/ensp/image/BGP.png)

```配置流程
AR6:
<Huawei>u t m
<Huawei>sys
[Huawei]int g0/0/0
[Huawei-GigabitEthernet0/0/0]ip add 10.10.1.1 24
[Huawei]int g0/0/1
[Huawei-GigabitEthernet0/0/1]ip add 192.168.1.254 24
[Huawei-GigabitEthernet0/0/1]q
[Huawei]bgp 100
[Huawei-bgp]peer 10.10.1.2 as-number 200
[Huawei-bgp]import-route direct



Ar7:
<Huawei>u t m
<Huawei>sys
[Huawei]int g0/0/0
[Huawei-GigabitEthernet0/0/0]ip add 10.10.1.2 24
[Huawei]int g0/0/1
[Huawei-GigabitEthernet0/0/1]ip add 10.10.2.1 24
[Huawei-GigabitEthernet0/0/1]q
[Huawei]bgp 200
[Huawei-bgp]peer 10.10.1.1 as-number 100 # 添加邻居 bgp
[Huawei-bgp]import-route ospf  #为了将ws内部的ospf分享给bgp学习

[Huawei-bgp]q
[Huawei]ospf 1
[Huawei-ospf-1]area 0
[Huawei-ospf-1-area-0.0.0.0]network 10.10.2.0 0.0.0.255
[Huawei-ospf-1-area-0.0.0.0]import-route bgp #将 bpg 的路由表给 ospf 学习




AR8:
<Huawei>u t m
<Huawei>sys
[Huawei]int g0/0/0
[Huawei-GigabitEthernet0/0/0]ip add 10.10.2.2 24
[Huawei]int g0/0/1
[Huawei-GigabitEthernet0/0/1]ip add 10.10.3.1 24
[Huawei-GigabitEthernet0/0/1]q
[Huawei]ospf 1
[Huawei-ospf-1]area 0
[Huawei-ospf-1-area-0.0.0.0]network 10.10.2.0 0.0.0.255
[Huawei-ospf-1-area-0.0.0.0]network 10.10.3.0 0.0.0.255



Ar9:
<Huawei>u t m
<Huawei>sys
[Huawei]int g0/0/0
[Huawei-GigabitEthernet0/0/0]ip add 10.10.3.2 24
[Huawei]int g0/0/1
[Huawei-GigabitEthernet0/0/1]ip add 10.10.4.1 24
[Huawei-GigabitEthernet0/0/1]q
[Huawei]bgp 200
[Huawei-bgp]peer 10.10.4.2 as-number 300
[Huawei-bgp]import-route ospf  #为了将ws内部的ospf分享给bgp学习

[Huawei-bgp]q
[Huawei]ospf 1
[Huawei-ospf-1]area 0
[Huawei-ospf-1-area-0.0.0.0]network 10.10.3.0 0.0.0.255
[Huawei-ospf-1-area-0.0.0.0]import-route bgp #将 bpg 的路由表给 ospf 学习




AR10：
<Huawei>u t m
<Huawei>sys
[Huawei]int g0/0/0
[Huawei-GigabitEthernet0/0/0]ip add 10.10.4.2 24
[Huawei]int g0/0/1
[Huawei-GigabitEthernet0/0/1]ip add 192.168.2.254 24
[Huawei-GigabitEthernet0/0/1]q
[Huawei]bgp 300
[Huawei-bgp]peer 10.10.1.2 as-number 200
[Huawei-bgp]import-route direct
```

```难点
bgp 之间默认不会自动相互学习路由表，需要使用 import-route 命令去指定学习,如果是 bgp 直连则使用 import-route direct,上述例子中我使用的是bgp 学习 ospf 的路由表，即 import-route ospf ,当然 ospf 与 bgp 之间页不能相互学习路由表,需要在 ospf 中配置 import-route bgp 。
```