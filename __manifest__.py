{
    'name': 'Biblioteca',
    'version': '18.0.0.1',
    'summary': 'Módulo para gestionar una biblioteca',
    'category': 'Tools',
    'author': 'ESGD, NYVC',
    'website': 'www.example.copm',
    'depends': ['base'],  
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
    ],
    'application': True,  
    'installable': True,
    'auto_install': False,
}