class DataCenter:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.racks = []
        
    def add_rack(self, rack):
        self.racks.append(rack)

class Rack:
    def __init__(self, rack_id, location):
        self.rack_id = rack_id
        self.location = location
        self.devices = []
        
    def add_device(self, device):
        self.devices.append(device)
        
    def mount_device(self, device, position):
        """
        Mount a device to the rack at specified position with validation
        
        Args:
            device: The device object to mount
            position: The position in rack (U position)
            
        Raises:
            ValueError: If position is invalid or already occupied
        """
        # Validate position is available
        for existing_device in self.devices:
            if hasattr(existing_device, 'position') and existing_device.position == position:
                raise ValueError(f"Position {position} is already occupied")
                
        # Set device position and add to rack
        device.position = position
        self.add_device(device)