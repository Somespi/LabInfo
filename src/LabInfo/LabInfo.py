
from types import ModuleType


class LabInfo:
    lib = None

    def __init__(self, library):
        """
        :param library: Library class from import and NOT String
        Upsetting the class to attach it with the class
        """
        if isinstance(library, ModuleType):
            self.lib = library
        else:
            raise OSError(f"{library} is not a module ")

    def fetch(self, mode):
        """
        :param mode: a string that has 3 cases.
        :return: a string that is satisfied with the case of the mode

        Learn More In The Official site
        """
        if mode == "docs":
            return self.lib.__doc__
        elif mode == "name":
            return self.lib.__name__
        elif mode == "location":
            if getattr(self.lib, '__file__', None):
                return self.lib.__file__
            raise TypeError('{0} is a built-in module'.format(self.lib))
        else: 
            raise SyntaxError(f"{mode} is not a true argument,\nThese are the true arguments:\ndocs\tname\tlocation")
