from odoo import fields, models

class studentManagement(models.Model):
    _name = "student.management"
    _description = "gestion de la liste des étudiants"

    last_name = fields.Char(string="Nom", required=True)
    first_name = fields.Char(string="Prénom", required=True)
    gender = fields.Selection(string="Genre", required=True, selection=[("M", "Homme"), ("F", "Femme")])
    birth_date = fields.Date(string="Date de naissance", required=True)
    admission_date = fields.Date(string="Date d'admission", required=True)
    student_id = fields.Integer(string="Numéro étudiant", required=True)
    mail = fields.Char(string="Adresse mail", required=True)
    phone_number = fields.Char(string="Numéro de téléphone", required=True)
    cursus = fields.Many2many("available.formation", string="Formations suivies")