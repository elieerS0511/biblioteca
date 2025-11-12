from odoo import models, fields

class LibraryAuthor(models.Model):
    _name = 'library.author' 
    _description = 'Autor de libros'
    
    name = fields.Char('Nombre', required=True)
    biography = fields.Text('Biografía')