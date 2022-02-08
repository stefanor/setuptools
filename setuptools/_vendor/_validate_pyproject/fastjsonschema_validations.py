# noqa
# type: ignore
# flake8: noqa
# pylint: skip-file
# mypy: ignore-errors
# yapf: disable
# pylama:skip=1


# *** PLEASE DO NOT MODIFY DIRECTLY: Automatically generated code *** 


VERSION = "2.15.3"
import re
from .fastjsonschema_exceptions import JsonSchemaValueException


REGEX_PATTERNS = {
    '^.*$': re.compile('^.*$'),
    '.+': re.compile('.+'),
    '^.+$': re.compile('^.+$'),
    'idn-email_re_pattern': re.compile('^[^@]+@[^@]+\\.[^@]+\\Z')
}

NoneType = type(None)

def validate(data, custom_formats={}):
    validate_https___www_python_org_dev_peps_pep_0517(data, custom_formats)
    return data

def validate_https___www_python_org_dev_peps_pep_0517(data, custom_formats={}):
    if not isinstance(data, (dict)):
        raise JsonSchemaValueException("data must be object", value=data, name="data", definition={'$schema': 'http://json-schema.org/draft-07/schema', '$id': 'https://www.python.org/dev/peps/pep-0517/', 'title': 'Data structure for ``pyproject.toml`` files', '$$description': [':pep:`517` defines a build-system independent format for source trees', 'while :pep:`518` provides a way of specifying the minimum system requirements', 'for Python projects.', 'Please notice the ``project`` table (as defined in  :pep:`621`) is not included', 'in this schema and should be considered separately.'], 'type': 'object', 'additionalProperties': False, 'properties': {'build-system': {'type': 'object', 'description': 'Table used to store build-related data', 'additionalProperties': False, 'properties': {'requires': {'type': 'array', '$$description': ['List of dependencies in the :pep:`508` format required to execute the build', 'system. Please notice that the resulting dependency graph', '**MUST NOT contain cycles**'], 'items': {'type': 'string'}}, 'build-backend': {'type': 'string', 'description': 'Python object that will be used to perform the build according to :pep:`517`', 'format': 'pep517-backend-reference'}, 'backend-path': {'type': 'array', '$$description': ['List of directories to be prepended to ``sys.path`` when loading the', 'back-end, and running its hooks'], 'items': {'type': 'string', '$comment': 'Should be a path (TODO: enforce it with format?)'}}}, 'required': ['requires']}, 'project': {'$ref': 'https://www.python.org/dev/peps/pep-0621/'}, 'tool': {'type': 'object', 'properties': {'distutils': {'$ref': 'https://docs.python.org/3/install/'}, 'setuptools': {'$ref': 'https://setuptools.pypa.io/en/latest/references/keywords.html'}}}}, 'project': {'$ref': 'https://www.python.org/dev/peps/pep-0621/'}}, rule='type')
    data_is_dict = isinstance(data, dict)
    if data_is_dict:
        data_keys = set(data.keys())
        if "build-system" in data_keys:
            data_keys.remove("build-system")
            data__buildsystem = data["build-system"]
            if not isinstance(data__buildsystem, (dict)):
                raise JsonSchemaValueException("data.build-system must be object", value=data__buildsystem, name="data.build-system", definition={'type': 'object', 'description': 'Table used to store build-related data', 'additionalProperties': False, 'properties': {'requires': {'type': 'array', '$$description': ['List of dependencies in the :pep:`508` format required to execute the build', 'system. Please notice that the resulting dependency graph', '**MUST NOT contain cycles**'], 'items': {'type': 'string'}}, 'build-backend': {'type': 'string', 'description': 'Python object that will be used to perform the build according to :pep:`517`', 'format': 'pep517-backend-reference'}, 'backend-path': {'type': 'array', '$$description': ['List of directories to be prepended to ``sys.path`` when loading the', 'back-end, and running its hooks'], 'items': {'type': 'string', '$comment': 'Should be a path (TODO: enforce it with format?)'}}}, 'required': ['requires']}, rule='type')
            data__buildsystem_is_dict = isinstance(data__buildsystem, dict)
            if data__buildsystem_is_dict:
                data__buildsystem_len = len(data__buildsystem)
                if not all(prop in data__buildsystem for prop in ['requires']):
                    raise JsonSchemaValueException("data.build-system must contain ['requires'] properties", value=data__buildsystem, name="data.build-system", definition={'type': 'object', 'description': 'Table used to store build-related data', 'additionalProperties': False, 'properties': {'requires': {'type': 'array', '$$description': ['List of dependencies in the :pep:`508` format required to execute the build', 'system. Please notice that the resulting dependency graph', '**MUST NOT contain cycles**'], 'items': {'type': 'string'}}, 'build-backend': {'type': 'string', 'description': 'Python object that will be used to perform the build according to :pep:`517`', 'format': 'pep517-backend-reference'}, 'backend-path': {'type': 'array', '$$description': ['List of directories to be prepended to ``sys.path`` when loading the', 'back-end, and running its hooks'], 'items': {'type': 'string', '$comment': 'Should be a path (TODO: enforce it with format?)'}}}, 'required': ['requires']}, rule='required')
                data__buildsystem_keys = set(data__buildsystem.keys())
                if "requires" in data__buildsystem_keys:
                    data__buildsystem_keys.remove("requires")
                    data__buildsystem__requires = data__buildsystem["requires"]
                    if not isinstance(data__buildsystem__requires, (list, tuple)):
                        raise JsonSchemaValueException("data.build-system.requires must be array", value=data__buildsystem__requires, name="data.build-system.requires", definition={'type': 'array', '$$description': ['List of dependencies in the :pep:`508` format required to execute the build', 'system. Please notice that the resulting dependency graph', '**MUST NOT contain cycles**'], 'items': {'type': 'string'}}, rule='type')
                    data__buildsystem__requires_is_list = isinstance(data__buildsystem__requires, (list, tuple))
                    if data__buildsystem__requires_is_list:
                        data__buildsystem__requires_len = len(data__buildsystem__requires)
                        for data__buildsystem__requires_x, data__buildsystem__requires_item in enumerate(data__buildsystem__requires):
                            if not isinstance(data__buildsystem__requires_item, (str)):
                                raise JsonSchemaValueException(""+"data.build-system.requires[{data__buildsystem__requires_x}]".format(**locals())+" must be string", value=data__buildsystem__requires_item, name=""+"data.build-system.requires[{data__buildsystem__requires_x}]".format(**locals())+"", definition={'type': 'string'}, rule='type')
                if "build-backend" in data__buildsystem_keys:
                    data__buildsystem_keys.remove("build-backend")
                    data__buildsystem__buildbackend = data__buildsystem["build-backend"]
                    if not isinstance(data__buildsystem__buildbackend, (str)):
                        raise JsonSchemaValueException("data.build-system.build-backend must be string", value=data__buildsystem__buildbackend, name="data.build-system.build-backend", definition={'type': 'string', 'description': 'Python object that will be used to perform the build according to :pep:`517`', 'format': 'pep517-backend-reference'}, rule='type')
                    if isinstance(data__buildsystem__buildbackend, str):
                        if not custom_formats["pep517-backend-reference"](data__buildsystem__buildbackend):
                            raise JsonSchemaValueException("data.build-system.build-backend must be pep517-backend-reference", value=data__buildsystem__buildbackend, name="data.build-system.build-backend", definition={'type': 'string', 'description': 'Python object that will be used to perform the build according to :pep:`517`', 'format': 'pep517-backend-reference'}, rule='format')
                if "backend-path" in data__buildsystem_keys:
                    data__buildsystem_keys.remove("backend-path")
                    data__buildsystem__backendpath = data__buildsystem["backend-path"]
                    if not isinstance(data__buildsystem__backendpath, (list, tuple)):
                        raise JsonSchemaValueException("data.build-system.backend-path must be array", value=data__buildsystem__backendpath, name="data.build-system.backend-path", definition={'type': 'array', '$$description': ['List of directories to be prepended to ``sys.path`` when loading the', 'back-end, and running its hooks'], 'items': {'type': 'string', '$comment': 'Should be a path (TODO: enforce it with format?)'}}, rule='type')
                    data__buildsystem__backendpath_is_list = isinstance(data__buildsystem__backendpath, (list, tuple))
                    if data__buildsystem__backendpath_is_list:
                        data__buildsystem__backendpath_len = len(data__buildsystem__backendpath)
                        for data__buildsystem__backendpath_x, data__buildsystem__backendpath_item in enumerate(data__buildsystem__backendpath):
                            if not isinstance(data__buildsystem__backendpath_item, (str)):
                                raise JsonSchemaValueException(""+"data.build-system.backend-path[{data__buildsystem__backendpath_x}]".format(**locals())+" must be string", value=data__buildsystem__backendpath_item, name=""+"data.build-system.backend-path[{data__buildsystem__backendpath_x}]".format(**locals())+"", definition={'type': 'string', '$comment': 'Should be a path (TODO: enforce it with format?)'}, rule='type')
                if data__buildsystem_keys:
                    raise JsonSchemaValueException("data.build-system must not contain "+str(data__buildsystem_keys)+" properties", value=data__buildsystem, name="data.build-system", definition={'type': 'object', 'description': 'Table used to store build-related data', 'additionalProperties': False, 'properties': {'requires': {'type': 'array', '$$description': ['List of dependencies in the :pep:`508` format required to execute the build', 'system. Please notice that the resulting dependency graph', '**MUST NOT contain cycles**'], 'items': {'type': 'string'}}, 'build-backend': {'type': 'string', 'description': 'Python object that will be used to perform the build according to :pep:`517`', 'format': 'pep517-backend-reference'}, 'backend-path': {'type': 'array', '$$description': ['List of directories to be prepended to ``sys.path`` when loading the', 'back-end, and running its hooks'], 'items': {'type': 'string', '$comment': 'Should be a path (TODO: enforce it with format?)'}}}, 'required': ['requires']}, rule='additionalProperties')
        if "project" in data_keys:
            data_keys.remove("project")
            data__project = data["project"]
            validate_https___www_python_org_dev_peps_pep_0621(data__project, custom_formats)
        if "tool" in data_keys:
            data_keys.remove("tool")
            data__tool = data["tool"]
            if not isinstance(data__tool, (dict)):
                raise JsonSchemaValueException("data.tool must be object", value=data__tool, name="data.tool", definition={'type': 'object', 'properties': {'distutils': {'$ref': 'https://docs.python.org/3/install/'}, 'setuptools': {'$ref': 'https://setuptools.pypa.io/en/latest/references/keywords.html'}}}, rule='type')
            data__tool_is_dict = isinstance(data__tool, dict)
            if data__tool_is_dict:
                data__tool_keys = set(data__tool.keys())
                if "distutils" in data__tool_keys:
                    data__tool_keys.remove("distutils")
                    data__tool__distutils = data__tool["distutils"]
                    validate_https___docs_python_org_3_install(data__tool__distutils, custom_formats)
                if "setuptools" in data__tool_keys:
                    data__tool_keys.remove("setuptools")
                    data__tool__setuptools = data__tool["setuptools"]
                    validate_https___setuptools_pypa_io_en_latest_references_keywords_html(data__tool__setuptools, custom_formats)
        if data_keys:
            raise JsonSchemaValueException("data must not contain "+str(data_keys)+" properties", value=data, name="data", definition={'$schema': 'http://json-schema.org/draft-07/schema', '$id': 'https://www.python.org/dev/peps/pep-0517/', 'title': 'Data structure for ``pyproject.toml`` files', '$$description': [':pep:`517` defines a build-system independent format for source trees', 'while :pep:`518` provides a way of specifying the minimum system requirements', 'for Python projects.', 'Please notice the ``project`` table (as defined in  :pep:`621`) is not included', 'in this schema and should be considered separately.'], 'type': 'object', 'additionalProperties': False, 'properties': {'build-system': {'type': 'object', 'description': 'Table used to store build-related data', 'additionalProperties': False, 'properties': {'requires': {'type': 'array', '$$description': ['List of dependencies in the :pep:`508` format required to execute the build', 'system. Please notice that the resulting dependency graph', '**MUST NOT contain cycles**'], 'items': {'type': 'string'}}, 'build-backend': {'type': 'string', 'description': 'Python object that will be used to perform the build according to :pep:`517`', 'format': 'pep517-backend-reference'}, 'backend-path': {'type': 'array', '$$description': ['List of directories to be prepended to ``sys.path`` when loading the', 'back-end, and running its hooks'], 'items': {'type': 'string', '$comment': 'Should be a path (TODO: enforce it with format?)'}}}, 'required': ['requires']}, 'project': {'$ref': 'https://www.python.org/dev/peps/pep-0621/'}, 'tool': {'type': 'object', 'properties': {'distutils': {'$ref': 'https://docs.python.org/3/install/'}, 'setuptools': {'$ref': 'https://setuptools.pypa.io/en/latest/references/keywords.html'}}}}, 'project': {'$ref': 'https://www.python.org/dev/peps/pep-0621/'}}, rule='additionalProperties')
    return data

