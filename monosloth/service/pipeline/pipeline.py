class Pipeline:

    def __init__(self):
        self.__pipes = []
        self.__method = 'handle'
        self.__resource = None

    def send(self, resource):
        """Prepare a resource to feed to each pipe.

        :param resource: The resource to prepare.

        :return: The pipeline instance.

        """
        self.__resource = resource

        return self

    def through(self, pipes):
        """Set pipe instances.

        provide the pipes with which to process the given resource.

        :param pipes: A list of pipe instances.

        :return: The pipeline instance.

        """
        self.__pipes = pipes

        return self

    def via(self, method):
        """Specify the method to invoke on each pipe.

        :param method: The method to invoke.

        :return: The pipeline instance.

        """
        self.__method = method

        return self

    def then(self, callback):
        """Run the pipline with the given callback.

        :param callback: The method to invoke on the result.

        :return: The result of the pipeline.

        """
        _next = self.__generate()

        return next(_next)(self.__resource, _next)

    def __generate(self):
        """Build a generator to traverse the pipe stack.

        :yield: The next pipe method to invoke.

        """
        for pipe in self.__pipes:
            yield getattr(resolve(pipe), self.__method)
