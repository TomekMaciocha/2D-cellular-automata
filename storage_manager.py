import tempfile
import numpy as np
import os


class StorageManager:
    """This class is used for storage of simulation data before converting it into animations"""

    tempfiles = []
    """This list stores handles to the temporary files"""

    def write(self, state: list[list[int]]) -> None:
        """This method writes a list to a temporary text file and appends it to the 'tempfiles' list."""
        self.tempfiles.append(tempfile.mkstemp(suffix=".txt"))
        np.savetxt(self.tempfiles[-1][1], np.array(state), fmt="%d")

    def read(self, file_number: int) -> list[list[int]]:
        """This method reads a list from a temporary text file in the 'tempfiles' list."""
        return list(np.loadtxt(self.tempfiles[file_number][1]))

    def clear(self) -> None:
        """This method removes all temporary files' handles from the 'tempfiles' list and deletes all the corresponding temporary files."""
        for file in self.tempfiles:
            os.close(file[0])
            os.remove(file[1])

        self.tempfiles = []
