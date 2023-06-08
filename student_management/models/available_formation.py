from odoo import fields, models

class availableFormation(models.Model):
    _name = "available.formation"

    name = fields.Char(string="Nom de la formation")