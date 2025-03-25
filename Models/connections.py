class Port:
    def __init__(self, port_id, port_type, port_model, speed):
        self.port_id = port_id
        self.port_type = port_type  # 'optical', 'electrical' or 'hybrid'
        self.port_model = port_model
        self.speed = speed  # in Gbps
        self.status = 'available'
        self.connected_to = None
        
    def connect(self, target_port):
        self.status = 'occupied'
        self.connected_to = target_port
        target_port.status = 'occupied'
        target_port.connected_to = self
        
    def disconnect(self):
        if self.connected_to:
            self.connected_to.status = 'available'
            self.connected_to.connected_to = None
            self.status = 'available'
            self.connected_to = None

class Cable(ABC):
    def __init__(self, cable_id, length, status='available'):
        self.cable_id = cable_id
        self.length = length  # in meters
        self.status = status
        self.connected_ports = []
        
    def connect(self, port1, port2):
        port1.connect(port2)
        self.connected_ports.extend([port1, port2])
        
    def disconnect(self):
        for port in self.connected_ports:
            port.disconnect()
        self.connected_ports = []
        
    @abstractmethod
    def get_cable_info(self):
        pass

def connect_devices_with_cable(device1, device2, cable, port_id1=None, port_id2=None):
    """
    Connect two devices using a cable through specified ports
    
    Args:
        device1: First device to connect
        device2: Second device to connect
        cable: Cable to use for connection
        port_id1: Optional port ID on device1 (uses first available if None)
        port_id2: Optional port ID on device2 (uses first available if None)
        
    Returns:
        Tuple of connected ports (port1, port2)
        
    Raises:
        ValueError: If ports are incompatible or unavailable
    """
    # Find ports to use
    port1 = next((p for p in device1.ports if (port_id1 is None or p.port_id == port_id1) and p.status == 'available'), None)
    port2 = next((p for p in device2.ports if (port_id2 is None or p.port_id == port_id2) and p.status == 'available'), None)
    
    if not port1 or not port2:
        raise ValueError("One or both specified ports are unavailable")
    
    # Validate port compatibility (simplified example)
    if port1.port_type != port2.port_type:
        raise ValueError(f"Port types mismatch: {port1.port_type} != {port2.port_type}")
    
    # Make connection
    cable.connect(port1, port2)
    return port1, port2

class TwistedPair(Cable):
    def __init__(self, cable_id, length, category, shielding=None, **kwargs):
        super().__init__(cable_id, length, **kwargs)
        self.category = category  # e.g. 'CAT5e', 'CAT6'
        self.shielding = shielding  # 'UTP', 'FTP', 'STP'
        
    def get_cable_info(self):
        return f"Twisted Pair: {self.category} ({'Shielded' if self.shielding else 'Unshielded'}), Length: {self.length}m"

class FiberOptic(Cable):
    def __init__(self, cable_id, length, core_type, connector_a, connector_b,
                 transceiver_a=None, transceiver_b=None, **kwargs):
        super().__init__(cable_id, length, **kwargs)
        self.core_type = core_type  # e.g. 'SMF', 'MMF'
        self.connector_a = connector_a  # e.g. 'LC', 'SC', 'FC'
        self.connector_b = connector_b
        self.transceiver_a = transceiver_a  # e.g. 'SFP+ 10G', 'QSFP28 100G'
        self.transceiver_b = transceiver_b
        
    def get_cable_info(self):
        info = f"Fiber Optic: {self.core_type}, Length: {self.length}m, "
        info += f"Connectors: {self.connector_a}/{self.connector_b}"
        if self.transceiver_a or self.transceiver_b:
            info += f", Transceivers: {self.transceiver_a or 'None'}/{self.transceiver_b or 'None'}"
        return info