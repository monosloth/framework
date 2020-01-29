class OutputWriter:

    def set_colours(self, info, warning, error):
        self.__info = info
        self.__warning = warning
        self.__error = error

    def write(self, message, colour):
        print("\033[{}m{}\033[0m".format(colour, message))

    def info(self, message):
        self.write(message, self.__info)

    def warning(self, message):
        self.write(message, self.__warning)

    def error(self, message):
        self.write(message, self.__error)