def validate_https___setuptools_pypa_io_en_latest_references_keywords_html(data, custom_formats={}):
    if not isinstance(data, (dict)):
        raise JsonSchemaValueException("data must be object", value=data, name="data", definition={'$schema': 'http://json-schema.org/draft-07/schema', '$id': 'https://setuptools.pypa.io/en/latest/references/keywords.html', 'title': '``tool.setuptools`` table', '$$description': ['Please notice for the time being the ``setuptools`` project does not specify', 'a way of configuring builds via ``pyproject.toml``.', 'Therefore this schema should be taken just as a *"thought experiment"* on how', 'this *might be done*, by following the principles established in', '`ini2toml <https://ini2toml.readthedocs.io/en/latest/setuptools_pep621.html>`_.', 'It considers only ``setuptools`` `parameters', '<https://setuptools.pypa.io/en/latest/userguide/declarative_config.html>`_', 'that can currently be configured via ``setup.cfg`` and are not covered by :pep:`621`', 'but intentionally excludes ``dependency_links`` and ``setup_requires``.', 'NOTE: ``scripts`` was renamed to ``script-files`` to avoid confusion with', 'entry-point based scripts (defined in :pep:`621`).'], 'type': 'object', 'additionalProperties': False, 'properties': {'platforms': {'type': 'array', 'items': {'type': 'string'}}, 'provides': {'$$description': ['Package and virtual package names contained within this package', '**(not supported by pip)**'], 'type': 'array', 'items': {'type': 'string', 'format': 'pep508-identifier'}}, 'obsoletes': {'$$description': ['Packages which this package renders obsolete', '**(not supported by pip)**'], 'type': 'array', 'items': {'type': 'string', 'format': 'pep508-identifier'}}, 'zip-safe': {'description': 'Whether the project can be safely installed and run from a zip file.', 'type': 'boolean'}, 'script-files': {'description': 'Legacy way of defining scripts (entry-points are preferred).', 'type': 'array', 'items': {'type': 'string'}, '$comment': 'TODO: is this field deprecated/should be removed?'}, 'eager-resources': {'$$description': ['Resources that should be extracted together, if any of them is needed,', 'or if any C extensions included in the project are imported.'], 'type': 'array', 'items': {'type': 'string'}}, 'packages': {'$$description': ['Packages that should be included in the distribution.', 'It can be given either as a list of package identifiers', 'or as a ``dict``-like structure with a single key ``find``', 'which corresponds to a dynamic call to', '``setuptools.config.expand.find_packages`` function.', 'The ``find`` key is associated with a nested ``dict``-like structure that can', 'contain ``where``, ``include``, ``exclude`` and ``namespaces`` keys,', 'mimicking the keyword arguments of the associated function.'], 'oneOf': [{'title': 'Array of Python package identifiers', 'type': 'array', 'items': {'type': 'string', 'format': 'python-module-name'}}, {'$ref': '#/definitions/find-directive'}]}, 'package-dir': {'$$description': [':class:`dict`-like structure mapping from package names to directories where their', 'code can be found.', 'The empty string (as key) means that all packages are contained inside', 'the given directory will be included in the distribution.'], 'type': 'object', 'additionalProperties': False, 'propertyNames': {'oneOf': [{'format': 'python-module-name'}, {'const': ''}]}, 'patternProperties': {'^.*$': {'type': 'string'}}}, 'package-data': {'$$description': ['Mapping from package names to lists of glob patterns.', 'Usually this option is not needed when using ``include-package-data = true``', 'For more information on how to include data files, check ``setuptools`` `docs', '<https://setuptools.pypa.io/en/latest/userguide/datafiles.html>`_.'], 'type': 'object', 'additionalProperties': False, 'propertyNames': {'oneOf': [{'format': 'python-module-name'}, {'const': '*'}]}, 'patternProperties': {'^.*$': {'type': 'array', 'items': {'type': 'string'}}}}, 'include-package-data': {'$$description': ['Automatically include any data files inside the package directories', 'that are specified by ``MANIFEST.in``', 'For more information on how to include data files, check ``setuptools`` `docs', '<https://setuptools.pypa.io/en/latest/userguide/datafiles.html>`_.'], 'type': 'boolean'}, 'exclude-package-data': {'$$description': ['Mapping from package names to lists of glob patterns that should be excluded', 'For more information on how to include data files, check ``setuptools`` `docs', '<https://setuptools.pypa.io/en/latest/userguide/datafiles.html>`_.'], 'type': 'object', 'additionalProperties': False, 'propertyNames': {'oneOf': [{'format': 'python-module-name'}, {'const': '*'}]}, 'patternProperties': {'^.*$': {'type': 'array', 'items': {'type': 'string'}}}}, 'namespace-packages': {'type': 'array', 'items': {'type': 'string', 'format': 'python-module-name'}, '$comment': 'https://setuptools.pypa.io/en/latest/userguide/package_discovery.html'}, 'py-modules': {'description': 'Modules that setuptools will manipulate', 'type': 'array', 'items': {'type': 'string', 'format': 'python-module-name'}, '$comment': 'TODO: clarify the relationship with ``packages``'}, 'data-files': {'$$description': ['**DEPRECATED**: dict-like structure where each key represents a directory and', 'the value is a list of glob patterns that should be installed in them.', "Please notice this don't work with wheels. See `data files support", '<https://setuptools.pypa.io/en/latest/userguide/datafiles.html>`_'], 'type': 'object', 'patternProperties': {'^.*$': {'type': 'array', 'items': {'type': 'string'}}}}, 'cmdclass': {'$$description': ['Mapping of distutils-style command names to ``setuptools.Command`` subclasses', 'which in turn should be represented by strings with a qualified class name', '(i.e., "dotted" form with module), e.g.::\n\n', '    cmdclass = {mycmd = "pkg.subpkg.module.CommandClass"}\n\n', 'The command class should be a directly defined at the top-level of the', 'containing module (no class nesting).'], 'type': 'object', 'patternProperties': {'^.*$': {'type': 'string', 'format': 'python-qualified-identifier'}}}, 'dynamic': {'type': 'object', 'description': 'Instructions for loading :pep:`621`-related metadata dynamically', 'properties': {'version': {'$$description': ['A version dynamically loaded via either the ``attr:`` or ``file:``', 'directives. Please make sure the given file or attribute respects :pep:`440`.'], 'oneOf': [{'$ref': '#/definitions/attr-directive'}, {'$ref': '#/definitions/file-directive'}]}, 'classifiers': {'$ref': '#/definitions/file-directive'}, 'description': {'$ref': '#/definitions/file-directive'}, 'entry-points': {'$ref': '#/definitions/file-directive'}, 'readme': {'anyOf': [{'$ref': '#/definitions/file-directive'}, {'properties': {'content-type': {'type': 'string'}}}], 'required': ['file']}, 'license': {'type': 'string', '$$description': ['PROVISIONAL: A string specifying the license of the package', '(might change with PEP 639)'], '$comment': 'TODO: revise if PEP 639 is accepted. Maybe ``license-expression``?'}, 'license-files': {'type': 'array', 'items': {'type': 'string'}, '$$description': ['PROVISIONAL: List of glob patterns for all license files being distributed.', '(might change with PEP 639)'], 'default': ['LICEN[CS]E*', ' COPYING*', ' NOTICE*', 'AUTHORS*'], '$comment': 'TODO: revise if PEP 639 is accepted. Maybe ``license-files.glob``?'}}}}, 'definitions': {'file-directive': {'$id': '#/definitions/file-directive', 'title': "'file:' directive", 'description': 'Value is read from a file (or list of files and then concatenated)', 'type': 'object', 'additionalProperties': False, 'properties': {'file': {'oneOf': [{'type': 'string'}, {'type': 'array', 'items': {'type': 'string'}}]}}, 'required': ['file']}, 'attr-directive': {'title': "'attr:' directive", '$id': '#/definitions/attr-directive', '$$description': ['Value is read from a module attribute. Supports callables and iterables;', 'unsupported types are cast via ``str()``'], 'type': 'object', 'additionalProperties': False, 'properties': {'attr': {'type': 'string'}}, 'required': ['attr']}, 'find-directive': {'$id': '#/definitions/find-directive', 'title': "'find:' directive", 'type': 'object', 'additionalProperties': False, 'properties': {'find': {'type': 'object', '$$description': ['Dynamic `package discovery', '<https://setuptools.pypa.io/en/latest/userguide/package_discovery.html>`_.'], 'additionalProperties': False, 'properties': {'where': {'description': 'Directories to be searched for packages (Unix-style relative path)', 'type': 'array', 'items': {'type': 'string'}}, 'exclude': {'type': 'array', '$$description': ['Exclude packages that match the values listed in this field.', "Can container shell-style wildcards (e.g. ``'pkg.*'``)"], 'items': {'type': 'string'}}, 'include': {'type': 'array', '$$description': ['Restrict the found packages to just the ones listed in this field.', "Can container shell-style wildcards (e.g. ``'pkg.*'``)"], 'items': {'type': 'string'}}, 'namespaces': {'type': 'boolean', '$$description': ['When ``True``, directories without a ``__init__.py`` file will also', 'be scanned for :pep:`420`-style implicit namespaces']}}}}}}}, rule='type')
    data_is_dict = isinstance(data, dict)
    if data_is_dict:
        data_keys = set(data.keys())
        if "platforms" in data_keys:
            data_keys.remove("platforms")
            data__platforms = data["platforms"]
            if not isinstance(data__platforms, (list, tuple)):
                raise JsonSchemaValueException("data.platforms must be array", value=data__platforms, name="data.platforms", definition={'type': 'array', 'items': {'type': 'string'}}, rule='type')
            data__platforms_is_list = isinstance(data__platforms, (list, tuple))
            if data__platforms_is_list:
                data__platforms_len = len(data__platforms)
                for data__platforms_x, data__platforms_item in enumerate(data__platforms):
                    if not isinstance(data__platforms_item, (str)):
                        raise JsonSchemaValueException(""+"data.platforms[{data__platforms_x}]".format(**locals())+" must be string", value=data__platforms_item, name=""+"data.platforms[{data__platforms_x}]".format(**locals())+"", definition={'type': 'string'}, rule='type')
        if "provides" in data_keys:
            data_keys.remove("provides")
            data__provides = data["provides"]
            if not isinstance(data__provides, (list, tuple)):
                raise JsonSchemaValueException("data.provides must be array", value=data__provides, name="data.provides", definition={'$$description': ['Package and virtual package names contained within this package', '**(not supported by pip)**'], 'type': 'array', 'items': {'type': 'string', 'format': 'pep508-identifier'}}, rule='type')
            data__provides_is_list = isinstance(data__provides, (list, tuple))
            if data__provides_is_list:
                data__provides_len = len(data__provides)
                for data__provides_x, data__provides_item in enumerate(data__provides):
                    if not isinstance(data__provides_item, (str)):
                        raise JsonSchemaValueException(""+"data.provides[{data__provides_x}]".format(**locals())+" must be string", value=data__provides_item, name=""+"data.provides[{data__provides_x}]".format(**locals())+"", definition={'type': 'string', 'format': 'pep508-identifier'}, rule='type')
                    if isinstance(data__provides_item, str):
                        if not custom_formats["pep508-identifier"](data__provides_item):
                            raise JsonSchemaValueException(""+"data.provides[{data__provides_x}]".format(**locals())+" must be pep508-identifier", value=data__provides_item, name=""+"data.provides[{data__provides_x}]".format(**locals())+"", definition={'type': 'string', 'format': 'pep508-identifier'}, rule='format')
        if "obsoletes" in data_keys:
            data_keys.remove("obsoletes")
            data__obsoletes = data["obsoletes"]
            if not isinstance(data__obsoletes, (list, tuple)):
                raise JsonSchemaValueException("data.obsoletes must be array", value=data__obsoletes, name="data.obsoletes", definition={'$$description': ['Packages which this package renders obsolete', '**(not supported by pip)**'], 'type': 'array', 'items': {'type': 'string', 'format': 'pep508-identifier'}}, rule='type')
            data__obsoletes_is_list = isinstance(data__obsoletes, (list, tuple))
            if data__obsoletes_is_list:
                data__obsoletes_len = len(data__obsoletes)
                for data__obsoletes_x, data__obsoletes_item in enumerate(data__obsoletes):
                    if not isinstance(data__obsoletes_item, (str)):
                        raise JsonSchemaValueException(""+"data.obsoletes[{data__obsoletes_x}]".format(**locals())+" must be string", value=data__obsoletes_item, name=""+"data.obsoletes[{data__obsoletes_x}]".format(**locals())+"", definition={'type': 'string', 'format': 'pep508-identifier'}, rule='type')
                    if isinstance(data__obsoletes_item, str):
                        if not custom_formats["pep508-identifier"](data__obsoletes_item):
                            raise JsonSchemaValueException(""+"data.obsoletes[{data__obsoletes_x}]".format(**locals())+" must be pep508-identifier", value=data__obsoletes_item, name=""+"data.obsoletes[{data__obsoletes_x}]".format(**locals())+"", definition={'type': 'string', 'format': 'pep508-identifier'}, rule='format')
        if "zip-safe" in data_keys:
            data_keys.remove("zip-safe")
            data__zipsafe = data["zip-safe"]
            if not isinstance(data__zipsafe, (bool)):
                raise JsonSchemaValueException("data.zip-safe must be boolean", value=data__zipsafe, name="data.zip-safe", definition={'description': 'Whether the project can be safely installed and run from a zip file.', 'type': 'boolean'}, rule='type')
        if "script-files" in data_keys:
            data_keys.remove("script-files")
            data__scriptfiles = data["script-files"]
            if not isinstance(data__scriptfiles, (list, tuple)):
                raise JsonSchemaValueException("data.script-files must be array", value=data__scriptfiles, name="data.script-files", definition={'description': 'Legacy way of defining scripts (entry-points are preferred).', 'type': 'array', 'items': {'type': 'string'}, '$comment': 'TODO: is this field deprecated/should be removed?'}, rule='type')
            data__scriptfiles_is_list = isinstance(data__scriptfiles, (list, tuple))
            if data__scriptfiles_is_list:
                data__scriptfiles_len = len(data__scriptfiles)
                for data__scriptfiles_x, data__scriptfiles_item in enumerate(data__scriptfiles):
                    if not isinstance(data__scriptfiles_item, (str)):
                        raise JsonSchemaValueException(""+"data.script-files[{data__scriptfiles_x}]".format(**locals())+" must be string", value=data__scriptfiles_item, name=""+"data.script-files[{data__scriptfiles_x}]".format(**locals())+"", definition={'type': 'string'}, rule='type')
        if "eager-resources" in data_keys:
            data_keys.remove("eager-resources")
            data__eagerresources = data["eager-resources"]
            if not isinstance(data__eagerresources, (list, tuple)):
                raise JsonSchemaValueException("data.eager-resources must be array", value=data__eagerresources, name="data.eager-resources", definition={'$$description': ['Resources that should be extracted together, if any of them is needed,', 'or if any C extensions included in the project are imported.'], 'type': 'array', 'items': {'type': 'string'}}, rule='type')
            data__eagerresources_is_list = isinstance(data__eagerresources, (list, tuple))
            if data__eagerresources_is_list:
                data__eagerresources_len = len(data__eagerresources)
                for data__eagerresources_x, data__eagerresources_item in enumerate(data__eagerresources):
                    if not isinstance(data__eagerresources_item, (str)):
                        raise JsonSchemaValueException(""+"data.eager-resources[{data__eagerresources_x}]".format(**locals())+" must be string", value=data__eagerresources_item, name=""+"data.eager-resources[{data__eagerresources_x}]".format(**locals())+"", definition={'type': 'string'}, rule='type')
        if "packages" in data_keys:
            data_keys.remove("packages")
            data__packages = data["packages"]
            data__packages_one_of_count1 = 0
            if data__packages_one_of_count1 < 2:
                try:
                    if not isinstance(data__packages, (list, tuple)):
                        raise JsonSchemaValueException("data.packages must be array", value=data__packages, name="data.packages", definition={'title': 'Array of Python package identifiers', 'type': 'array', 'items': {'type': 'string', 'format': 'python-module-name'}}, rule='type')
                    data__packages_is_list = isinstance(data__packages, (list, tuple))
                    if data__packages_is_list:
                        data__packages_len = len(data__packages)
                        for data__packages_x, data__packages_item in enumerate(data__packages):
                            if not isinstance(data__packages_item, (str)):
                                raise JsonSchemaValueException(""+"data.packages[{data__packages_x}]".format(**locals())+" must be string", value=data__packages_item, name=""+"data.packages[{data__packages_x}]".format(**locals())+"", definition={'type': 'string', 'format': 'python-module-name'}, rule='type')
                            if isinstance(data__packages_item, str):
                                if not custom_formats["python-module-name"](data__packages_item):
                                    raise JsonSchemaValueException(""+"data.packages[{data__packages_x}]".format(**locals())+" must be python-module-name", value=data__packages_item, name=""+"data.packages[{data__packages_x}]".format(**locals())+"", definition={'type': 'string', 'format': 'python-module-name'}, rule='format')
                    data__packages_one_of_count1 += 1
                except JsonSchemaValueException: pass
            if data__packages_one_of_count1 < 2:
                try:
                    validate_https___setuptools_pypa_io_en_latest_references_keywords_html__definitions_find_directive(data__packages, custom_formats)
                    data__packages_one_of_count1 += 1
                except JsonSchemaValueException: pass
            if data__packages_one_of_count1 != 1:
                raise JsonSchemaValueException("data.packages must be valid exactly by one of oneOf definition", value=data__packages, name="data.packages", definition={'$$description': ['Packages that should be included in the distribution.', 'It can be given either as a list of package identifiers', 'or as a ``dict``-like structure with a single key ``find``', 'which corresponds to a dynamic call to', '``setuptools.config.expand.find_packages`` function.', 'The ``find`` key is associated with a nested ``dict``-like structure that can', 'contain ``where``, ``include``, ``exclude`` and ``namespaces`` keys,', 'mimicking the keyword arguments of the associated function.'], 'oneOf': [{'title': 'Array of Python package identifiers', 'type': 'array', 'items': {'type': 'string', 'format': 'python-module-name'}}, {'$ref': '#/definitions/find-directive'}]}, rule='oneOf')
        if "package-dir" in data_keys:
            data_keys.remove("package-dir")
            data__packagedir = data["package-dir"]
            if not isinstance(data__packagedir, (dict)):
                raise JsonSchemaValueException("data.package-dir must be object", value=data__packagedir, name="data.package-dir", definition={'$$description': [':class:`dict`-like structure mapping from package names to directories where their', 'code can be found.', 'The empty string (as key) means that all packages are contained inside', 'the given directory will be included in the distribution.'], 'type': 'object', 'additionalProperties': False, 'propertyNames': {'oneOf': [{'format': 'python-module-name'}, {'const': ''}]}, 'patternProperties': {'^.*$': {'type': 'string'}}}, rule='type')
            data__packagedir_is_dict = isinstance(data__packagedir, dict)
            if data__packagedir_is_dict:
                data__packagedir_keys = set(data__packagedir.keys())
                for data__packagedir_key, data__packagedir_val in data__packagedir.items():
                    if REGEX_PATTERNS['^.*$'].search(data__packagedir_key):
                        if data__packagedir_key in data__packagedir_keys:
                            data__packagedir_keys.remove(data__packagedir_key)
                        if not isinstance(data__packagedir_val, (str)):
                            raise JsonSchemaValueException(""+"data.package-dir.{data__packagedir_key}".format(**locals())+" must be string", value=data__packagedir_val, name=""+"data.package-dir.{data__packagedir_key}".format(**locals())+"", definition={'type': 'string'}, rule='type')
                if data__packagedir_keys:
                    raise JsonSchemaValueException("data.package-dir must not contain "+str(data__packagedir_keys)+" properties", value=data__packagedir, name="data.package-dir", definition={'$$description': [':class:`dict`-like structure mapping from package names to directories where their', 'code can be found.', 'The empty string (as key) means that all packages are contained inside', 'the given directory will be included in the distribution.'], 'type': 'object', 'additionalProperties': False, 'propertyNames': {'oneOf': [{'format': 'python-module-name'}, {'const': ''}]}, 'patternProperties': {'^.*$': {'type': 'string'}}}, rule='additionalProperties')
                data__packagedir_len = len(data__packagedir)
                if data__packagedir_len != 0:
                    data__packagedir_property_names = True
                    for data__packagedir_key in data__packagedir:
                        try:
                            data__packagedir_key_one_of_count2 = 0
                            if data__packagedir_key_one_of_count2 < 2:
                                try:
                                    if isinstance(data__packagedir_key, str):
                                        if not custom_formats["python-module-name"](data__packagedir_key):
                                            raise JsonSchemaValueException("data.package-dir must be python-module-name", value=data__packagedir_key, name="data.package-dir", definition={'format': 'python-module-name'}, rule='format')
                                    data__packagedir_key_one_of_count2 += 1
                                except JsonSchemaValueException: pass
                            if data__packagedir_key_one_of_count2 < 2:
                                try:
                                    if data__packagedir_key != "":
                                        raise JsonSchemaValueException("data.package-dir must be same as const definition: ", value=data__packagedir_key, name="data.package-dir", definition={'const': ''}, rule='const')
                                    data__packagedir_key_one_of_count2 += 1
                                except JsonSchemaValueException: pass
                            if data__packagedir_key_one_of_count2 != 1:
                                raise JsonSchemaValueException("data.package-dir must be valid exactly by one of oneOf definition", value=data__packagedir_key, name="data.package-dir", definition={'oneOf': [{'format': 'python-module-name'}, {'const': ''}]}, rule='oneOf')
                        except JsonSchemaValueException:
                            data__packagedir_property_names = False
                    if not data__packagedir_property_names:
                        raise JsonSchemaValueException("data.package-dir must be named by propertyName definition", value=data__packagedir, name="data.package-dir", definition={'$$description': [':class:`dict`-like structure mapping from package names to directories where their', 'code can be found.', 'The empty string (as key) means that all packages are contained inside', 'the given directory will be included in the distribution.'], 'type': 'object', 'additionalProperties': False, 'propertyNames': {'oneOf': [{'format': 'python-module-name'}, {'const': ''}]}, 'patternProperties': {'^.*$': {'type': 'string'}}}, rule='propertyNames')
        if "package-data" in data_keys:
            data_keys.remove("package-data")
            data__packagedata = data["package-data"]
            if not isinstance(data__packagedata, (dict)):
                raise JsonSchemaValueException("data.package-data must be object", value=data__packagedata, name="data.package-data", definition={'$$description': ['Mapping from package names to lists of glob patterns.', 'Usually this option is not needed when using ``include-package-data = true``', 'For more information on how to include data files, check ``setuptools`` `docs', '<https://setuptools.pypa.io/en/latest/userguide/datafiles.html>`_.'], 'type': 'object', 'additionalProperties': False, 'propertyNames': {'oneOf': [{'format': 'python-module-name'}, {'const': '*'}]}, 'patternProperties': {'^.*$': {'type': 'array', 'items': {'type': 'string'}}}}, rule='type')
            data__packagedata_is_dict = isinstance(data__packagedata, dict)
            if data__packagedata_is_dict:
                data__packagedata_keys = set(data__packagedata.keys())
                for data__packagedata_key, data__packagedata_val in data__packagedata.items():
                    if REGEX_PATTERNS['^.*$'].search(data__packagedata_key):
                        if data__packagedata_key in data__packagedata_keys:
                            data__packagedata_keys.remove(data__packagedata_key)
                        if not isinstance(data__packagedata_val, (list, tuple)):
                            raise JsonSchemaValueException(""+"data.package-data.{data__packagedata_key}".format(**locals())+" must be array", value=data__packagedata_val, name=""+"data.package-data.{data__packagedata_key}".format(**locals())+"", definition={'type': 'array', 'items': {'type': 'string'}}, rule='type')
                        data__packagedata_val_is_list = isinstance(data__packagedata_val, (list, tuple))
                        if data__packagedata_val_is_list:
                            data__packagedata_val_len = len(data__packagedata_val)
                            for data__packagedata_val_x, data__packagedata_val_item in enumerate(data__packagedata_val):
                                if not isinstance(data__packagedata_val_item, (str)):
                                    raise JsonSchemaValueException(""+"data.package-data.{data__packagedata_key}[{data__packagedata_val_x}]".format(**locals())+" must be string", value=data__packagedata_val_item, name=""+"data.package-data.{data__packagedata_key}[{data__packagedata_val_x}]".format(**locals())+"", definition={'type': 'string'}, rule='type')
                if data__packagedata_keys:
                    raise JsonSchemaValueException("data.package-data must not contain "+str(data__packagedata_keys)+" properties", value=data__packagedata, name="data.package-data", definition={'$$description': ['Mapping from package names to lists of glob patterns.', 'Usually this option is not needed when using ``include-package-data = true``', 'For more information on how to include data files, check ``setuptools`` `docs', '<https://setuptools.pypa.io/en/latest/userguide/datafiles.html>`_.'], 'type': 'object', 'additionalProperties': False, 'propertyNames': {'oneOf': [{'format': 'python-module-name'}, {'const': '*'}]}, 'patternProperties': {'^.*$': {'type': 'array', 'items': {'type': 'string'}}}}, rule='additionalProperties')
                data__packagedata_len = len(data__packagedata)
                if data__packagedata_len != 0:
                    data__packagedata_property_names = True
                    for data__packagedata_key in data__packagedata:
                        try:
                            data__packagedata_key_one_of_count3 = 0
                            if data__packagedata_key_one_of_count3 < 2:
                                try:
                                    if isinstance(data__packagedata_key, str):
                                        if not custom_formats["python-module-name"](data__packagedata_key):
                                            raise JsonSchemaValueException("data.package-data must be python-module-name", value=data__packagedata_key, name="data.package-data", definition={'format': 'python-module-name'}, rule='format')
                                    data__packagedata_key_one_of_count3 += 1
                                except JsonSchemaValueException: pass
                            if data__packagedata_key_one_of_count3 < 2:
                                try:
                                    if data__packagedata_key != "*":
                                        raise JsonSchemaValueException("data.package-data must be same as const definition: *", value=data__packagedata_key, name="data.package-data", definition={'const': '*'}, rule='const')
                                    data__packagedata_key_one_of_count3 += 1
                                except JsonSchemaValueException: pass
                            if data__packagedata_key_one_of_count3 != 1:
                                raise JsonSchemaValueException("data.package-data must be valid exactly by one of oneOf definition", value=data__packagedata_key, name="data.package-data", definition={'oneOf': [{'format': 'python-module-name'}, {'const': '*'}]}, rule='oneOf')
                        except JsonSchemaValueException:
                            data__packagedata_property_names = False
                    if not data__packagedata_property_names:
                        raise JsonSchemaValueException("data.package-data must be named by propertyName definition", value=data__packagedata, name="data.package-data", definition={'$$description': ['Mapping from package names to lists of glob patterns.', 'Usually this option is not needed when using ``include-package-data = true``', 'For more information on how to include data files, check ``setuptools`` `docs', '<https://setuptools.pypa.io/en/latest/userguide/datafiles.html>`_.'], 'type': 'object', 'additionalProperties': False, 'propertyNames': {'oneOf': [{'format': 'python-module-name'}, {'const': '*'}]}, 'patternProperties': {'^.*$': {'type': 'array', 'items': {'type': 'string'}}}}, rule='propertyNames')
        if "include-package-data" in data_keys:
            data_keys.remove("include-package-data")
            data__includepackagedata = data["include-package-data"]
            if not isinstance(data__includepackagedata, (bool)):
                raise JsonSchemaValueException("data.include-package-data must be boolean", value=data__includepackagedata, name="data.include-package-data", definition={'$$description': ['Automatically include any data files inside the package directories', 'that are specified by ``MANIFEST.in``', 'For more information on how to include data files, check ``setuptools`` `docs', '<https://setuptools.pypa.io/en/latest/userguide/datafiles.html>`_.'], 'type': 'boolean'}, rule='type')
        if "exclude-package-data" in data_keys:
            data_keys.remove("exclude-package-data")
            data__excludepackagedata = data["exclude-package-data"]
            if not isinstance(data__excludepackagedata, (dict)):
                raise JsonSchemaValueException("data.exclude-package-data must be object", value=data__excludepackagedata, name="data.exclude-package-data", definition={'$$description': ['Mapping from package names to lists of glob patterns that should be excluded', 'For more information on how to include data files, check ``setuptools`` `docs', '<https://setuptools.pypa.io/en/latest/userguide/datafiles.html>`_.'], 'type': 'object', 'additionalProperties': False, 'propertyNames': {'oneOf': [{'format': 'python-module-name'}, {'const': '*'}]}, 'patternProperties': {'^.*$': {'type': 'array', 'items': {'type': 'string'}}}}, rule='type')
            data__excludepackagedata_is_dict = isinstance(data__excludepackagedata, dict)
            if data__excludepackagedata_is_dict:
                data__excludepackagedata_keys = set(data__excludepackagedata.keys())
                for data__excludepackagedata_key, data__excludepackagedata_val in data__excludepackagedata.items():
                    if REGEX_PATTERNS['^.*$'].search(data__excludepackagedata_key):
                        if data__excludepackagedata_key in data__excludepackagedata_keys:
                            data__excludepackagedata_keys.remove(data__excludepackagedata_key)
                        if not isinstance(data__excludepackagedata_val, (list, tuple)):
                            raise JsonSchemaValueException(""+"data.exclude-package-data.{data__excludepackagedata_key}".format(**locals())+" must be array", value=data__excludepackagedata_val, name=""+"data.exclude-package-data.{data__excludepackagedata_key}".format(**locals())+"", definition={'type': 'array', 'items': {'type': 'string'}}, rule='type')
                        data__excludepackagedata_val_is_list = isinstance(data__excludepackagedata_val, (list, tuple))
                        if data__excludepackagedata_val_is_list:
                            data__excludepackagedata_val_len = len(data__excludepackagedata_val)
                            for data__excludepackagedata_val_x, data__excludepackagedata_val_item in enumerate(data__excludepackagedata_val):
                                if not isinstance(data__excludepackagedata_val_item, (str)):
                                    raise JsonSchemaValueException(""+"data.exclude-package-data.{data__excludepackagedata_key}[{data__excludepackagedata_val_x}]".format(**locals())+" must be string", value=data__excludepackagedata_val_item, name=""+"data.exclude-package-data.{data__excludepackagedata_key}[{data__excludepackagedata_val_x}]".format(**locals())+"", definition={'type': 'string'}, rule='type')
                if data__excludepackagedata_keys:
                    raise JsonSchemaValueException("data.exclude-package-data must not contain "+str(data__excludepackagedata_keys)+" properties", value=data__excludepackagedata, name="data.exclude-package-data", definition={'$$description': ['Mapping from package names to lists of glob patterns that should be excluded', 'For more information on how to include data files, check ``setuptools`` `docs', '<https://setuptools.pypa.io/en/latest/userguide/datafiles.html>`_.'], 'type': 'object', 'additionalProperties': False, 'propertyNames': {'oneOf': [{'format': 'python-module-name'}, {'const': '*'}]}, 'patternProperties': {'^.*$': {'type': 'array', 'items': {'type': 'string'}}}}, rule='additionalProperties')
                data__excludepackagedata_len = len(data__excludepackagedata)
                if data__excludepackagedata_len != 0:
                    data__excludepackagedata_property_names = True
                    for data__excludepackagedata_key in data__excludepackagedata:
                        try:
                            data__excludepackagedata_key_one_of_count4 = 0
                            if data__excludepackagedata_key_one_of_count4 < 2:
                                try:
                                    if isinstance(data__excludepackagedata_key, str):
                                        if not custom_formats["python-module-name"](data__excludepackagedata_key):
                                            raise JsonSchemaValueException("data.exclude-package-data must be python-module-name", value=data__excludepackagedata_key, name="data.exclude-package-data", definition={'format': 'python-module-name'}, rule='format')
                                    data__excludepackagedata_key_one_of_count4 += 1
                                except JsonSchemaValueException: pass
                            if data__excludepackagedata_key_one_of_count4 < 2:
                                try:
                                    if data__excludepackagedata_key != "*":
                                        raise JsonSchemaValueException("data.exclude-package-data must be same as const definition: *", value=data__excludepackagedata_key, name="data.exclude-package-data", definition={'const': '*'}, rule='const')
                                    data__excludepackagedata_key_one_of_count4 += 1
                                except JsonSchemaValueException: pass
                            if data__excludepackagedata_key_one_of_count4 != 1:
                                raise JsonSchemaValueException("data.exclude-package-data must be valid exactly by one of oneOf definition", value=data__excludepackagedata_key, name="data.exclude-package-data", definition={'oneOf': [{'format': 'python-module-name'}, {'const': '*'}]}, rule='oneOf')
                        except JsonSchemaValueException:
                            data__excludepackagedata_property_names = False
                    if not data__excludepackagedata_property_names:
                        raise JsonSchemaValueException("data.exclude-package-data must be named by propertyName definition", value=data__excludepackagedata, name="data.exclude-package-data", definition={'$$description': ['Mapping from package names to lists of glob patterns that should be excluded', 'For more information on how to include data files, check ``setuptools`` `docs', '<https://setuptools.pypa.io/en/latest/userguide/datafiles.html>`_.'], 'type': 'object', 'additionalProperties': False, 'propertyNames': {'oneOf': [{'format': 'python-module-name'}, {'const': '*'}]}, 'patternProperties': {'^.*$': {'type': 'array', 'items': {'type': 'string'}}}}, rule='propertyNames')
        if "namespace-packages" in data_keys:
            data_keys.remove("namespace-packages")
            data__namespacepackages = data["namespace-packages"]
            if not isinstance(data__namespacepackages, (list, tuple)):
                raise JsonSchemaValueException("data.namespace-packages must be array", value=data__namespacepackages, name="data.namespace-packages", definition={'type': 'array', 'items': {'type': 'string', 'format': 'python-module-name'}, '$comment': 'https://setuptools.pypa.io/en/latest/userguide/package_discovery.html'}, rule='type')
            data__namespacepackages_is_list = isinstance(data__namespacepackages, (list, tuple))
            if data__namespacepackages_is_list:
                data__namespacepackages_len = len(data__namespacepackages)
                for data__namespacepackages_x, data__namespacepackages_item in enumerate(data__namespacepackages):
                    if not isinstance(data__namespacepackages_item, (str)):
                        raise JsonSchemaValueException(""+"data.namespace-packages[{data__namespacepackages_x}]".format(**locals())+" must be string", value=data__namespacepackages_item, name=""+"data.namespace-packages[{data__namespacepackages_x}]".format(**locals())+"", definition={'type': 'string', 'format': 'python-module-name'}, rule='type')
                    if isinstance(data__namespacepackages_item, str):
                        if not custom_formats["python-module-name"](data__namespacepackages_item):
                            raise JsonSchemaValueException(""+"data.namespace-packages[{data__namespacepackages_x}]".format(**locals())+" must be python-module-name", value=data__namespacepackages_item, name=""+"data.namespace-packages[{data__namespacepackages_x}]".format(**locals())+"", definition={'type': 'string', 'format': 'python-module-name'}, rule='format')
        if "py-modules" in data_keys:
            data_keys.remove("py-modules")
            data__pymodules = data["py-modules"]
            if not isinstance(data__pymodules, (list, tuple)):
                raise JsonSchemaValueException("data.py-modules must be array", value=data__pymodules, name="data.py-modules", definition={'description': 'Modules that setuptools will manipulate', 'type': 'array', 'items': {'type': 'string', 'format': 'python-module-name'}, '$comment': 'TODO: clarify the relationship with ``packages``'}, rule='type')
            data__pymodules_is_list = isinstance(data__pymodules, (list, tuple))
            if data__pymodules_is_list:
                data__pymodules_len = len(data__pymodules)
                for data__pymodules_x, data__pymodules_item in enumerate(data__pymodules):
                    if not isinstance(data__pymodules_item, (str)):
                        raise JsonSchemaValueException(""+"data.py-modules[{data__pymodules_x}]".format(**locals())+" must be string", value=data__pymodules_item, name=""+"data.py-modules[{data__pymodules_x}]".format(**locals())+"", definition={'type': 'string', 'format': 'python-module-name'}, rule='type')
                    if isinstance(data__pymodules_item, str):
                        if not custom_formats["python-module-name"](data__pymodules_item):
                            raise JsonSchemaValueException(""+"data.py-modules[{data__pymodules_x}]".format(**locals())+" must be python-module-name", value=data__pymodules_item, name=""+"data.py-modules[{data__pymodules_x}]".format(**locals())+"", definition={'type': 'string', 'format': 'python-module-name'}, rule='format')
        if "data-files" in data_keys:
            data_keys.remove("data-files")
            data__datafiles = data["data-files"]
            if not isinstance(data__datafiles, (dict)):
                raise JsonSchemaValueException("data.data-files must be object", value=data__datafiles, name="data.data-files", definition={'$$description': ['**DEPRECATED**: dict-like structure where each key represents a directory and', 'the value is a list of glob patterns that should be installed in them.', "Please notice this don't work with wheels. See `data files support", '<https://setuptools.pypa.io/en/latest/userguide/datafiles.html>`_'], 'type': 'object', 'patternProperties': {'^.*$': {'type': 'array', 'items': {'type': 'string'}}}}, rule='type')
            data__datafiles_is_dict = isinstance(data__datafiles, dict)
            if data__datafiles_is_dict:
                data__datafiles_keys = set(data__datafiles.keys())
                for data__datafiles_key, data__datafiles_val in data__datafiles.items():
                    if REGEX_PATTERNS['^.*$'].search(data__datafiles_key):
                        if data__datafiles_key in data__datafiles_keys:
                            data__datafiles_keys.remove(data__datafiles_key)
                        if not isinstance(data__datafiles_val, (list, tuple)):
                            raise JsonSchemaValueException(""+"data.data-files.{data__datafiles_key}".format(**locals())+" must be array", value=data__datafiles_val, name=""+"data.data-files.{data__datafiles_key}".format(**locals())+"", definition={'type': 'array', 'items': {'type': 'string'}}, rule='type')
                        data__datafiles_val_is_list = isinstance(data__datafiles_val, (list, tuple))
                        if data__datafiles_val_is_list:
                            data__datafiles_val_len = len(data__datafiles_val)
                            for data__datafiles_val_x, data__datafiles_val_item in enumerate(data__datafiles_val):
                                if not isinstance(data__datafiles_val_item, (str)):
                                    raise JsonSchemaValueException(""+"data.data-files.{data__datafiles_key}[{data__datafiles_val_x}]".format(**locals())+" must be string", value=data__datafiles_val_item, name=""+"data.data-files.{data__datafiles_key}[{data__datafiles_val_x}]".format(**locals())+"", definition={'type': 'string'}, rule='type')
        if "cmdclass" in data_keys:
            data_keys.remove("cmdclass")
            data__cmdclass = data["cmdclass"]
            if not isinstance(data__cmdclass, (dict)):
                raise JsonSchemaValueException("data.cmdclass must be object", value=data__cmdclass, name="data.cmdclass", definition={'$$description': ['Mapping of distutils-style command names to ``setuptools.Command`` subclasses', 'which in turn should be represented by strings with a qualified class name', '(i.e., "dotted" form with module), e.g.::\n\n', '    cmdclass = {mycmd = "pkg.subpkg.module.CommandClass"}\n\n', 'The command class should be a directly defined at the top-level of the', 'containing module (no class nesting).'], 'type': 'object', 'patternProperties': {'^.*$': {'type': 'string', 'format': 'python-qualified-identifier'}}}, rule='type')
            data__cmdclass_is_dict = isinstance(data__cmdclass, dict)
            if data__cmdclass_is_dict:
                data__cmdclass_keys = set(data__cmdclass.keys())
                for data__cmdclass_key, data__cmdclass_val in data__cmdclass.items():
                    if REGEX_PATTERNS['^.*$'].search(data__cmdclass_key):
                        if data__cmdclass_key in data__cmdclass_keys:
                            data__cmdclass_keys.remove(data__cmdclass_key)
                        if not isinstance(data__cmdclass_val, (str)):
                            raise JsonSchemaValueException(""+"data.cmdclass.{data__cmdclass_key}".format(**locals())+" must be string", value=data__cmdclass_val, name=""+"data.cmdclass.{data__cmdclass_key}".format(**locals())+"", definition={'type': 'string', 'format': 'python-qualified-identifier'}, rule='type')
                        if isinstance(data__cmdclass_val, str):
                            if not custom_formats["python-qualified-identifier"](data__cmdclass_val):
                                raise JsonSchemaValueException(""+"data.cmdclass.{data__cmdclass_key}".format(**locals())+" must be python-qualified-identifier", value=data__cmdclass_val, name=""+"data.cmdclass.{data__cmdclass_key}".format(**locals())+"", definition={'type': 'string', 'format': 'python-qualified-identifier'}, rule='format')
        if "dynamic" in data_keys:
            data_keys.remove("dynamic")
            data__dynamic = data["dynamic"]
            if not isinstance(data__dynamic, (dict)):
                raise JsonSchemaValueException("data.dynamic must be object", value=data__dynamic, name="data.dynamic", definition={'type': 'object', 'description': 'Instructions for loading :pep:`621`-related metadata dynamically', 'properties': {'version': {'$$description': ['A version dynamically loaded via either the ``attr:`` or ``file:``', 'directives. Please make sure the given file or attribute respects :pep:`440`.'], 'oneOf': [{'$ref': '#/definitions/attr-directive'}, {'$ref': '#/definitions/file-directive'}]}, 'classifiers': {'$ref': '#/definitions/file-directive'}, 'description': {'$ref': '#/definitions/file-directive'}, 'entry-points': {'$ref': '#/definitions/file-directive'}, 'readme': {'anyOf': [{'$ref': '#/definitions/file-directive'}, {'properties': {'content-type': {'type': 'string'}}}], 'required': ['file']}, 'license': {'type': 'string', '$$description': ['PROVISIONAL: A string specifying the license of the package', '(might change with PEP 639)'], '$comment': 'TODO: revise if PEP 639 is accepted. Maybe ``license-expression``?'}, 'license-files': {'type': 'array', 'items': {'type': 'string'}, '$$description': ['PROVISIONAL: List of glob patterns for all license files being distributed.', '(might change with PEP 639)'], 'default': ['LICEN[CS]E*', ' COPYING*', ' NOTICE*', 'AUTHORS*'], '$comment': 'TODO: revise if PEP 639 is accepted. Maybe ``license-files.glob``?'}}}, rule='type')
            data__dynamic_is_dict = isinstance(data__dynamic, dict)
            if data__dynamic_is_dict:
                data__dynamic_keys = set(data__dynamic.keys())
                if "version" in data__dynamic_keys:
                    data__dynamic_keys.remove("version")
                    data__dynamic__version = data__dynamic["version"]
                    data__dynamic__version_one_of_count5 = 0
                    if data__dynamic__version_one_of_count5 < 2:
                        try:
                            validate_https___setuptools_pypa_io_en_latest_references_keywords_html__definitions_attr_directive(data__dynamic__version, custom_formats)
                            data__dynamic__version_one_of_count5 += 1
                        except JsonSchemaValueException: pass
                    if data__dynamic__version_one_of_count5 < 2:
                        try:
                            validate_https___setuptools_pypa_io_en_latest_references_keywords_html__definitions_file_directive(data__dynamic__version, custom_formats)
                            data__dynamic__version_one_of_count5 += 1
                        except JsonSchemaValueException: pass
                    if data__dynamic__version_one_of_count5 != 1:
                        raise JsonSchemaValueException("data.dynamic.version must be valid exactly by one of oneOf definition", value=data__dynamic__version, name="data.dynamic.version", definition={'$$description': ['A version dynamically loaded via either the ``attr:`` or ``file:``', 'directives. Please make sure the given file or attribute respects :pep:`440`.'], 'oneOf': [{'$ref': '#/definitions/attr-directive'}, {'$ref': '#/definitions/file-directive'}]}, rule='oneOf')
                if "classifiers" in data__dynamic_keys:
                    data__dynamic_keys.remove("classifiers")
                    data__dynamic__classifiers = data__dynamic["classifiers"]
                    validate_https___setuptools_pypa_io_en_latest_references_keywords_html__definitions_file_directive(data__dynamic__classifiers, custom_formats)
                if "description" in data__dynamic_keys:
                    data__dynamic_keys.remove("description")
                    data__dynamic__description = data__dynamic["description"]
                    validate_https___setuptools_pypa_io_en_latest_references_keywords_html__definitions_file_directive(data__dynamic__description, custom_formats)
                if "entry-points" in data__dynamic_keys:
                    data__dynamic_keys.remove("entry-points")
                    data__dynamic__entrypoints = data__dynamic["entry-points"]
                    validate_https___setuptools_pypa_io_en_latest_references_keywords_html__definitions_file_directive(data__dynamic__entrypoints, custom_formats)
                if "readme" in data__dynamic_keys:
                    data__dynamic_keys.remove("readme")
                    data__dynamic__readme = data__dynamic["readme"]
                    data__dynamic__readme_any_of_count6 = 0
                    if not data__dynamic__readme_any_of_count6:
                        try:
                            validate_https___setuptools_pypa_io_en_latest_references_keywords_html__definitions_file_directive(data__dynamic__readme, custom_formats)
                            data__dynamic__readme_any_of_count6 += 1
                        except JsonSchemaValueException: pass
                    if not data__dynamic__readme_any_of_count6:
                        try:
                            data__dynamic__readme_is_dict = isinstance(data__dynamic__readme, dict)
                            if data__dynamic__readme_is_dict:
                                data__dynamic__readme_keys = set(data__dynamic__readme.keys())
                                if "content-type" in data__dynamic__readme_keys:
                                    data__dynamic__readme_keys.remove("content-type")
                                    data__dynamic__readme__contenttype = data__dynamic__readme["content-type"]
                                    if not isinstance(data__dynamic__readme__contenttype, (str)):
                                        raise JsonSchemaValueException("data.dynamic.readme.content-type must be string", value=data__dynamic__readme__contenttype, name="data.dynamic.readme.content-type", definition={'type': 'string'}, rule='type')
                            data__dynamic__readme_any_of_count6 += 1
                        except JsonSchemaValueException: pass
                    if not data__dynamic__readme_any_of_count6:
                        raise JsonSchemaValueException("data.dynamic.readme must be valid by one of anyOf definition", value=data__dynamic__readme, name="data.dynamic.readme", definition={'anyOf': [{'$ref': '#/definitions/file-directive'}, {'properties': {'content-type': {'type': 'string'}}}], 'required': ['file']}, rule='anyOf')
                    data__dynamic__readme_is_dict = isinstance(data__dynamic__readme, dict)
                    if data__dynamic__readme_is_dict:
                        data__dynamic__readme_len = len(data__dynamic__readme)
                        if not all(prop in data__dynamic__readme for prop in ['file']):
                            raise JsonSchemaValueException("data.dynamic.readme must contain ['file'] properties", value=data__dynamic__readme, name="data.dynamic.readme", definition={'anyOf': [{'$ref': '#/definitions/file-directive'}, {'properties': {'content-type': {'type': 'string'}}}], 'required': ['file']}, rule='required')
                if "license" in data__dynamic_keys:
                    data__dynamic_keys.remove("license")
                    data__dynamic__license = data__dynamic["license"]
                    if not isinstance(data__dynamic__license, (str)):
                        raise JsonSchemaValueException("data.dynamic.license must be string", value=data__dynamic__license, name="data.dynamic.license", definition={'type': 'string', '$$description': ['PROVISIONAL: A string specifying the license of the package', '(might change with PEP 639)'], '$comment': 'TODO: revise if PEP 639 is accepted. Maybe ``license-expression``?'}, rule='type')
                if "license-files" in data__dynamic_keys:
                    data__dynamic_keys.remove("license-files")
                    data__dynamic__licensefiles = data__dynamic["license-files"]
                    if not isinstance(data__dynamic__licensefiles, (list, tuple)):
                        raise JsonSchemaValueException("data.dynamic.license-files must be array", value=data__dynamic__licensefiles, name="data.dynamic.license-files", definition={'type': 'array', 'items': {'type': 'string'}, '$$description': ['PROVISIONAL: List of glob patterns for all license files being distributed.', '(might change with PEP 639)'], 'default': ['LICEN[CS]E*', ' COPYING*', ' NOTICE*', 'AUTHORS*'], '$comment': 'TODO: revise if PEP 639 is accepted. Maybe ``license-files.glob``?'}, rule='type')
                    data__dynamic__licensefiles_is_list = isinstance(data__dynamic__licensefiles, (list, tuple))
                    if data__dynamic__licensefiles_is_list:
                        data__dynamic__licensefiles_len = len(data__dynamic__licensefiles)
                        for data__dynamic__licensefiles_x, data__dynamic__licensefiles_item in enumerate(data__dynamic__licensefiles):
                            if not isinstance(data__dynamic__licensefiles_item, (str)):
                                raise JsonSchemaValueException(""+"data.dynamic.license-files[{data__dynamic__licensefiles_x}]".format(**locals())+" must be string", value=data__dynamic__licensefiles_item, name=""+"data.dynamic.license-files[{data__dynamic__licensefiles_x}]".format(**locals())+"", definition={'type': 'string'}, rule='type')
                else: data__dynamic["license-files"] = ['LICEN[CS]E*', ' COPYING*', ' NOTICE*', 'AUTHORS*']
        if data_keys:
            raise JsonSchemaValueException("data must not contain "+str(data_keys)+" properties", value=data, name="data", definition={'$schema': 'http://json-schema.org/draft-07/schema', '$id': 'https://setuptools.pypa.io/en/latest/references/keywords.html', 'title': '``tool.setuptools`` table', '$$description': ['Please notice for the time being the ``setuptools`` project does not specify', 'a way of configuring builds via ``pyproject.toml``.', 'Therefore this schema should be taken just as a *"thought experiment"* on how', 'this *might be done*, by following the principles established in', '`ini2toml <https://ini2toml.readthedocs.io/en/latest/setuptools_pep621.html>`_.', 'It considers only ``setuptools`` `parameters', '<https://setuptools.pypa.io/en/latest/userguide/declarative_config.html>`_', 'that can currently be configured via ``setup.cfg`` and are not covered by :pep:`621`', 'but intentionally excludes ``dependency_links`` and ``setup_requires``.', 'NOTE: ``scripts`` was renamed to ``script-files`` to avoid confusion with', 'entry-point based scripts (defined in :pep:`621`).'], 'type': 'object', 'additionalProperties': False, 'properties': {'platforms': {'type': 'array', 'items': {'type': 'string'}}, 'provides': {'$$description': ['Package and virtual package names contained within this package', '**(not supported by pip)**'], 'type': 'array', 'items': {'type': 'string', 'format': 'pep508-identifier'}}, 'obsoletes': {'$$description': ['Packages which this package renders obsolete', '**(not supported by pip)**'], 'type': 'array', 'items': {'type': 'string', 'format': 'pep508-identifier'}}, 'zip-safe': {'description': 'Whether the project can be safely installed and run from a zip file.', 'type': 'boolean'}, 'script-files': {'description': 'Legacy way of defining scripts (entry-points are preferred).', 'type': 'array', 'items': {'type': 'string'}, '$comment': 'TODO: is this field deprecated/should be removed?'}, 'eager-resources': {'$$description': ['Resources that should be extracted together, if any of them is needed,', 'or if any C extensions included in the project are imported.'], 'type': 'array', 'items': {'type': 'string'}}, 'packages': {'$$description': ['Packages that should be included in the distribution.', 'It can be given either as a list of package identifiers', 'or as a ``dict``-like structure with a single key ``find``', 'which corresponds to a dynamic call to', '``setuptools.config.expand.find_packages`` function.', 'The ``find`` key is associated with a nested ``dict``-like structure that can', 'contain ``where``, ``include``, ``exclude`` and ``namespaces`` keys,', 'mimicking the keyword arguments of the associated function.'], 'oneOf': [{'title': 'Array of Python package identifiers', 'type': 'array', 'items': {'type': 'string', 'format': 'python-module-name'}}, {'$ref': '#/definitions/find-directive'}]}, 'package-dir': {'$$description': [':class:`dict`-like structure mapping from package names to directories where their', 'code can be found.', 'The empty string (as key) means that all packages are contained inside', 'the given directory will be included in the distribution.'], 'type': 'object', 'additionalProperties': False, 'propertyNames': {'oneOf': [{'format': 'python-module-name'}, {'const': ''}]}, 'patternProperties': {'^.*$': {'type': 'string'}}}, 'package-data': {'$$description': ['Mapping from package names to lists of glob patterns.', 'Usually this option is not needed when using ``include-package-data = true``', 'For more information on how to include data files, check ``setuptools`` `docs', '<https://setuptools.pypa.io/en/latest/userguide/datafiles.html>`_.'], 'type': 'object', 'additionalProperties': False, 'propertyNames': {'oneOf': [{'format': 'python-module-name'}, {'const': '*'}]}, 'patternProperties': {'^.*$': {'type': 'array', 'items': {'type': 'string'}}}}, 'include-package-data': {'$$description': ['Automatically include any data files inside the package directories', 'that are specified by ``MANIFEST.in``', 'For more information on how to include data files, check ``setuptools`` `docs', '<https://setuptools.pypa.io/en/latest/userguide/datafiles.html>`_.'], 'type': 'boolean'}, 'exclude-package-data': {'$$description': ['Mapping from package names to lists of glob patterns that should be excluded', 'For more information on how to include data files, check ``setuptools`` `docs', '<https://setuptools.pypa.io/en/latest/userguide/datafiles.html>`_.'], 'type': 'object', 'additionalProperties': False, 'propertyNames': {'oneOf': [{'format': 'python-module-name'}, {'const': '*'}]}, 'patternProperties': {'^.*$': {'type': 'array', 'items': {'type': 'string'}}}}, 'namespace-packages': {'type': 'array', 'items': {'type': 'string', 'format': 'python-module-name'}, '$comment': 'https://setuptools.pypa.io/en/latest/userguide/package_discovery.html'}, 'py-modules': {'description': 'Modules that setuptools will manipulate', 'type': 'array', 'items': {'type': 'string', 'format': 'python-module-name'}, '$comment': 'TODO: clarify the relationship with ``packages``'}, 'data-files': {'$$description': ['**DEPRECATED**: dict-like structure where each key represents a directory and', 'the value is a list of glob patterns that should be installed in them.', "Please notice this don't work with wheels. See `data files support", '<https://setuptools.pypa.io/en/latest/userguide/datafiles.html>`_'], 'type': 'object', 'patternProperties': {'^.*$': {'type': 'array', 'items': {'type': 'string'}}}}, 'cmdclass': {'$$description': ['Mapping of distutils-style command names to ``setuptools.Command`` subclasses', 'which in turn should be represented by strings with a qualified class name', '(i.e., "dotted" form with module), e.g.::\n\n', '    cmdclass = {mycmd = "pkg.subpkg.module.CommandClass"}\n\n', 'The command class should be a directly defined at the top-level of the', 'containing module (no class nesting).'], 'type': 'object', 'patternProperties': {'^.*$': {'type': 'string', 'format': 'python-qualified-identifier'}}}, 'dynamic': {'type': 'object', 'description': 'Instructions for loading :pep:`621`-related metadata dynamically', 'properties': {'version': {'$$description': ['A version dynamically loaded via either the ``attr:`` or ``file:``', 'directives. Please make sure the given file or attribute respects :pep:`440`.'], 'oneOf': [{'$ref': '#/definitions/attr-directive'}, {'$ref': '#/definitions/file-directive'}]}, 'classifiers': {'$ref': '#/definitions/file-directive'}, 'description': {'$ref': '#/definitions/file-directive'}, 'entry-points': {'$ref': '#/definitions/file-directive'}, 'readme': {'anyOf': [{'$ref': '#/definitions/file-directive'}, {'properties': {'content-type': {'type': 'string'}}}], 'required': ['file']}, 'license': {'type': 'string', '$$description': ['PROVISIONAL: A string specifying the license of the package', '(might change with PEP 639)'], '$comment': 'TODO: revise if PEP 639 is accepted. Maybe ``license-expression``?'}, 'license-files': {'type': 'array', 'items': {'type': 'string'}, '$$description': ['PROVISIONAL: List of glob patterns for all license files being distributed.', '(might change with PEP 639)'], 'default': ['LICEN[CS]E*', ' COPYING*', ' NOTICE*', 'AUTHORS*'], '$comment': 'TODO: revise if PEP 639 is accepted. Maybe ``license-files.glob``?'}}}}, 'definitions': {'file-directive': {'$id': '#/definitions/file-directive', 'title': "'file:' directive", 'description': 'Value is read from a file (or list of files and then concatenated)', 'type': 'object', 'additionalProperties': False, 'properties': {'file': {'oneOf': [{'type': 'string'}, {'type': 'array', 'items': {'type': 'string'}}]}}, 'required': ['file']}, 'attr-directive': {'title': "'attr:' directive", '$id': '#/definitions/attr-directive', '$$description': ['Value is read from a module attribute. Supports callables and iterables;', 'unsupported types are cast via ``str()``'], 'type': 'object', 'additionalProperties': False, 'properties': {'attr': {'type': 'string'}}, 'required': ['attr']}, 'find-directive': {'$id': '#/definitions/find-directive', 'title': "'find:' directive", 'type': 'object', 'additionalProperties': False, 'properties': {'find': {'type': 'object', '$$description': ['Dynamic `package discovery', '<https://setuptools.pypa.io/en/latest/userguide/package_discovery.html>`_.'], 'additionalProperties': False, 'properties': {'where': {'description': 'Directories to be searched for packages (Unix-style relative path)', 'type': 'array', 'items': {'type': 'string'}}, 'exclude': {'type': 'array', '$$description': ['Exclude packages that match the values listed in this field.', "Can container shell-style wildcards (e.g. ``'pkg.*'``)"], 'items': {'type': 'string'}}, 'include': {'type': 'array', '$$description': ['Restrict the found packages to just the ones listed in this field.', "Can container shell-style wildcards (e.g. ``'pkg.*'``)"], 'items': {'type': 'string'}}, 'namespaces': {'type': 'boolean', '$$description': ['When ``True``, directories without a ``__init__.py`` file will also', 'be scanned for :pep:`420`-style implicit namespaces']}}}}}}}, rule='additionalProperties')
    return data

