class CommandParser:

    def parse(self, args):
        arguments = [i for i in args if '-' not in i]
        options = self.__parse_options(args)

        return arguments, options

    def __parse_options(self, args):
        collection = [i for i in args if '-' in i]
        options = {}

        for option in collection:
            if '--' in option:
                if '=' in option:
                    parts = option.split('=')
                    options[parts[0][2:]] = parts[1]
                    continue
                options[option[2:]] = True
                continue
            options[option[1:]] = True
        return options
