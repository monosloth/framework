from . import ClassSpecification


class Container:

    __resolved = {}

    def set_modules(self, modules):
        """Set class modules.

        :param modules: The class definition modules.

        """
        self.modules = modules

    def set_factory(self, factory):
        """Set factory instance.

        :param factory: An abstract factory instance.

        """
        self.factory = factory

    def resolve(self, clazz):
        """Resolve the given class to an instance.

        :param clazz: The class to resolve.

        :return: An instance where by the type is relative to the class.

        """
        if clazz not in self.__resolved:
            spec = ClassSpecification(clazz)
            self.__resolved[clazz] = spec
        else:
             spec = self.__resolved[clazz]

        conf = self.modules[spec.get_key()]

        return self.factory.get(conf, self.modules)