def validate_https___setuptools_pypa_io_en_latest_references_keywords_html__definitions_file_directive(data, custom_formats={}):
    if not isinstance(data, (dict)):
        raise JsonSchemaValueException("data must be object", value=data, name="data", definition={'$id': '#/definitions/file-directive', 'title': "'file:' directive", 'description': 'Value is read from a file (or list of files and then concatenated)', 'type': 'object', 'additionalProperties': False, 'properties': {'file': {'oneOf': [{'type': 'string'}, {'type': 'array', 'items': {'type': 'string'}}]}}, 'required': ['file']}, rule='type')
    data_is_dict = isinstance(data, dict)
    if data_is_dict:
        data_len = len(data)
        if not all(prop in data for prop in ['file']):
            raise JsonSchemaValueException("data must contain ['file'] properties", value=data, name="data", definition={'$id': '#/definitions/file-directive', 'title': "'file:' directive", 'description': 'Value is read from a file (or list of files and then concatenated)', 'type': 'object', 'additionalProperties': False, 'properties': {'file': {'oneOf': [{'type': 'string'}, {'type': 'array', 'items': {'type': 'string'}}]}}, 'required': ['file']}, rule='required')
        data_keys = set(data.keys())
        if "file" in data_keys:
            data_keys.remove("file")
            data__file = data["file"]
            data__file_one_of_count7 = 0
            if data__file_one_of_count7 < 2:
                try:
                    if not isinstance(data__file, (str)):
                        raise JsonSchemaValueException("data.file must be string", value=data__file, name="data.file", definition={'type': 'string'}, rule='type')
                    data__file_one_of_count7 += 1
                except JsonSchemaValueException: pass
            if data__file_one_of_count7 < 2:
                try:
                    if not isinstance(data__file, (list, tuple)):
                        raise JsonSchemaValueException("data.file must be array", value=data__file, name="data.file", definition={'type': 'array', 'items': {'type': 'string'}}, rule='type')
                    data__file_is_list = isinstance(data__file, (list, tuple))
                    if data__file_is_list:
                        data__file_len = len(data__file)
                        for data__file_x, data__file_item in enumerate(data__file):
                            if not isinstance(data__file_item, (str)):
                                raise JsonSchemaValueException(""+"data.file[{data__file_x}]".format(**locals())+" must be string", value=data__file_item, name=""+"data.file[{data__file_x}]".format(**locals())+"", definition={'type': 'string'}, rule='type')
                    data__file_one_of_count7 += 1
                except JsonSchemaValueException: pass
            if data__file_one_of_count7 != 1:
                raise JsonSchemaValueException("data.file must be valid exactly by one of oneOf definition", value=data__file, name="data.file", definition={'oneOf': [{'type': 'string'}, {'type': 'array', 'items': {'type': 'string'}}]}, rule='oneOf')
        if data_keys:
            raise JsonSchemaValueException("data must not contain "+str(data_keys)+" properties", value=data, name="data", definition={'$id': '#/definitions/file-directive', 'title': "'file:' directive", 'description': 'Value is read from a file (or list of files and then concatenated)', 'type': 'object', 'additionalProperties': False, 'properties': {'file': {'oneOf': [{'type': 'string'}, {'type': 'array', 'items': {'type': 'string'}}]}}, 'required': ['file']}, rule='additionalProperties')
    return data

