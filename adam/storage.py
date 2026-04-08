from django.core.files.storage import FileSystemStorage

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        """Return filename that's available, overwrite if exists"""
        if self.exists(name):
            self.delete(name)
        return name