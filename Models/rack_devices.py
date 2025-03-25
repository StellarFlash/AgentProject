from abc import ABC, abstractmethod

class RackDevice(ABC):
    def __init__(self, device_id, device_type, port_layout=None, status='online'):
        self.device_id = device_id
        self.device_type = device_type
        self.port_layout = port_layout or []
        self.status = status
        self.ports = []
        
    def add_port(self, port):
        self.ports.append(port)
        
    def visualize_front_panel(self):
        """Generate ASCII visualization of device front panel showing port status"""
        panel = f"Device: {self.device_id} ({self.device_type})\n"
        panel += "=" * 20 + "\n"
        
        if not self.ports:
            panel += "No ports configured\n"
            return panel
            
        # Group ports by their position (if port_layout is specified)
        port_groups = {}
        for port in self.ports:
            pos = port.port_id.split('-')[0] if '-' in port.port_id else '1'
            port_groups.setdefault(pos, []).append(port)
        
        # Visualize each port group
        for pos, ports in port_groups.items():
            panel += f"Port Group {pos}: "
            for port in ports:
                panel += "O" if port.status == 'occupied' else "."
            panel += "\n"
            
        return panel

    @abstractmethod
    def get_device_info(self):
        pass

class NetworkDevice(RackDevice):
    def __init__(self, device_id, device_type, ip_address=None, management_port=None, **kwargs):
        super().__init__(device_id, device_type, **kwargs)
        self.ip_address = ip_address
        self.management_port = management_port
        
    def get_device_info(self):
        return f"Network Device: {self.device_type} (ID: {self.device_id})"

class Server(RackDevice):
    def __init__(self, device_id, device_type='server', status='online', **kwargs):
        super().__init__(device_id, device_type, **kwargs)
        self.status = status
        self.temperature = None
        self.humidity = None
        self.power_status = None
        
    def update_environment(self, temperature, humidity, power_status):
        self.temperature = temperature
        self.humidity = humidity
        self.power_status = power_status
        
    def get_device_info(self):
        return f"Server: {self.device_type} (ID: {self.device_id})"

class StorageDevice(RackDevice):
    def __init__(self, device_id, device_type='storage', **kwargs):
        super().__init__(device_id, device_type, **kwargs)
        
    def get_device_info(self):
        return f"Storage Device: {self.device_type} (ID: {self.device_id})"