def validate_https___setuptools_pypa_io_en_latest_references_keywords_html__definitions_attr_directive(data, custom_formats={}):
    if not isinstance(data, (dict)):
        raise JsonSchemaValueException("data must be object", value=data, name="data", definition={'title': "'attr:' directive", '$id': '#/definitions/attr-directive', '$$description': ['Value is read from a module attribute. Supports callables and iterables;', 'unsupported types are cast via ``str()``'], 'type': 'object', 'additionalProperties': False, 'properties': {'attr': {'type': 'string'}}, 'required': ['attr']}, rule='type')
    data_is_dict = isinstance(data, dict)
    if data_is_dict:
        data_len = len(data)
        if not all(prop in data for prop in ['attr']):
            raise JsonSchemaValueException("data must contain ['attr'] properties", value=data, name="data", definition={'title': "'attr:' directive", '$id': '#/definitions/attr-directive', '$$description': ['Value is read from a module attribute. Supports callables and iterables;', 'unsupported types are cast via ``str()``'], 'type': 'object', 'additionalProperties': False, 'properties': {'attr': {'type': 'string'}}, 'required': ['attr']}, rule='required')
        data_keys = set(data.keys())
        if "attr" in data_keys:
            data_keys.remove("attr")
            data__attr = data["attr"]
            if not isinstance(data__attr, (str)):
                raise JsonSchemaValueException("data.attr must be string", value=data__attr, name="data.attr", definition={'type': 'string'}, rule='type')
        if data_keys:
            raise JsonSchemaValueException("data must not contain "+str(data_keys)+" properties", value=data, name="data", definition={'title': "'attr:' directive", '$id': '#/definitions/attr-directive', '$$description': ['Value is read from a module attribute. Supports callables and iterables;', 'unsupported types are cast via ``str()``'], 'type': 'object', 'additionalProperties': False, 'properties': {'attr': {'type': 'string'}}, 'required': ['attr']}, rule='additionalProperties')
    return data

