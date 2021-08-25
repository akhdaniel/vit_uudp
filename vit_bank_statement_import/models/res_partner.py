from odoo import api, fields, models, _
import time
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    mid = fields.Char(string="MID", required=False)
    va = fields.Char(string="Virtual Account", required=False)
