from odoo import fields, models

class Book(models.Model):
    _name = 'library.book'
    _description = 'Libro de Biblioteca'

    title = fields.Char(string='Título', required=True)
    description = fields.Text(string='Descripción')
    publication_date = fields.Date(string='Fecha de Publicación')
    isbn = fields.Char(string='ISBN', size=13)