def validate_https___setuptools_pypa_io_en_latest_references_keywords_html__definitions_find_directive(data, custom_formats={}):
    if not isinstance(data, (dict)):
        raise JsonSchemaValueException("data must be object", value=data, name="data", definition={'$id': '#/definitions/find-directive', 'title': "'find:' directive", 'type': 'object', 'additionalProperties': False, 'properties': {'find': {'type': 'object', '$$description': ['Dynamic `package discovery', '<https://setuptools.pypa.io/en/latest/userguide/package_discovery.html>`_.'], 'additionalProperties': False, 'properties': {'where': {'description': 'Directories to be searched for packages (Unix-style relative path)', 'type': 'array', 'items': {'type': 'string'}}, 'exclude': {'type': 'array', '$$description': ['Exclude packages that match the values listed in this field.', "Can container shell-style wildcards (e.g. ``'pkg.*'``)"], 'items': {'type': 'string'}}, 'include': {'type': 'array', '$$description': ['Restrict the found packages to just the ones listed in this field.', "Can container shell-style wildcards (e.g. ``'pkg.*'``)"], 'items': {'type': 'string'}}, 'namespaces': {'type': 'boolean', '$$description': ['When ``True``, directories without a ``__init__.py`` file will also', 'be scanned for :pep:`420`-style implicit namespaces']}}}}}, rule='type')
    data_is_dict = isinstance(data, dict)
    if data_is_dict:
        data_keys = set(data.keys())
        if "find" in data_keys:
            data_keys.remove("find")
            data__find = data["find"]
            if not isinstance(data__find, (dict)):
                raise JsonSchemaValueException("data.find must be object", value=data__find, name="data.find", definition={'type': 'object', '$$description': ['Dynamic `package discovery', '<https://setuptools.pypa.io/en/latest/userguide/package_discovery.html>`_.'], 'additionalProperties': False, 'properties': {'where': {'description': 'Directories to be searched for packages (Unix-style relative path)', 'type': 'array', 'items': {'type': 'string'}}, 'exclude': {'type': 'array', '$$description': ['Exclude packages that match the values listed in this field.', "Can container shell-style wildcards (e.g. ``'pkg.*'``)"], 'items': {'type': 'string'}}, 'include': {'type': 'array', '$$description': ['Restrict the found packages to just the ones listed in this field.', "Can container shell-style wildcards (e.g. ``'pkg.*'``)"], 'items': {'type': 'string'}}, 'namespaces': {'type': 'boolean', '$$description': ['When ``True``, directories without a ``__init__.py`` file will also', 'be scanned for :pep:`420`-style implicit namespaces']}}}, rule='type')
            data__find_is_dict = isinstance(data__find, dict)
            if data__find_is_dict:
                data__find_keys = set(data__find.keys())
                if "where" in data__find_keys:
                    data__find_keys.remove("where")
                    data__find__where = data__find["where"]
                    if not isinstance(data__find__where, (list, tuple)):
                        raise JsonSchemaValueException("data.find.where must be array", value=data__find__where, name="data.find.where", definition={'description': 'Directories to be searched for packages (Unix-style relative path)', 'type': 'array', 'items': {'type': 'string'}}, rule='type')
                    data__find__where_is_list = isinstance(data__find__where, (list, tuple))
                    if data__find__where_is_list:
                        data__find__where_len = len(data__find__where)
                        for data__find__where_x, data__find__where_item in enumerate(data__find__where):
                            if not isinstance(data__find__where_item, (str)):
                                raise JsonSchemaValueException(""+"data.find.where[{data__find__where_x}]".format(**locals())+" must be string", value=data__find__where_item, name=""+"data.find.where[{data__find__where_x}]".format(**locals())+"", definition={'type': 'string'}, rule='type')
                if "exclude" in data__find_keys:
                    data__find_keys.remove("exclude")
                    data__find__exclude = data__find["exclude"]
                    if not isinstance(data__find__exclude, (list, tuple)):
                        raise JsonSchemaValueException("data.find.exclude must be array", value=data__find__exclude, name="data.find.exclude", definition={'type': 'array', '$$description': ['Exclude packages that match the values listed in this field.', "Can container shell-style wildcards (e.g. ``'pkg.*'``)"], 'items': {'type': 'string'}}, rule='type')
                    data__find__exclude_is_list = isinstance(data__find__exclude, (list, tuple))
                    if data__find__exclude_is_list:
                        data__find__exclude_len = len(data__find__exclude)
                        for data__find__exclude_x, data__find__exclude_item in enumerate(data__find__exclude):
                            if not isinstance(data__find__exclude_item, (str)):
                                raise JsonSchemaValueException(""+"data.find.exclude[{data__find__exclude_x}]".format(**locals())+" must be string", value=data__find__exclude_item, name=""+"data.find.exclude[{data__find__exclude_x}]".format(**locals())+"", definition={'type': 'string'}, rule='type')
                if "include" in data__find_keys:
                    data__find_keys.remove("include")
                    data__find__include = data__find["include"]
                    if not isinstance(data__find__include, (list, tuple)):
                        raise JsonSchemaValueException("data.find.include must be array", value=data__find__include, name="data.find.include", definition={'type': 'array', '$$description': ['Restrict the found packages to just the ones listed in this field.', "Can container shell-style wildcards (e.g. ``'pkg.*'``)"], 'items': {'type': 'string'}}, rule='type')
                    data__find__include_is_list = isinstance(data__find__include, (list, tuple))
                    if data__find__include_is_list:
                        data__find__include_len = len(data__find__include)
                        for data__find__include_x, data__find__include_item in enumerate(data__find__include):
                            if not isinstance(data__find__include_item, (str)):
                                raise JsonSchemaValueException(""+"data.find.include[{data__find__include_x}]".format(**locals())+" must be string", value=data__find__include_item, name=""+"data.find.include[{data__find__include_x}]".format(**locals())+"", definition={'type': 'string'}, rule='type')
                if "namespaces" in data__find_keys:
                    data__find_keys.remove("namespaces")
                    data__find__namespaces = data__find["namespaces"]
                    if not isinstance(data__find__namespaces, (bool)):
                        raise JsonSchemaValueException("data.find.namespaces must be boolean", value=data__find__namespaces, name="data.find.namespaces", definition={'type': 'boolean', '$$description': ['When ``True``, directories without a ``__init__.py`` file will also', 'be scanned for :pep:`420`-style implicit namespaces']}, rule='type')
                if data__find_keys:
                    raise JsonSchemaValueException("data.find must not contain "+str(data__find_keys)+" properties", value=data__find, name="data.find", definition={'type': 'object', '$$description': ['Dynamic `package discovery', '<https://setuptools.pypa.io/en/latest/userguide/package_discovery.html>`_.'], 'additionalProperties': False, 'properties': {'where': {'description': 'Directories to be searched for packages (Unix-style relative path)', 'type': 'array', 'items': {'type': 'string'}}, 'exclude': {'type': 'array', '$$description': ['Exclude packages that match the values listed in this field.', "Can container shell-style wildcards (e.g. ``'pkg.*'``)"], 'items': {'type': 'string'}}, 'include': {'type': 'array', '$$description': ['Restrict the found packages to just the ones listed in this field.', "Can container shell-style wildcards (e.g. ``'pkg.*'``)"], 'items': {'type': 'string'}}, 'namespaces': {'type': 'boolean', '$$description': ['When ``True``, directories without a ``__init__.py`` file will also', 'be scanned for :pep:`420`-style implicit namespaces']}}}, rule='additionalProperties')
        if data_keys:
            raise JsonSchemaValueException("data must not contain "+str(data_keys)+" properties", value=data, name="data", definition={'$id': '#/definitions/find-directive', 'title': "'find:' directive", 'type': 'object', 'additionalProperties': False, 'properties': {'find': {'type': 'object', '$$description': ['Dynamic `package discovery', '<https://setuptools.pypa.io/en/latest/userguide/package_discovery.html>`_.'], 'additionalProperties': False, 'properties': {'where': {'description': 'Directories to be searched for packages (Unix-style relative path)', 'type': 'array', 'items': {'type': 'string'}}, 'exclude': {'type': 'array', '$$description': ['Exclude packages that match the values listed in this field.', "Can container shell-style wildcards (e.g. ``'pkg.*'``)"], 'items': {'type': 'string'}}, 'include': {'type': 'array', '$$description': ['Restrict the found packages to just the ones listed in this field.', "Can container shell-style wildcards (e.g. ``'pkg.*'``)"], 'items': {'type': 'string'}}, 'namespaces': {'type': 'boolean', '$$description': ['When ``True``, directories without a ``__init__.py`` file will also', 'be scanned for :pep:`420`-style implicit namespaces']}}}}}, rule='additionalProperties')
    return data

def validate_https___docs_python_org_3_install(data, custom_formats={}):
    if not isinstance(data, (dict)):
        raise JsonSchemaValueException("data must be object", value=data, name="data", definition={'$schema': 'http://json-schema.org/draft-07/schema', '$id': 'https://docs.python.org/3/install/', 'title': '``tool.distutils`` table', '$$description': ['Originally, ``distutils`` allowed developers to configure arguments for', '``setup.py`` scripts via `distutils configuration files', '<https://docs.python.org/3/install/#distutils-configuration-files>`_.', '``tool.distutils`` subtables could be used with the same purpose', '(NOT CURRENTLY IMPLEMENTED).'], 'type': 'object', 'properties': {'global': {'type': 'object', 'description': 'Global options applied to all ``distutils`` commands'}}, 'patternProperties': {'.+': {'type': 'object'}}, '$comment': 'TODO: Is there a practical way of making this schema more specific?'}, rule='type')
    data_is_dict = isinstance(data, dict)
    if data_is_dict:
        data_keys = set(data.keys())
        if "global" in data_keys:
            data_keys.remove("global")
            data__global = data["global"]
            if not isinstance(data__global, (dict)):
                raise JsonSchemaValueException("data.global must be object", value=data__global, name="data.global", definition={'type': 'object', 'description': 'Global options applied to all ``distutils`` commands'}, rule='type')
        for data_key, data_val in data.items():
            if REGEX_PATTERNS['.+'].search(data_key):
                if data_key in data_keys:
                    data_keys.remove(data_key)
                if not isinstance(data_val, (dict)):
                    raise JsonSchemaValueException(""+"data.{data_key}".format(**locals())+" must be object", value=data_val, name=""+"data.{data_key}".format(**locals())+"", definition={'type': 'object'}, rule='type')
    return data

