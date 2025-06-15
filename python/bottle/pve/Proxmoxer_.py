import json

from proxmoxer import ProxmoxAPI
import time
proxmox = ProxmoxAPI(
    "192.168.34.8", user="root@pam", password="147258369", verify_ssl=False
)
def dynamic_path(path, method='get', data={}):
    current = proxmox
    for node in path:
        if type(node) is dict:

            for key, value in node.items():
                current = getattr(current, key)
                if callable(current):
                    current = current(value)
        else:
            current = getattr(current, node)
    if callable(current):
        return getattr(current, method)(**data)
def getInfo():
    info = dynamic_path([{'nodes': 'com'}, {'qemu': 100}, 'agent', 'network-get-interfaces'])
    for item in info['result']:
        for item2 in item['ip-addresses']:
            print(item2['ip-address-type'],item2['ip-address'])


def command(command='ls',options = '-a',path='/'):
    pid = dynamic_path([{'nodes': 'com'}, {'qemu': 100}, 'agent', 'exec'], method="post",
                                      data={'command': [f"/bin/{command}", f"{options}", f"{path}"]})['pid']
    while True:
        # 使用 dynamic_path 函数查询命令状态
        result = dynamic_path(
            path=[{'nodes': 'com'}, {'qemu': 100}, 'agent', 'exec-status'],
            method='get',
            data={'pid': pid}
        )

        if result.get('exited'):
            print("命令执行完成！")
            if 'out-data' in result:
                print("标准输出：", result['out-data'])
            else:
                print("无标准输出")

            if 'err-data' in result and result['err-data']:
                print("错误输出：", result['err-data'])
            else:
                print("无错误输出")

            print("退出码：", result['exitcode'])
            break
        else:
            print(f"命令仍在运行，等待... (PID: {pid})")

        # 等待一段时间再检查
        time.sleep(1)
# command()

# print(dynamic_path(path=[{'nodes':'com'},{'qemu':101}]))

print(proxmox.get_info())