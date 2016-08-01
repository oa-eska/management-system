# -*- coding: utf-8 -*-

from openerp import fields, models


class MgmtSystemVerificationLine(models.Model):
    """Class to manage verification's Line."""
    _name = "mgmtsystem.verification.line"
    _description = "Verification Line"
    _order = "seq"

    name = fields.Char('Question', required=True)
    audit_id = fields.Many2one(
        'mgmtsystem.audit',
        'Audit',
        ondelete='cascade',
        select=True,
    )
    procedure_id = fields.Many2one(
        'document.page',
        'Procedure',
        ondelete='restrict',
        select=True,
    )
    is_conformed = fields.Boolean('Is conformed', default=False)
    comments = fields.Text('Comments')
    seq = fields.Integer('Sequence')
    company_id = fields.Many2one(
        'res.company', 'Company',
        default=lambda self: self.env.user.company_id.id)