def validate_https___www_python_org_dev_peps_pep_0621(data, custom_formats={}):
    if not isinstance(data, (dict)):
        raise JsonSchemaValueException("data must be object", value=data, name="data", definition={'$schema': 'http://json-schema.org/draft-07/schema', '$id': 'https://www.python.org/dev/peps/pep-0621/', 'title': '``project`` table', '$$description': ['Data structure for the **project** table inside ``pyproject.toml``', '(as defined in :pep:`621`)'], 'type': 'object', 'properties': {'name': {'type': 'string', 'description': 'The name (primary identifier) of the project. MUST be statically defined.', 'format': 'pep508-identifier'}, 'version': {'type': 'string', 'description': 'The version of the project as supported by :pep:`440`.', 'format': 'pep440'}, 'description': {'type': 'string', '$$description': ['The `summary description of the project', '<https://packaging.python.org/specifications/core-metadata/#summary>`_']}, 'readme': {'$$description': ['`Full/detailed description of the project in the form of a README', '<https://www.python.org/dev/peps/pep-0621/#readme>`_', "with meaning similar to the one defined in `core metadata's Description", '<https://packaging.python.org/specifications/core-metadata/#description>`_'], 'oneOf': [{'type': 'string', '$$description': ['Relative path to a text file (UTF-8) containing the full description', 'of the project. If the file path ends in case-insensitive ``.md`` or', '``.rst`` suffixes, then the content-type is respectively', '``text/markdown`` or ``text/x-rst``']}, {'type': 'object', 'allOf': [{'anyOf': [{'properties': {'file': {'type': 'string', '$$description': ['Relative path to a text file containing the full description', 'of the project.']}}, 'required': ['file']}, {'properties': {'text': {'type': 'string', 'description': 'Full text describing the project.'}}, 'required': ['text']}]}, {'properties': {'content-type': {'type': 'string', '$$description': ['Content-type (:rfc:`1341`) of the full description', '(e.g. ``text/markdown``). The ``charset`` parameter is assumed', 'UTF-8 when not present.'], '$comment': 'TODO: add regex pattern or format?'}}, 'required': ['content-type']}]}]}, 'requires-python': {'type': 'string', 'format': 'pep508-versionspec', '$$description': ['`The Python version requirements of the project', '<https://packaging.python.org/specifications/core-metadata/#requires-python>`_.']}, 'license': {'description': '`Project license <https://www.python.org/dev/peps/pep-0621/#license>`_.', 'oneOf': [{'properties': {'file': {'type': 'string', '$$description': ['Relative path to the file (UTF-8) which contains the license for the', 'project.']}}, 'required': ['file']}, {'properties': {'text': {'type': 'string', '$$description': ['The license of the project whose meaning is that of the', '`License field from the core metadata', '<https://packaging.python.org/specifications/core-metadata/#license>`_.']}}, 'required': ['text']}]}, 'authors': {'type': 'array', 'items': {'$ref': '#/definitions/author'}, '$$description': ["The people or organizations considered to be the 'authors' of the project.", 'The exact meaning is open to interpretation (e.g. original or primary authors,', 'current maintainers, or owners of the package).']}, 'maintainers': {'type': 'array', 'items': {'$ref': '#/definitions/author'}, '$$description': ["The people or organizations considered to be the 'maintainers' of the project.", 'Similarly to ``authors``, the exact meaning is open to interpretation.']}, 'keywords': {'type': 'array', 'items': {'type': 'string'}, 'description': 'List of keywords to assist searching for the distribution in a larger catalog.'}, 'classifiers': {'type': 'array', 'items': {'type': 'string', 'format': 'trove-classifier', 'description': '`PyPI classifier <https://pypi.org/classifiers/>`_.'}, '$$description': ['`Trove classifiers <https://pypi.org/classifiers/>`_', 'which apply to the project.']}, 'urls': {'type': 'object', 'description': 'URLs associated with the project in the form ``label => value``.', 'additionalProperties': False, 'patternProperties': {'^.+$': {'type': 'string', 'format': 'url'}}}, 'scripts': {'$ref': '#/definitions/entry-point-group', '$$description': ['Instruct the installer to create command-line wrappers for the given', '`entry points <https://packaging.python.org/specifications/entry-points/>`_.']}, 'gui-scripts': {'$ref': '#/definitions/entry-point-group', '$$description': ['Instruct the installer to create GUI wrappers for the given', '`entry points <https://packaging.python.org/specifications/entry-points/>`_.', 'The difference between ``scripts`` and ``gui-scripts`` is only relevant in', 'Windows.']}, 'entry-points': {'$$description': ['Instruct the installer to expose the given modules/functions via', '``entry-point`` discovery mechanism (useful for plugins).', 'More information available in the `Python packaging guide', '<https://packaging.python.org/specifications/entry-points/>`_.'], 'propertyNames': {'format': 'python-entrypoint-group'}, 'additionalProperties': False, 'patternProperties': {'^.+$': {'$ref': '#/definitions/entry-point-group'}}}, 'dependencies': {'type': 'array', 'description': 'Project (mandatory) dependencies.', 'items': {'$ref': '#/definitions/dependency'}}, 'optional-dependencies': {'type': 'object', 'description': 'Optional dependency for the project', 'propertyNames': {'format': 'pep508-identifier'}, 'additionalProperties': False, 'patternProperties': {'^.+$': {'type': 'array', 'items': {'$ref': '#/definitions/dependency'}}}}, 'dynamic': {'type': 'array', '$$description': ['Specifies which fields are intentionally unspecified and expected to be', 'dynamically provided by build tools'], 'items': {'enum': ['version', 'description', 'readme', 'requires-python', 'license', 'authors', 'maintainers', 'keywords', 'classifiers', 'urls', 'scripts', 'gui-scripts', 'entry-points', 'dependencies', 'optional-dependencies']}}}, 'required': ['name'], 'if': {'not': {'required': ['version'], '$$description': ['version is statically defined in the ``version`` field']}, '$$comment': ['According to :pep:`621`:', '    If the core metadata specification lists a field as "Required", then', '    the metadata MUST specify the field statically or list it in dynamic', 'In turn, `core metadata`_ defines:', '    The required fields are: Metadata-Version, Name, Version.', '    All the other fields are optional.', 'Since ``Metadata-Version`` is defined by the build back-end, ``name`` and', '``version`` are the only mandatory information in ``pyproject.toml``.', '.. _core metadata: https://packaging.python.org/specifications/core-metadata/']}, 'then': {'properties': {'dynamic': {'contains': {'const': 'version'}, '$$description': ['version should be listed in ``dynamic``']}}}, 'definitions': {'author': {'$id': '#/definitions/author', 'title': 'Author or Maintainer', '$comment': 'https://www.python.org/dev/peps/pep-0621/#authors-maintainers', 'type': 'object', 'properties': {'name': {'type': 'string', '$$description': ['MUST be a valid email name, i.e. whatever can be put as a name, before an', 'email, in :rfc:`822`.']}, 'email': {'type': 'string', 'format': 'idn-email', 'description': 'MUST be a valid email address'}}}, 'entry-point-group': {'$id': '#/definitions/entry-point-group', 'title': 'Entry-points', 'type': 'object', '$$description': ['Entry-points are grouped together to indicate what sort of capabilities they', 'provide.', 'See the `packaging guides', '<https://packaging.python.org/specifications/entry-points/>`_', 'and `setuptools docs', '<https://setuptools.pypa.io/en/latest/userguide/entry_point.html>`_', 'for more information.'], 'propertyNames': {'format': 'python-entrypoint-name'}, 'additionalProperties': False, 'patternProperties': {'^.+$': {'type': 'string', '$$description': ['Reference to a Python object. It is either in the form', '``importable.module``, or ``importable.module:object.attr``.'], 'format': 'python-entrypoint-reference', '$comment': 'https://packaging.python.org/specifications/entry-points/'}}}, 'dependency': {'$id': '#/definitions/dependency', 'title': 'Dependency', 'type': 'string', 'description': 'Project dependency specification according to PEP 508', 'format': 'pep508'}}}, rule='type')
    data_is_dict = isinstance(data, dict)
    if data_is_dict:
        data_len = len(data)
        if not all(prop in data for prop in ['name']):
            raise JsonSchemaValueException("data must contain ['name'] properties", value=data, name="data", definition={'$schema': 'http://json-schema.org/draft-07/schema', '$id': 'https://www.python.org/dev/peps/pep-0621/', 'title': '``project`` table', '$$description': ['Data structure for the **project** table inside ``pyproject.toml``', '(as defined in :pep:`621`)'], 'type': 'object', 'properties': {'name': {'type': 'string', 'description': 'The name (primary identifier) of the project. MUST be statically defined.', 'format': 'pep508-identifier'}, 'version': {'type': 'string', 'description': 'The version of the project as supported by :pep:`440`.', 'format': 'pep440'}, 'description': {'type': 'string', '$$description': ['The `summary description of the project', '<https://packaging.python.org/specifications/core-metadata/#summary>`_']}, 'readme': {'$$description': ['`Full/detailed description of the project in the form of a README', '<https://www.python.org/dev/peps/pep-0621/#readme>`_', "with meaning similar to the one defined in `core metadata's Description", '<https://packaging.python.org/specifications/core-metadata/#description>`_'], 'oneOf': [{'type': 'string', '$$description': ['Relative path to a text file (UTF-8) containing the full description', 'of the project. If the file path ends in case-insensitive ``.md`` or', '``.rst`` suffixes, then the content-type is respectively', '``text/markdown`` or ``text/x-rst``']}, {'type': 'object', 'allOf': [{'anyOf': [{'properties': {'file': {'type': 'string', '$$description': ['Relative path to a text file containing the full description', 'of the project.']}}, 'required': ['file']}, {'properties': {'text': {'type': 'string', 'description': 'Full text describing the project.'}}, 'required': ['text']}]}, {'properties': {'content-type': {'type': 'string', '$$description': ['Content-type (:rfc:`1341`) of the full description', '(e.g. ``text/markdown``). The ``charset`` parameter is assumed', 'UTF-8 when not present.'], '$comment': 'TODO: add regex pattern or format?'}}, 'required': ['content-type']}]}]}, 'requires-python': {'type': 'string', 'format': 'pep508-versionspec', '$$description': ['`The Python version requirements of the project', '<https://packaging.python.org/specifications/core-metadata/#requires-python>`_.']}, 'license': {'description': '`Project license <https://www.python.org/dev/peps/pep-0621/#license>`_.', 'oneOf': [{'properties': {'file': {'type': 'string', '$$description': ['Relative path to the file (UTF-8) which contains the license for the', 'project.']}}, 'required': ['file']}, {'properties': {'text': {'type': 'string', '$$description': ['The license of the project whose meaning is that of the', '`License field from the core metadata', '<https://packaging.python.org/specifications/core-metadata/#license>`_.']}}, 'required': ['text']}]}, 'authors': {'type': 'array', 'items': {'$ref': '#/definitions/author'}, '$$description': ["The people or organizations considered to be the 'authors' of the project.", 'The exact meaning is open to interpretation (e.g. original or primary authors,', 'current maintainers, or owners of the package).']}, 'maintainers': {'type': 'array', 'items': {'$ref': '#/definitions/author'}, '$$description': ["The people or organizations considered to be the 'maintainers' of the project.", 'Similarly to ``authors``, the exact meaning is open to interpretation.']}, 'keywords': {'type': 'array', 'items': {'type': 'string'}, 'description': 'List of keywords to assist searching for the distribution in a larger catalog.'}, 'classifiers': {'type': 'array', 'items': {'type': 'string', 'format': 'trove-classifier', 'description': '`PyPI classifier <https://pypi.org/classifiers/>`_.'}, '$$description': ['`Trove classifiers <https://pypi.org/classifiers/>`_', 'which apply to the project.']}, 'urls': {'type': 'object', 'description': 'URLs associated with the project in the form ``label => value``.', 'additionalProperties': False, 'patternProperties': {'^.+$': {'type': 'string', 'format': 'url'}}}, 'scripts': {'$ref': '#/definitions/entry-point-group', '$$description': ['Instruct the installer to create command-line wrappers for the given', '`entry points <https://packaging.python.org/specifications/entry-points/>`_.']}, 'gui-scripts': {'$ref': '#/definitions/entry-point-group', '$$description': ['Instruct the installer to create GUI wrappers for the given', '`entry points <https://packaging.python.org/specifications/entry-points/>`_.', 'The difference between ``scripts`` and ``gui-scripts`` is only relevant in', 'Windows.']}, 'entry-points': {'$$description': ['Instruct the installer to expose the given modules/functions via', '``entry-point`` discovery mechanism (useful for plugins).', 'More information available in the `Python packaging guide', '<https://packaging.python.org/specifications/entry-points/>`_.'], 'propertyNames': {'format': 'python-entrypoint-group'}, 'additionalProperties': False, 'patternProperties': {'^.+$': {'$ref': '#/definitions/entry-point-group'}}}, 'dependencies': {'type': 'array', 'description': 'Project (mandatory) dependencies.', 'items': {'$ref': '#/definitions/dependency'}}, 'optional-dependencies': {'type': 'object', 'description': 'Optional dependency for the project', 'propertyNames': {'format': 'pep508-identifier'}, 'additionalProperties': False, 'patternProperties': {'^.+$': {'type': 'array', 'items': {'$ref': '#/definitions/dependency'}}}}, 'dynamic': {'type': 'array', '$$description': ['Specifies which fields are intentionally unspecified and expected to be', 'dynamically provided by build tools'], 'items': {'enum': ['version', 'description', 'readme', 'requires-python', 'license', 'authors', 'maintainers', 'keywords', 'classifiers', 'urls', 'scripts', 'gui-scripts', 'entry-points', 'dependencies', 'optional-dependencies']}}}, 'required': ['name'], 'if': {'not': {'required': ['version'], '$$description': ['version is statically defined in the ``version`` field']}, '$$comment': ['According to :pep:`621`:', '    If the core metadata specification lists a field as "Required", then', '    the metadata MUST specify the field statically or list it in dynamic', 'In turn, `core metadata`_ defines:', '    The required fields are: Metadata-Version, Name, Version.', '    All the other fields are optional.', 'Since ``Metadata-Version`` is defined by the build back-end, ``name`` and', '``version`` are the only mandatory information in ``pyproject.toml``.', '.. _core metadata: https://packaging.python.org/specifications/core-metadata/']}, 'then': {'properties': {'dynamic': {'contains': {'const': 'version'}, '$$description': ['version should be listed in ``dynamic``']}}}, 'definitions': {'author': {'$id': '#/definitions/author', 'title': 'Author or Maintainer', '$comment': 'https://www.python.org/dev/peps/pep-0621/#authors-maintainers', 'type': 'object', 'properties': {'name': {'type': 'string', '$$description': ['MUST be a valid email name, i.e. whatever can be put as a name, before an', 'email, in :rfc:`822`.']}, 'email': {'type': 'string', 'format': 'idn-email', 'description': 'MUST be a valid email address'}}}, 'entry-point-group': {'$id': '#/definitions/entry-point-group', 'title': 'Entry-points', 'type': 'object', '$$description': ['Entry-points are grouped together to indicate what sort of capabilities they', 'provide.', 'See the `packaging guides', '<https://packaging.python.org/specifications/entry-points/>`_', 'and `setuptools docs', '<https://setuptools.pypa.io/en/latest/userguide/entry_point.html>`_', 'for more information.'], 'propertyNames': {'format': 'python-entrypoint-name'}, 'additionalProperties': False, 'patternProperties': {'^.+$': {'type': 'string', '$$description': ['Reference to a Python object. It is either in the form', '``importable.module``, or ``importable.module:object.attr``.'], 'format': 'python-entrypoint-reference', '$comment': 'https://packaging.python.org/specifications/entry-points/'}}}, 'dependency': {'$id': '#/definitions/dependency', 'title': 'Dependency', 'type': 'string', 'description': 'Project dependency specification according to PEP 508', 'format': 'pep508'}}}, rule='required')
        data_keys = set(data.keys())
        if "name" in data_keys:
            data_keys.remove("name")
            data__name = data["name"]
            if not isinstance(data__name, (str)):
                raise JsonSchemaValueException("data.name must be string", value=data__name, name="data.name", definition={'type': 'string', 'description': 'The name (primary identifier) of the project. MUST be statically defined.', 'format': 'pep508-identifier'}, rule='type')
            if isinstance(data__name, str):
                if not custom_formats["pep508-identifier"](data__name):
                    raise JsonSchemaValueException("data.name must be pep508-identifier", value=data__name, name="data.name", definition={'type': 'string', 'description': 'The name (primary identifier) of the project. MUST be statically defined.', 'format': 'pep508-identifier'}, rule='format')
        if "version" in data_keys:
            data_keys.remove("version")
            data__version = data["version"]
            if not isinstance(data__version, (str)):
                raise JsonSchemaValueException("data.version must be string", value=data__version, name="data.version", definition={'type': 'string', 'description': 'The version of the project as supported by :pep:`440`.', 'format': 'pep440'}, rule='type')
            if isinstance(data__version, str):
                if not custom_formats["pep440"](data__version):
                    raise JsonSchemaValueException("data.version must be pep440", value=data__version, name="data.version", definition={'type': 'string', 'description': 'The version of the project as supported by :pep:`440`.', 'format': 'pep440'}, rule='format')
        if "description" in data_keys:
            data_keys.remove("description")
            data__description = data["description"]
            if not isinstance(data__description, (str)):
                raise JsonSchemaValueException("data.description must be string", value=data__description, name="data.description", definition={'type': 'string', '$$description': ['The `summary description of the project', '<https://packaging.python.org/specifications/core-metadata/#summary>`_']}, rule='type')
        if "readme" in data_keys:
            data_keys.remove("readme")
            data__readme = data["readme"]
            data__readme_one_of_count8 = 0
            if data__readme_one_of_count8 < 2:
                try:
                    if not isinstance(data__readme, (str)):
                        raise JsonSchemaValueException("data.readme must be string", value=data__readme, name="data.readme", definition={'type': 'string', '$$description': ['Relative path to a text file (UTF-8) containing the full description', 'of the project. If the file path ends in case-insensitive ``.md`` or', '``.rst`` suffixes, then the content-type is respectively', '``text/markdown`` or ``text/x-rst``']}, rule='type')
                    data__readme_one_of_count8 += 1
                except JsonSchemaValueException: pass
            if data__readme_one_of_count8 < 2:
                try:
                    if not isinstance(data__readme, (dict)):
                        raise JsonSchemaValueException("data.readme must be object", value=data__readme, name="data.readme", definition={'type': 'object', 'allOf': [{'anyOf': [{'properties': {'file': {'type': 'string', '$$description': ['Relative path to a text file containing the full description', 'of the project.']}}, 'required': ['file']}, {'properties': {'text': {'type': 'string', 'description': 'Full text describing the project.'}}, 'required': ['text']}]}, {'properties': {'content-type': {'type': 'string', '$$description': ['Content-type (:rfc:`1341`) of the full description', '(e.g. ``text/markdown``). The ``charset`` parameter is assumed', 'UTF-8 when not present.'], '$comment': 'TODO: add regex pattern or format?'}}, 'required': ['content-type']}]}, rule='type')
                    data__readme_any_of_count9 = 0
                    if not data__readme_any_of_count9:
                        try:
                            data__readme_is_dict = isinstance(data__readme, dict)
                            if data__readme_is_dict:
                                data__readme_len = len(data__readme)
                                if not all(prop in data__readme for prop in ['file']):
                                    raise JsonSchemaValueException("data.readme must contain ['file'] properties", value=data__readme, name="data.readme", definition={'properties': {'file': {'type': 'string', '$$description': ['Relative path to a text file containing the full description', 'of the project.']}}, 'required': ['file']}, rule='required')
                                data__readme_keys = set(data__readme.keys())
                                if "file" in data__readme_keys:
                                    data__readme_keys.remove("file")
                                    data__readme__file = data__readme["file"]
                                    if not isinstance(data__readme__file, (str)):
                                        raise JsonSchemaValueException("data.readme.file must be string", value=data__readme__file, name="data.readme.file", definition={'type': 'string', '$$description': ['Relative path to a text file containing the full description', 'of the project.']}, rule='type')
                            data__readme_any_of_count9 += 1
                        except JsonSchemaValueException: pass
                    if not data__readme_any_of_count9:
                        try:
                            data__readme_is_dict = isinstance(data__readme, dict)
                            if data__readme_is_dict:
                                data__readme_len = len(data__readme)
                                if not all(prop in data__readme for prop in ['text']):
                                    raise JsonSchemaValueException("data.readme must contain ['text'] properties", value=data__readme, name="data.readme", definition={'properties': {'text': {'type': 'string', 'description': 'Full text describing the project.'}}, 'required': ['text']}, rule='required')
                                data__readme_keys = set(data__readme.keys())
                                if "text" in data__readme_keys:
                                    data__readme_keys.remove("text")
                                    data__readme__text = data__readme["text"]
                                    if not isinstance(data__readme__text, (str)):
                                        raise JsonSchemaValueException("data.readme.text must be string", value=data__readme__text, name="data.readme.text", definition={'type': 'string', 'description': 'Full text describing the project.'}, rule='type')
                            data__readme_any_of_count9 += 1
                        except JsonSchemaValueException: pass
                    if not data__readme_any_of_count9:
                        raise JsonSchemaValueException("data.readme must be valid by one of anyOf definition", value=data__readme, name="data.readme", definition={'anyOf': [{'properties': {'file': {'type': 'string', '$$description': ['Relative path to a text file containing the full description', 'of the project.']}}, 'required': ['file']}, {'properties': {'text': {'type': 'string', 'description': 'Full text describing the project.'}}, 'required': ['text']}]}, rule='anyOf')
                    data__readme_is_dict = isinstance(data__readme, dict)
                    if data__readme_is_dict:
                        data__readme_len = len(data__readme)
                        if not all(prop in data__readme for prop in ['content-type']):
                            raise JsonSchemaValueException("data.readme must contain ['content-type'] properties", value=data__readme, name="data.readme", definition={'properties': {'content-type': {'type': 'string', '$$description': ['Content-type (:rfc:`1341`) of the full description', '(e.g. ``text/markdown``). The ``charset`` parameter is assumed', 'UTF-8 when not present.'], '$comment': 'TODO: add regex pattern or format?'}}, 'required': ['content-type']}, rule='required')
                        data__readme_keys = set(data__readme.keys())
                        if "content-type" in data__readme_keys:
                            data__readme_keys.remove("content-type")
                            data__readme__contenttype = data__readme["content-type"]
                            if not isinstance(data__readme__contenttype, (str)):
                                raise JsonSchemaValueException("data.readme.content-type must be string", value=data__readme__contenttype, name="data.readme.content-type", definition={'type': 'string', '$$description': ['Content-type (:rfc:`1341`) of the full description', '(e.g. ``text/markdown``). The ``charset`` parameter is assumed', 'UTF-8 when not present.'], '$comment': 'TODO: add regex pattern or format?'}, rule='type')
                    data__readme_one_of_count8 += 1
                except JsonSchemaValueException: pass
            if data__readme_one_of_count8 != 1:
                raise JsonSchemaValueException("data.readme must be valid exactly by one of oneOf definition", value=data__readme, name="data.readme", definition={'$$description': ['`Full/detailed description of the project in the form of a README', '<https://www.python.org/dev/peps/pep-0621/#readme>`_', "with meaning similar to the one defined in `core metadata's Description", '<https://packaging.python.org/specifications/core-metadata/#description>`_'], 'oneOf': [{'type': 'string', '$$description': ['Relative path to a text file (UTF-8) containing the full description', 'of the project. If the file path ends in case-insensitive ``.md`` or', '``.rst`` suffixes, then the content-type is respectively', '``text/markdown`` or ``text/x-rst``']}, {'type': 'object', 'allOf': [{'anyOf': [{'properties': {'file': {'type': 'string', '$$description': ['Relative path to a text file containing the full description', 'of the project.']}}, 'required': ['file']}, {'properties': {'text': {'type': 'string', 'description': 'Full text describing the project.'}}, 'required': ['text']}]}, {'properties': {'content-type': {'type': 'string', '$$description': ['Content-type (:rfc:`1341`) of the full description', '(e.g. ``text/markdown``). The ``charset`` parameter is assumed', 'UTF-8 when not present.'], '$comment': 'TODO: add regex pattern or format?'}}, 'required': ['content-type']}]}]}, rule='oneOf')
        if "requires-python" in data_keys:
            data_keys.remove("requires-python")
            data__requirespython = data["requires-python"]
            if not isinstance(data__requirespython, (str)):
                raise JsonSchemaValueException("data.requires-python must be string", value=data__requirespython, name="data.requires-python", definition={'type': 'string', 'format': 'pep508-versionspec', '$$description': ['`The Python version requirements of the project', '<https://packaging.python.org/specifications/core-metadata/#requires-python>`_.']}, rule='type')
            if isinstance(data__requirespython, str):
                if not custom_formats["pep508-versionspec"](data__requirespython):
                    raise JsonSchemaValueException("data.requires-python must be pep508-versionspec", value=data__requirespython, name="data.requires-python", definition={'type': 'string', 'format': 'pep508-versionspec', '$$description': ['`The Python version requirements of the project', '<https://packaging.python.org/specifications/core-metadata/#requires-python>`_.']}, rule='format')
        if "license" in data_keys:
            data_keys.remove("license")
            data__license = data["license"]
            data__license_one_of_count10 = 0
            if data__license_one_of_count10 < 2:
                try:
                    data__license_is_dict = isinstance(data__license, dict)
                    if data__license_is_dict:
                        data__license_len = len(data__license)
                        if not all(prop in data__license for prop in ['file']):
                            raise JsonSchemaValueException("data.license must contain ['file'] properties", value=data__license, name="data.license", definition={'properties': {'file': {'type': 'string', '$$description': ['Relative path to the file (UTF-8) which contains the license for the', 'project.']}}, 'required': ['file']}, rule='required')
                        data__license_keys = set(data__license.keys())
                        if "file" in data__license_keys:
                            data__license_keys.remove("file")
                            data__license__file = data__license["file"]
                            if not isinstance(data__license__file, (str)):
                                raise JsonSchemaValueException("data.license.file must be string", value=data__license__file, name="data.license.file", definition={'type': 'string', '$$description': ['Relative path to the file (UTF-8) which contains the license for the', 'project.']}, rule='type')
                    data__license_one_of_count10 += 1
                except JsonSchemaValueException: pass
            if data__license_one_of_count10 < 2:
                try:
                    data__license_is_dict = isinstance(data__license, dict)
                    if data__license_is_dict:
                        data__license_len = len(data__license)
                        if not all(prop in data__license for prop in ['text']):
                            raise JsonSchemaValueException("data.license must contain ['text'] properties", value=data__license, name="data.license", definition={'properties': {'text': {'type': 'string', '$$description': ['The license of the project whose meaning is that of the', '`License field from the core metadata', '<https://packaging.python.org/specifications/core-metadata/#license>`_.']}}, 'required': ['text']}, rule='required')
                        data__license_keys = set(data__license.keys())
                        if "text" in data__license_keys:
                            data__license_keys.remove("text")
                            data__license__text = data__license["text"]
                            if not isinstance(data__license__text, (str)):
                                raise JsonSchemaValueException("data.license.text must be string", value=data__license__text, name="data.license.text", definition={'type': 'string', '$$description': ['The license of the project whose meaning is that of the', '`License field from the core metadata', '<https://packaging.python.org/specifications/core-metadata/#license>`_.']}, rule='type')
                    data__license_one_of_count10 += 1
                except JsonSchemaValueException: pass
            if data__license_one_of_count10 != 1:
                raise JsonSchemaValueException("data.license must be valid exactly by one of oneOf definition", value=data__license, name="data.license", definition={'description': '`Project license <https://www.python.org/dev/peps/pep-0621/#license>`_.', 'oneOf': [{'properties': {'file': {'type': 'string', '$$description': ['Relative path to the file (UTF-8) which contains the license for the', 'project.']}}, 'required': ['file']}, {'properties': {'text': {'type': 'string', '$$description': ['The license of the project whose meaning is that of the', '`License field from the core metadata', '<https://packaging.python.org/specifications/core-metadata/#license>`_.']}}, 'required': ['text']}]}, rule='oneOf')
        if "authors" in data_keys:
            data_keys.remove("authors")
            data__authors = data["authors"]
            if not isinstance(data__authors, (list, tuple)):
                raise JsonSchemaValueException("data.authors must be array", value=data__authors, name="data.authors", definition={'type': 'array', 'items': {'$ref': '#/definitions/author'}, '$$description': ["The people or organizations considered to be the 'authors' of the project.", 'The exact meaning is open to interpretation (e.g. original or primary authors,', 'current maintainers, or owners of the package).']}, rule='type')
            data__authors_is_list = isinstance(data__authors, (list, tuple))
            if data__authors_is_list:
                data__authors_len = len(data__authors)
                for data__authors_x, data__authors_item in enumerate(data__authors):
                    validate_https___www_python_org_dev_peps_pep_0621___definitions_author(data__authors_item, custom_formats)
        if "maintainers" in data_keys:
            data_keys.remove("maintainers")
            data__maintainers = data["maintainers"]
            if not isinstance(data__maintainers, (list, tuple)):
                raise JsonSchemaValueException("data.maintainers must be array", value=data__maintainers, name="data.maintainers", definition={'type': 'array', 'items': {'$ref': '#/definitions/author'}, '$$description': ["The people or organizations considered to be the 'maintainers' of the project.", 'Similarly to ``authors``, the exact meaning is open to interpretation.']}, rule='type')
            data__maintainers_is_list = isinstance(data__maintainers, (list, tuple))
            if data__maintainers_is_list:
                data__maintainers_len = len(data__maintainers)
                for data__maintainers_x, data__maintainers_item in enumerate(data__maintainers):
                    validate_https___www_python_org_dev_peps_pep_0621___definitions_author(data__maintainers_item, custom_formats)
        if "keywords" in data_keys:
            data_keys.remove("keywords")
            data__keywords = data["keywords"]
            if not isinstance(data__keywords, (list, tuple)):
                raise JsonSchemaValueException("data.keywords must be array", value=data__keywords, name="data.keywords", definition={'type': 'array', 'items': {'type': 'string'}, 'description': 'List of keywords to assist searching for the distribution in a larger catalog.'}, rule='type')
            data__keywords_is_list = isinstance(data__keywords, (list, tuple))
            if data__keywords_is_list:
                data__keywords_len = len(data__keywords)
                for data__keywords_x, data__keywords_item in enumerate(data__keywords):
                    if not isinstance(data__keywords_item, (str)):
                        raise JsonSchemaValueException(""+"data.keywords[{data__keywords_x}]".format(**locals())+" must be string", value=data__keywords_item, name=""+"data.keywords[{data__keywords_x}]".format(**locals())+"", definition={'type': 'string'}, rule='type')
        if "classifiers" in data_keys:
            data_keys.remove("classifiers")
            data__classifiers = data["classifiers"]
            if not isinstance(data__classifiers, (list, tuple)):
                raise JsonSchemaValueException("data.classifiers must be array", value=data__classifiers, name="data.classifiers", definition={'type': 'array', 'items': {'type': 'string', 'format': 'trove-classifier', 'description': '`PyPI classifier <https://pypi.org/classifiers/>`_.'}, '$$description': ['`Trove classifiers <https://pypi.org/classifiers/>`_', 'which apply to the project.']}, rule='type')
            data__classifiers_is_list = isinstance(data__classifiers, (list, tuple))
            if data__classifiers_is_list:
                data__classifiers_len = len(data__classifiers)
                for data__classifiers_x, data__classifiers_item in enumerate(data__classifiers):
                    if not isinstance(data__classifiers_item, (str)):
                        raise JsonSchemaValueException(""+"data.classifiers[{data__classifiers_x}]".format(**locals())+" must be string", value=data__classifiers_item, name=""+"data.classifiers[{data__classifiers_x}]".format(**locals())+"", definition={'type': 'string', 'format': 'trove-classifier', 'description': '`PyPI classifier <https://pypi.org/classifiers/>`_.'}, rule='type')
                    if isinstance(data__classifiers_item, str):
                        if not custom_formats["trove-classifier"](data__classifiers_item):
                            raise JsonSchemaValueException(""+"data.classifiers[{data__classifiers_x}]".format(**locals())+" must be trove-classifier", value=data__classifiers_item, name=""+"data.classifiers[{data__classifiers_x}]".format(**locals())+"", definition={'type': 'string', 'format': 'trove-classifier', 'description': '`PyPI classifier <https://pypi.org/classifiers/>`_.'}, rule='format')
        if "urls" in data_keys:
            data_keys.remove("urls")
            data__urls = data["urls"]
            if not isinstance(data__urls, (dict)):
                raise JsonSchemaValueException("data.urls must be object", value=data__urls, name="data.urls", definition={'type': 'object', 'description': 'URLs associated with the project in the form ``label => value``.', 'additionalProperties': False, 'patternProperties': {'^.+$': {'type': 'string', 'format': 'url'}}}, rule='type')
            data__urls_is_dict = isinstance(data__urls, dict)
            if data__urls_is_dict:
                data__urls_keys = set(data__urls.keys())
                for data__urls_key, data__urls_val in data__urls.items():
                    if REGEX_PATTERNS['^.+$'].search(data__urls_key):
                        if data__urls_key in data__urls_keys:
                            data__urls_keys.remove(data__urls_key)
                        if not isinstance(data__urls_val, (str)):
                            raise JsonSchemaValueException(""+"data.urls.{data__urls_key}".format(**locals())+" must be string", value=data__urls_val, name=""+"data.urls.{data__urls_key}".format(**locals())+"", definition={'type': 'string', 'format': 'url'}, rule='type')
                        if isinstance(data__urls_val, str):
                            if not custom_formats["url"](data__urls_val):
                                raise JsonSchemaValueException(""+"data.urls.{data__urls_key}".format(**locals())+" must be url", value=data__urls_val, name=""+"data.urls.{data__urls_key}".format(**locals())+"", definition={'type': 'string', 'format': 'url'}, rule='format')
                if data__urls_keys:
                    raise JsonSchemaValueException("data.urls must not contain "+str(data__urls_keys)+" properties", value=data__urls, name="data.urls", definition={'type': 'object', 'description': 'URLs associated with the project in the form ``label => value``.', 'additionalProperties': False, 'patternProperties': {'^.+$': {'type': 'string', 'format': 'url'}}}, rule='additionalProperties')
        if "scripts" in data_keys:
            data_keys.remove("scripts")
            data__scripts = data["scripts"]
            validate_https___www_python_org_dev_peps_pep_0621___definitions_entry_point_group(data__scripts, custom_formats)
        if "gui-scripts" in data_keys:
            data_keys.remove("gui-scripts")
            data__guiscripts = data["gui-scripts"]
            validate_https___www_python_org_dev_peps_pep_0621___definitions_entry_point_group(data__guiscripts, custom_formats)
        if "entry-points" in data_keys:
            data_keys.remove("entry-points")
            data__entrypoints = data["entry-points"]
            data__entrypoints_is_dict = isinstance(data__entrypoints, dict)
            if data__entrypoints_is_dict:
                data__entrypoints_keys = set(data__entrypoints.keys())
                for data__entrypoints_key, data__entrypoints_val in data__entrypoints.items():
                    if REGEX_PATTERNS['^.+$'].search(data__entrypoints_key):
                        if data__entrypoints_key in data__entrypoints_keys:
                            data__entrypoints_keys.remove(data__entrypoints_key)
                        validate_https___www_python_org_dev_peps_pep_0621___definitions_entry_point_group(data__entrypoints_val, custom_formats)
                if data__entrypoints_keys:
                    raise JsonSchemaValueException("data.entry-points must not contain "+str(data__entrypoints_keys)+" properties", value=data__entrypoints, name="data.entry-points", definition={'$$description': ['Instruct the installer to expose the given modules/functions via', '``entry-point`` discovery mechanism (useful for plugins).', 'More information available in the `Python packaging guide', '<https://packaging.python.org/specifications/entry-points/>`_.'], 'propertyNames': {'format': 'python-entrypoint-group'}, 'additionalProperties': False, 'patternProperties': {'^.+$': {'$ref': '#/definitions/entry-point-group'}}}, rule='additionalProperties')
                data__entrypoints_len = len(data__entrypoints)
                if data__entrypoints_len != 0:
                    data__entrypoints_property_names = True
                    for data__entrypoints_key in data__entrypoints:
                        try:
                            if isinstance(data__entrypoints_key, str):
                                if not custom_formats["python-entrypoint-group"](data__entrypoints_key):
                                    raise JsonSchemaValueException("data.entry-points must be python-entrypoint-group", value=data__entrypoints_key, name="data.entry-points", definition={'format': 'python-entrypoint-group'}, rule='format')
                        except JsonSchemaValueException:
                            data__entrypoints_property_names = False
                    if not data__entrypoints_property_names:
                        raise JsonSchemaValueException("data.entry-points must be named by propertyName definition", value=data__entrypoints, name="data.entry-points", definition={'$$description': ['Instruct the installer to expose the given modules/functions via', '``entry-point`` discovery mechanism (useful for plugins).', 'More information available in the `Python packaging guide', '<https://packaging.python.org/specifications/entry-points/>`_.'], 'propertyNames': {'format': 'python-entrypoint-group'}, 'additionalProperties': False, 'patternProperties': {'^.+$': {'$ref': '#/definitions/entry-point-group'}}}, rule='propertyNames')
        if "dependencies" in data_keys:
            data_keys.remove("dependencies")
            data__dependencies = data["dependencies"]
            if not isinstance(data__dependencies, (list, tuple)):
                raise JsonSchemaValueException("data.dependencies must be array", value=data__dependencies, name="data.dependencies", definition={'type': 'array', 'description': 'Project (mandatory) dependencies.', 'items': {'$ref': '#/definitions/dependency'}}, rule='type')
            data__dependencies_is_list = isinstance(data__dependencies, (list, tuple))
            if data__dependencies_is_list:
                data__dependencies_len = len(data__dependencies)
                for data__dependencies_x, data__dependencies_item in enumerate(data__dependencies):
                    validate_https___www_python_org_dev_peps_pep_0621___definitions_dependency(data__dependencies_item, custom_formats)
        if "optional-dependencies" in data_keys:
            data_keys.remove("optional-dependencies")
            data__optionaldependencies = data["optional-dependencies"]
            if not isinstance(data__optionaldependencies, (dict)):
                raise JsonSchemaValueException("data.optional-dependencies must be object", value=data__optionaldependencies, name="data.optional-dependencies", definition={'type': 'object', 'description': 'Optional dependency for the project', 'propertyNames': {'format': 'pep508-identifier'}, 'additionalProperties': False, 'patternProperties': {'^.+$': {'type': 'array', 'items': {'$ref': '#/definitions/dependency'}}}}, rule='type')
            data__optionaldependencies_is_dict = isinstance(data__optionaldependencies, dict)
            if data__optionaldependencies_is_dict:
                data__optionaldependencies_keys = set(data__optionaldependencies.keys())
                for data__optionaldependencies_key, data__optionaldependencies_val in data__optionaldependencies.items():
                    if REGEX_PATTERNS['^.+$'].search(data__optionaldependencies_key):
                        if data__optionaldependencies_key in data__optionaldependencies_keys:
                            data__optionaldependencies_keys.remove(data__optionaldependencies_key)
                        if not isinstance(data__optionaldependencies_val, (list, tuple)):
                            raise JsonSchemaValueException(""+"data.optional-dependencies.{data__optionaldependencies_key}".format(**locals())+" must be array", value=data__optionaldependencies_val, name=""+"data.optional-dependencies.{data__optionaldependencies_key}".format(**locals())+"", definition={'type': 'array', 'items': {'$ref': '#/definitions/dependency'}}, rule='type')
                        data__optionaldependencies_val_is_list = isinstance(data__optionaldependencies_val, (list, tuple))
                        if data__optionaldependencies_val_is_list:
                            data__optionaldependencies_val_len = len(data__optionaldependencies_val)
                            for data__optionaldependencies_val_x, data__optionaldependencies_val_item in enumerate(data__optionaldependencies_val):
                                validate_https___www_python_org_dev_peps_pep_0621___definitions_dependency(data__optionaldependencies_val_item, custom_formats)
                if data__optionaldependencies_keys:
                    raise JsonSchemaValueException("data.optional-dependencies must not contain "+str(data__optionaldependencies_keys)+" properties", value=data__optionaldependencies, name="data.optional-dependencies", definition={'type': 'object', 'description': 'Optional dependency for the project', 'propertyNames': {'format': 'pep508-identifier'}, 'additionalProperties': False, 'patternProperties': {'^.+$': {'type': 'array', 'items': {'$ref': '#/definitions/dependency'}}}}, rule='additionalProperties')
                data__optionaldependencies_len = len(data__optionaldependencies)
                if data__optionaldependencies_len != 0:
                    data__optionaldependencies_property_names = True
                    for data__optionaldependencies_key in data__optionaldependencies:
                        try:
                            if isinstance(data__optionaldependencies_key, str):
                                if not custom_formats["pep508-identifier"](data__optionaldependencies_key):
                                    raise JsonSchemaValueException("data.optional-dependencies must be pep508-identifier", value=data__optionaldependencies_key, name="data.optional-dependencies", definition={'format': 'pep508-identifier'}, rule='format')
                        except JsonSchemaValueException:
                            data__optionaldependencies_property_names = False
                    if not data__optionaldependencies_property_names:
                        raise JsonSchemaValueException("data.optional-dependencies must be named by propertyName definition", value=data__optionaldependencies, name="data.optional-dependencies", definition={'type': 'object', 'description': 'Optional dependency for the project', 'propertyNames': {'format': 'pep508-identifier'}, 'additionalProperties': False, 'patternProperties': {'^.+$': {'type': 'array', 'items': {'$ref': '#/definitions/dependency'}}}}, rule='propertyNames')
        if "dynamic" in data_keys:
            data_keys.remove("dynamic")
            data__dynamic = data["dynamic"]
            if not isinstance(data__dynamic, (list, tuple)):
                raise JsonSchemaValueException("data.dynamic must be array", value=data__dynamic, name="data.dynamic", definition={'type': 'array', '$$description': ['Specifies which fields are intentionally unspecified and expected to be', 'dynamically provided by build tools'], 'items': {'enum': ['version', 'description', 'readme', 'requires-python', 'license', 'authors', 'maintainers', 'keywords', 'classifiers', 'urls', 'scripts', 'gui-scripts', 'entry-points', 'dependencies', 'optional-dependencies']}}, rule='type')
            data__dynamic_is_list = isinstance(data__dynamic, (list, tuple))
            if data__dynamic_is_list:
                data__dynamic_len = len(data__dynamic)
                for data__dynamic_x, data__dynamic_item in enumerate(data__dynamic):
                    if data__dynamic_item not in ['version', 'description', 'readme', 'requires-python', 'license', 'authors', 'maintainers', 'keywords', 'classifiers', 'urls', 'scripts', 'gui-scripts', 'entry-points', 'dependencies', 'optional-dependencies']:
                        raise JsonSchemaValueException(""+"data.dynamic[{data__dynamic_x}]".format(**locals())+" must be one of ['version', 'description', 'readme', 'requires-python', 'license', 'authors', 'maintainers', 'keywords', 'classifiers', 'urls', 'scripts', 'gui-scripts', 'entry-points', 'dependencies', 'optional-dependencies']", value=data__dynamic_item, name=""+"data.dynamic[{data__dynamic_x}]".format(**locals())+"", definition={'enum': ['version', 'description', 'readme', 'requires-python', 'license', 'authors', 'maintainers', 'keywords', 'classifiers', 'urls', 'scripts', 'gui-scripts', 'entry-points', 'dependencies', 'optional-dependencies']}, rule='enum')
    try:
        try:
            data_is_dict = isinstance(data, dict)
            if data_is_dict:
                data_len = len(data)
                if not all(prop in data for prop in ['version']):
                    raise JsonSchemaValueException("data must contain ['version'] properties", value=data, name="data", definition={'required': ['version'], '$$description': ['version is statically defined in the ``version`` field']}, rule='required')
        except JsonSchemaValueException: pass
        else:
            raise JsonSchemaValueException("data must not be valid by not definition", value=data, name="data", definition={'not': {'required': ['version'], '$$description': ['version is statically defined in the ``version`` field']}, '$$comment': ['According to :pep:`621`:', '    If the core metadata specification lists a field as "Required", then', '    the metadata MUST specify the field statically or list it in dynamic', 'In turn, `core metadata`_ defines:', '    The required fields are: Metadata-Version, Name, Version.', '    All the other fields are optional.', 'Since ``Metadata-Version`` is defined by the build back-end, ``name`` and', '``version`` are the only mandatory information in ``pyproject.toml``.', '.. _core metadata: https://packaging.python.org/specifications/core-metadata/']}, rule='not')
    except JsonSchemaValueException:
        pass
    else:
        data_is_dict = isinstance(data, dict)
        if data_is_dict:
            data_keys = set(data.keys())
            if "dynamic" in data_keys:
                data_keys.remove("dynamic")
                data__dynamic = data["dynamic"]
                data__dynamic_is_list = isinstance(data__dynamic, (list, tuple))
                if data__dynamic_is_list:
                    data__dynamic_contains = False
                    for data__dynamic_key in data__dynamic:
                        try:
                            if data__dynamic_key != "version":
                                raise JsonSchemaValueException("data.dynamic must be same as const definition: version", value=data__dynamic_key, name="data.dynamic", definition={'const': 'version'}, rule='const')
                            data__dynamic_contains = True
                            break
                        except JsonSchemaValueException: pass
                    if not data__dynamic_contains:
                        raise JsonSchemaValueException("data.dynamic must contain one of contains definition", value=data__dynamic, name="data.dynamic", definition={'contains': {'const': 'version'}, '$$description': ['version should be listed in ``dynamic``']}, rule='contains')
    return data

