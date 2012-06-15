import copy
from os.path import join
from templer.core.vars import BooleanVar
from templer.core.vars import EASY
from templer.core.vars import EXPERT
from templer.core import BasicNamespace
from templer.core.structures import Structure


class ContentType(Structure):
    summary = 'Kotti AddOn base files'
    _structure_dir = 'kotti_addon/contenttype'


class Addon(BasicNamespace):

    dots = 0  # for kotti we don't use a dotted namespaces

    summary = 'Kotti AddOn base files'

    _template_dir = 'kotti_addon/addon'

    content_type = BooleanVar('content_type',
        title='Content type example?',
        description='Add content type example to the add-on?',
        default=True,
        modes=(EASY, EXPERT),
        structures={'False': None, 'True': 'content_type'},
    )

    vars = copy.deepcopy(BasicNamespace.vars)
    vars.append(content_type)


class Git(Structure):
    summary = u'generate gitignore file'
    _structure_dir = 'kotti_project/git'


class Travis(Structure):
    summary = u'generate a travis file'
    _structure_dir = 'kotti_project/travis'


class Buildout(BasicNamespace):

    dots = 0  # for kotti we don't use a dotted namespaces
    summary = 'A buildout based Kotti project'

    _template_dir = 'kotti_project/buildout'

    travis = BooleanVar('travis',
        title='Generate a travis configuration file?',
        description='Add a travis configuration file to the buildout?',
        default=False,
        modes=(EXPERT),
        structures={'False': None, 'True': 'travis'},
    )

    gitignore = BooleanVar('gitignore',
        title='Generate a .gitignore file?',
        description='Add a .gitignore file to the buildout?',
        default=True,
        modes=(EXPERT),
        structures={'False': None, 'True': 'gitignore'},
    )

    vars = copy.deepcopy(BasicNamespace.vars)
    vars.extend([travis, gitignore, ])

    # codeintel
    # omelette
    # supervisor

    def post(self, command, output_dir, vars):
        addon_template = Addon(vars['project'])
        addon_template.run(command, join(output_dir, 'src', vars['project']), vars)
