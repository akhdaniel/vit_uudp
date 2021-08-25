# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Department(models.Model):
    _inherit = "hr.department"

    analytic_account_id = fields.Many2one('account.analytic.account', 'Analytic Account')

Department()