def validate_https___www_python_org_dev_peps_pep_0621___definitions_dependency(data, custom_formats={}):
    if not isinstance(data, (str)):
        raise JsonSchemaValueException("data must be string", value=data, name="data", definition={'$id': '#/definitions/dependency', 'title': 'Dependency', 'type': 'string', 'description': 'Project dependency specification according to PEP 508', 'format': 'pep508'}, rule='type')
    if isinstance(data, str):
        if not custom_formats["pep508"](data):
            raise JsonSchemaValueException("data must be pep508", value=data, name="data", definition={'$id': '#/definitions/dependency', 'title': 'Dependency', 'type': 'string', 'description': 'Project dependency specification according to PEP 508', 'format': 'pep508'}, rule='format')
    return data

def validate_https___www_python_org_dev_peps_pep_0621___definitions_entry_point_group(data, custom_formats={}):
    if not isinstance(data, (dict)):
        raise JsonSchemaValueException("data must be object", value=data, name="data", definition={'$id': '#/definitions/entry-point-group', 'title': 'Entry-points', 'type': 'object', '$$description': ['Entry-points are grouped together to indicate what sort of capabilities they', 'provide.', 'See the `packaging guides', '<https://packaging.python.org/specifications/entry-points/>`_', 'and `setuptools docs', '<https://setuptools.pypa.io/en/latest/userguide/entry_point.html>`_', 'for more information.'], 'propertyNames': {'format': 'python-entrypoint-name'}, 'additionalProperties': False, 'patternProperties': {'^.+$': {'type': 'string', '$$description': ['Reference to a Python object. It is either in the form', '``importable.module``, or ``importable.module:object.attr``.'], 'format': 'python-entrypoint-reference', '$comment': 'https://packaging.python.org/specifications/entry-points/'}}}, rule='type')
    data_is_dict = isinstance(data, dict)
    if data_is_dict:
        data_keys = set(data.keys())
        for data_key, data_val in data.items():
            if REGEX_PATTERNS['^.+$'].search(data_key):
                if data_key in data_keys:
                    data_keys.remove(data_key)
                if not isinstance(data_val, (str)):
                    raise JsonSchemaValueException(""+"data.{data_key}".format(**locals())+" must be string", value=data_val, name=""+"data.{data_key}".format(**locals())+"", definition={'type': 'string', '$$description': ['Reference to a Python object. It is either in the form', '``importable.module``, or ``importable.module:object.attr``.'], 'format': 'python-entrypoint-reference', '$comment': 'https://packaging.python.org/specifications/entry-points/'}, rule='type')
                if isinstance(data_val, str):
                    if not custom_formats["python-entrypoint-reference"](data_val):
                        raise JsonSchemaValueException(""+"data.{data_key}".format(**locals())+" must be python-entrypoint-reference", value=data_val, name=""+"data.{data_key}".format(**locals())+"", definition={'type': 'string', '$$description': ['Reference to a Python object. It is either in the form', '``importable.module``, or ``importable.module:object.attr``.'], 'format': 'python-entrypoint-reference', '$comment': 'https://packaging.python.org/specifications/entry-points/'}, rule='format')
        if data_keys:
            raise JsonSchemaValueException("data must not contain "+str(data_keys)+" properties", value=data, name="data", definition={'$id': '#/definitions/entry-point-group', 'title': 'Entry-points', 'type': 'object', '$$description': ['Entry-points are grouped together to indicate what sort of capabilities they', 'provide.', 'See the `packaging guides', '<https://packaging.python.org/specifications/entry-points/>`_', 'and `setuptools docs', '<https://setuptools.pypa.io/en/latest/userguide/entry_point.html>`_', 'for more information.'], 'propertyNames': {'format': 'python-entrypoint-name'}, 'additionalProperties': False, 'patternProperties': {'^.+$': {'type': 'string', '$$description': ['Reference to a Python object. It is either in the form', '``importable.module``, or ``importable.module:object.attr``.'], 'format': 'python-entrypoint-reference', '$comment': 'https://packaging.python.org/specifications/entry-points/'}}}, rule='additionalProperties')
        data_len = len(data)
        if data_len != 0:
            data_property_names = True
            for data_key in data:
                try:
                    if isinstance(data_key, str):
                        if not custom_formats["python-entrypoint-name"](data_key):
                            raise JsonSchemaValueException("data must be python-entrypoint-name", value=data_key, name="data", definition={'format': 'python-entrypoint-name'}, rule='format')
                except JsonSchemaValueException:
                    data_property_names = False
            if not data_property_names:
                raise JsonSchemaValueException("data must be named by propertyName definition", value=data, name="data", definition={'$id': '#/definitions/entry-point-group', 'title': 'Entry-points', 'type': 'object', '$$description': ['Entry-points are grouped together to indicate what sort of capabilities they', 'provide.', 'See the `packaging guides', '<https://packaging.python.org/specifications/entry-points/>`_', 'and `setuptools docs', '<https://setuptools.pypa.io/en/latest/userguide/entry_point.html>`_', 'for more information.'], 'propertyNames': {'format': 'python-entrypoint-name'}, 'additionalProperties': False, 'patternProperties': {'^.+$': {'type': 'string', '$$description': ['Reference to a Python object. It is either in the form', '``importable.module``, or ``importable.module:object.attr``.'], 'format': 'python-entrypoint-reference', '$comment': 'https://packaging.python.org/specifications/entry-points/'}}}, rule='propertyNames')
    return data

