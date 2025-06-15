class ProxmoxTools(object):
    def __init__(self, proxmox):
        self.proxmox = proxmox

    def run(self, path, method='get', data={}):
        current = self.proxmox
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
