# -*- coding: utf-8 -*-
from odoo import  fields, models

class model(models.Model):
    _name = 'ej.pet'
    name = fields.Char(string='name', required=True)
    age = fields.Integer(string='age')
    color = fields.Char(string='color')
    is_new = fields.Boolean(string='is_new', default=True)
    type = fields.Selection([
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('fish', 'Fish'),
        ('other', 'Other')], string='type', default="dog", required=True)