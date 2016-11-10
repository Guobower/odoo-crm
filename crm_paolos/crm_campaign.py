# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2016 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api, _

import logging
_logger = logging.getLogger(__name__)


class crm_lead(models.Model):
    _inherit='crm.lead'

    campaign = fields.Many2one(comodel_name='marketing.campaign', string='Campaign')
    revenue_unit = fields.Selection(related='campaign.unit')


class marketing_campaign(models.Model):
    _inherit='marketing.campaign'

    campaign_type = fields.Selection([('local', 'Local'), ('central', 'Central')], string='Campaign type')
    campaign_budget = fields.Float(string='Campaign Budget')
    distribution = fields.Selection([('evenly', 'Evenly Distributed'), ('revenue', 'Revenue')], string='Distribution')
    unit = fields.Selection([('DFP', 'DFP'), ('KFP', 'KFP'), ('kr', 'kr')], string='Unit')
    account_id = fields.Many2one(comodel_name='account.analytic.account', string='Analytic Account')


class note_note(models.Model):
    _inherit='note.note'

    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner')
    due_date = fields.Date('Due Date')
    salesman_id = fields.Many2one(string="Salesman",comodel_name="res.partner",)

    @api.one
    def message_subscribe(self, partner_ids, subtype_ids=None):
        if partner_ids:
            self.salesman_id = partner_ids[0]
        super(note_note, self).message_subscribe(partner_ids, subtype_ids)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
