from distutils.core import setup

# must be in sync with dum_ddc.VERSION
VERSION = (0, 0, 0, 4)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))


data_patterns = [
    'templates/*.html',
    'templates/*/*.html',
    'templates/*/*/*.html',
    'locale/*/*/*'
]

packages = [
    'fragapy', 'fragapy.auth', 'fragapy.common', 'fragapy.countries', 'fragapy.currencies',
    'fragapy.currencies.templatetags', 'fragapy.cz_localflavour',
    'fragapy.object_perms', 'fragapy.odt', 'fragapy.soft_delete_models',
    'fragapy.system_models', 'fragapy.cloneable_models', 'fragapy.adminhelp',
    'fragapy.adminhelp.templatetags', 'fragapy.gmail', 'fragapy.fields', 
    'fragapy.profiling', 'fragapy.versioning', 'fragapy.ella.send_email'
]

setup(
    name = 'fragapy',
    version = __versionstr__,
    description = 'Fragaria commons library',
    long_description = '\n'.join((
        'Fragaria commons library',
    )),
    author = 'Fragaria s.r.o',
    author_email='admin@fragaria.cz',
    license = 'proprietary',
    url='TBD', # FIXME
    
    packages = packages,
    package_data = dict((package_name, data_patterns) for package_name in packages),
    
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)



