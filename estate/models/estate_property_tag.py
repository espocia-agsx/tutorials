from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tags"

    name = fields.Char(required=True)
