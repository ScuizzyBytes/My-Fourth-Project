import ctypes


class BlockHeader(ctypes.Structure):   
    _fields_ = [("size", ctypes.c_uint32),("is_free", ctypes.c_bool)]
    
class Arena:
    def __init__(self, size= 1024):
        self.buffer = ctypes.create_string_buffer(size)
        
        header = BlockHeader.from_buffer(self.buffer, 0)
        header.size = 1016
        header.is_free = True
        
    def allocate(self, size):
        offset = 0
        while offset < len(self.buffer):
            header = BlockHeader.from_buffer(self.buffer, offset)
            if header.is_free and header.size >= size:
                header.is_free = False
                new_offset = offset + ctypes.sizeof(BlockHeader) + size
                new_header = BlockHeader.from_buffer(self.buffer, new_offset)
                new_header.size = header.size - size - ctypes.sizeof(BlockHeader)
                new_header.is_free = True
                return offset + ctypes.sizeof(BlockHeader)
        return None
