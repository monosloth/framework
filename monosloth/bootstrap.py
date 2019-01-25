from monosloth import Kernel
from monosloth.container import Container, ModuleLoader
from monosloth.factory import AbstractFactory
from monosloth.singleton import App
from monosloth.service.parser import KeyParser


factory = AbstractFactory()

container = Container()
container.set_modules(ModuleLoader().load())
container.set_factory(factory)

kernel = container.resolve(Kernel)
kernel.register()

application = container.resolve(App)
application.set_kernel(kernel)
application.set_container(container)
application.set_parser(container.resolve(KeyParser))
application.run()
