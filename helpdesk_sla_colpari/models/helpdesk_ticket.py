# Copyright (C) 2023 colpari GmbH <colpari.cx>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from datetime import datetime


class colpariHelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    sla_expired = fields.Boolean(string="SLA expired")
    sla_deadline = fields.Datetime(string="SLA deadline")

    team_sla = fields.Boolean(string="Team SLA", compute="_compute_team_sla")

    @api.depends('team_id.use_sla')
    def _compute_team_sla(self):
        for rec in self:
            rec.team_sla = rec.team_id.use_sla

    hours_since_open = fields.Float(compute='_comp_hours_since_open')

    @api.depends('create_date')
    def _comp_hours_since_open(self):
        now = datetime.now()
        for ticket in self:
            ticket.hours_since_open = (now - ticket.create_date).total_seconds() / 3600

    hours_in_stage = fields.Float(compute='_comp_hours_in_stage')

    @api.depends('last_stage_update')
    def _comp_hours_in_stage(self):
        now = datetime.now()
        for ticket in self:
            ticket.hours_in_stage = (now - ticket.last_stage_update).total_seconds() / 3600
