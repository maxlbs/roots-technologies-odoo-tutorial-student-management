{
    'name': 'Gestion des étudiants',
    'version': '15.0.1.0.0',
    'sequence': '12',
    'summary': 'Module de gestion des étudiants',
    'description': 'Module permettant de gérer les étudiants de l université et leurs informations personnelles',
    'author': 'moi@roots.services',
    'maintainer': 'moi@roots.services',

    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_management_views.xml',
        'views/available_formation_views.xml',
        'views/student_management_menus.xml',
    ],

    'licence': 'LGPL-3',
    'installable': True,
    'application': True,
}