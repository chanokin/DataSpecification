from data_allocation.abstract_data_writer import AbstractDataWriter

class FileDataWriter(AbstractDataWriter):
    
    def __init__(self, filename):
        """
        :param filename: The file to write to
        :type filename: str
        :raise data_allocation.exceptions.DataWriteException: If the file cannot
                    found or opened for writing
        """
    
    def write_bytes(self, data):
        """ See :py:meth:`data_allocation.abstract_data_writer.AbstractDataWriter.write_bytes`
        """
        # TODO
        pass
    
    def close(self):
        """ See :py:meth:`data_allocation.abstract_data_writer.AbstractDataWriter.close`
        """
        # TODO
        pass