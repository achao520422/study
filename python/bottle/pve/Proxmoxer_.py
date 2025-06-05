from proxmoxer import ProxmoxAPI

proxmox = ProxmoxAPI(
    "192.168.34.8", user="root@pam", password="147258369", verify_ssl=False
)
# print(proxmox.nodes('com').qemu(100).agent.get())

def dynamic_proxmox_get(proxmox, base, path_parts):
    """
    :param proxmox: ProxmoxAPI 实例
    :param base: 初始入口，例如 proxmox.nodes('xxx')
    :param path_parts: list of str/int 表示后续路径
    :return: API 响应结果
    """
    api_call = base
    for part in path_parts:
        api_call = api_call(part)
    return api_call.get()

# result = dynamic_proxmox_get(
#     proxmox,
#     proxmox.nodes('com'),
#     [('qemu', 100), 'status', 'start']
# )
# print(result)
print(proxmox.nodes('com').qemu(100).status().start.get())