def validate_https___www_python_org_dev_peps_pep_0621___definitions_author(data, custom_formats={}):
    if not isinstance(data, (dict)):
        raise JsonSchemaValueException("data must be object", value=data, name="data", definition={'$id': '#/definitions/author', 'title': 'Author or Maintainer', '$comment': 'https://www.python.org/dev/peps/pep-0621/#authors-maintainers', 'type': 'object', 'properties': {'name': {'type': 'string', '$$description': ['MUST be a valid email name, i.e. whatever can be put as a name, before an', 'email, in :rfc:`822`.']}, 'email': {'type': 'string', 'format': 'idn-email', 'description': 'MUST be a valid email address'}}}, rule='type')
    data_is_dict = isinstance(data, dict)
    if data_is_dict:
        data_keys = set(data.keys())
        if "name" in data_keys:
            data_keys.remove("name")
            data__name = data["name"]
            if not isinstance(data__name, (str)):
                raise JsonSchemaValueException("data.name must be string", value=data__name, name="data.name", definition={'type': 'string', '$$description': ['MUST be a valid email name, i.e. whatever can be put as a name, before an', 'email, in :rfc:`822`.']}, rule='type')
        if "email" in data_keys:
            data_keys.remove("email")
            data__email = data["email"]
            if not isinstance(data__email, (str)):
                raise JsonSchemaValueException("data.email must be string", value=data__email, name="data.email", definition={'type': 'string', 'format': 'idn-email', 'description': 'MUST be a valid email address'}, rule='type')
            if isinstance(data__email, str):
                if not REGEX_PATTERNS["idn-email_re_pattern"].match(data__email):
                    raise JsonSchemaValueException("data.email must be idn-email", value=data__email, name="data.email", definition={'type': 'string', 'format': 'idn-email', 'description': 'MUST be a valid email address'}, rule='format')
    return data