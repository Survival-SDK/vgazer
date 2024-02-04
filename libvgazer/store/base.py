import os
import shutil

from libvgazer.exceptions import DirNameEngaged
from libvgazer.exceptions import FilenameEngaged

class StoreBase():
    def __init__(self, baseDirPath):
        self.baseDirPath = baseDirPath

    def GetDirectoryPath(self):
        return self.baseDirPath

    def GetSubdirectoryPath(self, subdirName):
        return os.path.join(self.baseDirPath, subdirName)

    def GetDirectoryFilePath(self, filename):
        return os.path.join(self.baseDirPath, filename)

    def GetSubdirectoryFilePath(self, subdirName, filename):
        return os.path.join(self.baseDirPath, subdirName, filename)

    def DirectoryExists(self):
        if os.path.exists(self.baseDirPath):
            if os.path.isdir(self.baseDirPath):
                return True
            else:
                raise DirNameEngaged(
                 "Name of directory for storing local settings are engaged "
                 "by file"
                )
        else:
            return False

    def SubdirectoryExists(self, subdirName):
        subdirPath = os.path.join(self.baseDirPath, subdirName)
        if os.path.exists(subdirPath):
            if os.path.isdir(subdirPath):
                return True
            else:
                raise DirNameEngaged(
                 "Name of directory " + subdirPath + " are engaged by file")
        else:
            return False

    def SubdirectoryFileExists(self, subdirName, filename):
        subdirFilePath = os.path.join(self.baseDirPath, subdirName, filename)
        if os.path.exists(subdirFilePath):
            if os.path.isfile(subdirFilePath):
                return True
            else:
                raise FilenameEngaged(
                 subdirFilePath + " is not a file and its filename are engaged"
                )
        else:
            return False

    def DirectoryFileExists(self, filename):
        filePath = os.path.join(self.baseDirPath, filename)
        if os.path.exists(filePath):
            if os.path.isfile(filePath):
                return True
            else:
                raise FilenameEngaged(
                 filePath + " is not a file and its filename are engaged")
        else:
            return False

    def ResolveDirectory(self):
        try:
            if not self.DirectoryExists():
                os.makedirs(self.baseDirPath)
            return True
        except self.DirNameEngaged:
            return False

    def ResolveSubdirectory(self, subdirName):
        self.ResolveDirectory()
        try:
            if not self.SubdirectoryExists(subdirName):
                subdirPath = os.path.join(self.baseDirPath, subdirName)
                os.makedirs(subdirPath)
            return True
        except DirNameEngaged:
            return False

    def ResolveEmptySubdirectory(self, subdirName):
        self.ResolveDirectory()
        try:
            if self.SubdirectoryExists(subdirName):
                self.RemoveSubdirectory(subdirName)
            subdirPath = os.path.join(self.baseDirPath, subdirName)
            os.makedirs(subdirPath)
            return True
        except DirNameEngaged:
            return False

    def ResolveDirectoryFile(self, subdirName, filename):
        self.ResolveDirectory()
        try:
            if not self.DirectoryFileExists(filename):
                filePath = os.path.join(self.baseDirPath, filename)
                open(filePath, "a").close()
            return True
        except FilenameEngaged:
            return False

    def ResolveSubdirectoryFile(self, subdirName, filename):
        self.ResolveDirectory()
        self.ResolveSubdirectory(subdirName)
        try:
            if not self.SubdirectoryFileExists(subdirName, filename):
                subdirFilePath = os.path.join(self.baseDirPath, subdirName,
                 filename)
                open(subdirFilePath, "a").close()
            return True
        except FilenameEngaged:
            return False

    def SubdirectoryFileIsEmpty(self, subdirName, filename):
        subdirFilePath = os.path.join(self.baseDirPath, subdirName, filename)
        if os.stat(subdirFilePath).st_size == 0:
            return True
        return False

    def SubdirectoryReadFile(self, subdirName, filename, mode):
        filepath = os.path.join(self.baseDirPath, subdirName, filename)
        fh = open(filepath, mode)
        data = fh.read()
        fh.close()
        return data

    def SubdirectoryReadTextFile(self, subdirName, filename):
        return self.SubdirectoryReadFile(subdirName, filename, "r")

    def SubdirectoryReadBinaryFile(self, subdirName, filename):
        return self.SubdirectoryReadFile(subdirName, filename, "rb")

    def SubdirectoryWriteFile(self, subdirName, filename, data, mode):
        filepath = os.path.join(self.baseDirPath, subdirName, filename)
        fh = open(filepath, mode)
        fh.write(data)
        fh.close()
        return data

    def SubdirectoryWriteTextFile(self, subdirName, filename, data):
        return self.SubdirectoryWriteFile(subdirName, filename, data, "w")

    def SubdirectoryWriteBinaryFile(self, subdirName, filename, data):
        return self.SubdirectoryWriteFile(subdirName, filename, data, "wb")

    def RemoveSubdirectory(self, subdirName):
        dirpath = os.path.join(self.baseDirPath, subdirName)
        shutil.rmtree(dirpath)

    def DirectoryReadTextFile(self, filename):
        return self.SubdirectoryReadTextFile(".", filename)

    def DirectoryReadBinaryFile(self, filename):
        return self.SubdirectoryReadBinaryFile(".", filename)

    def DirectoryWriteTextFile(self, filename, data):
        return self.SubdirectoryWriteTextFile(".", filename, data)

    def DirectoryWriteBinaryFile(self, filename, data):
        return self.SubdirectoryWriteBinaryFile(".", filename, data)
