
# Monosloth

A multi-purpose Python based application framework. It's purpose is to provide an application layout designed to scale quickly.

### INSTALLATION

To install monosloth simply,
```
pip3 install monosloth
```
or from source
```
python3 setup.py install
```

### GETTING STARTED

Use the starter repository with the necessary configs [here](https://github.com/monosloth/monosloth](https://github.com/monosloth/monosloth)). Alternatively, Initialise monosloth to have access to the dependency container; facades and decorator aliases. NOTE: If you choose not to use the starter application you will need to follow the steps listed under framework constructs.

```python
>>> from monosloth.bootstrap import *
```



### FRAMEWORK CONSTRUCTS

#### _Container_

The dependency container is config driven and resolves a class and it's dependencies based on the config provided within the `config/modules` directory, for example `./config/{module}.yaml` where `{module}` is any name you like. Each file within this directory is merged into a single dictionary which is used to resolve types.

Classes can be resolved with the `resolve()` method anywhere within the application. This method accepts a string which denotes the class specification key as shown below. This key consists of the class module, that is, the file it resides within and the inner most package name. This method also accepts a class from which it can derive it's module and class name to form the key.

```python
>>> resolve('foo.bar')
>>> resolve(FizzBuzz)
```
A class specification may look like the following:

_config/modules/thingy.yaml_

```yaml
foo.bar:
  module: my.package
  class: FizzBuzz
  dependencies:
    - my.thing
  methods:
    - init
    - set_thing:
      - thingy.thing
```

This specification defines a class within the `my.package` module and it's class is name `FizzBuzz`. The module or file it's in would be called `bar.py` and it's inner most package would be `foo`. This spec defines one dependency. Each dependency is resolved recursively and injected into the class during instantiation. Each spec may also list a set of methods of which can be used for setter injection or initialising classes.

The `app()` facade can be used to access the container instance where required.

```python
>>> app('container')
```

#### _Kernel_

The Kernel is responsible for bootstrapping the application by registering all of the applications providers. Providers are used to load and register properties used throughout the application. If you choose not to use the starter application you'll have to build the kernel config yourself.

_config/modules/app.yaml_

```yaml
kernel:
  module: monosloth
  class: Kernel
  dependencies:
    - provider.config
    - provider.decorator
    - provider.facade
```

The `app()` facade can be used to access the kernel instance if necessary.

```python
>>> app('kernel')
```

#### _Providers_

A Provider is a class injected as a dependency to the Kernel which is used to load or register some logic at run-time. The default necessary providers include config, decorator and facade. The configs are defined here and not in the framework itself so that their implementations can be overridden more easily, however the providers and their dependencies listed below need to be made available. Feel free to override and add additional providers, then register them within the kernel config.

_config/modules/provider.yaml_

```yaml
provider.config:
  module: monosloth.provider
  class: ConfigProvider

provider.decorator:
  module: monosloth.provider
  class: DecoratorProvider
  dependencies:
    - decorator.inject

provider.facade:
  module: monosloth.provider
  class: FacadeProvider
  dependencies:
    - facade.cache
    - facade.config
    - facade.resolve
    - facade.app
```

#### _Facades_

Facades provide an alias and helper logic to a given service. For some instances they serve simply as helper methods and are used to register the aforementioned `resolve` method. Though further usage should demonstrate a single interface to an array of sub-systems or services. The facades referenced above are defined as follows.

_config/modules/facade.yaml_

```yaml
facade.cache:
  module: monosloth.facade
  class: CacheFacade

facade.config:
  module: monosloth.facade
  class: ConfigFacade

facade.resolve:
  module: monosloth.facade
  class: ResolveFacade

facade.logger:
  module: monosloth.facade
  class: LoggerFacade

facade.app:
  module: monosloth.facade
  class: AppFacade

facade.event:
  module: monosloth.facade
  class: EventFacade

facade.register:
  module: monosloth.facade
  class: RegisterFacade
```



#### _Decorators_

Through the decorator provider aliases are registered to make globally use decorators available. These may include profiling tools. One decorator is provided by default and is used to inject dependencies at run-time.



_config/modules/decorator.yaml_

```yaml

decorator.inject:
  module: monosloth.decorator
  class: inject
```

#### _Singletons_

The class types are used throughout the framework. They are helpful for retaining data and for use with facades though choose carefully between their usage and the Borg pattern. The framework dependent singletons are listed below.



_config/modules/singleton.yaml_

```yaml
singleton.app:
  module: monosloth.singleton
  class: App

singleton.cache:
  module: monosloth.singleton
  class: Cache

singleton.config:
  module: monosloth.singleton
  class: Config

singleton.dispatcher:
  module: monosloth.singleton
  class: Dispatcher

singleton.event:
  module: monosloth.singleton
  class: Event
```



#### _Services_

Some services are injected as dependencies throughout the framework, feel free to override their behaviour but ensure they are provided.



_config/modules/service.yaml_

```yaml
parser.key:
  module: monosloth.service.parser
  class: KeyParser
```



#### _Events_

An event dispatcher is used to register and process events.

```python
>>> register(MyEvent, SomeRegister) # Register my listener
>>> event(MyEvent, [1, 2, 3]) # Invoke an event with the given payload
```

#### Database

The database driver and credentials can be defined with the environment file. The default driver is mysql.

#### Cache

The cache driver and credentials can be defined within the environment file. The default driver is redis.

```python
>>> cache('foo', 'bar') # Set cache property
>>> cache('foo') # Get cache property
```

Events are process

### REQUIREMENTS

- Python 3.7+

### DEPENDENCIES

- pyyaml

### DOCUMENTATION

[https://docs.monosloth.com](https://docs.monosloth.com/)

### AUTHOR

[admin@monosloth.com](mailto:admin@monosloth.com)
