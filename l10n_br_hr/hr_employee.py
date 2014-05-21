# -*- coding: utf-8 -*-
##############################################################################
# #
# Copyright (C) 2014 Proge Informática Ltda (<http://www.proge.com.br>). #
# #
# Author Daniel Hartmann <daniel@proge.com.br> #
# #
# This program is free software: you can redistribute it and/or modify #
# it under the terms of the GNU Affero General Public License as #
# published by the Free Software Foundation, either version 3 of the #
# License, or (at your option) any later version. #
# #
# This program is distributed in the hope that it will be useful, #
# but WITHOUT ANY WARRANTY; without even the implied warranty of #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the #
# GNU Affero General Public License for more details. #
# #
# You should have received a copy of the GNU Affero General Public License #
# along with this program. If not, see <http://www.gnu.org/licenses/>. #
# #
##############################################################################

from osv import osv, fields

class hr_employee(osv.osv):
    _name = 'hr.employee'
    _inherit = 'hr.employee'

    _columns = {
        'matricula': fields.char(u'Matrícula', size=11),
        'pis_pasep': fields.char(u'PIS/PASEP', size=15),
        'carteira_de_trabalho_numero': fields.integer(u'Número da Carteira de Trabalho', size=8),
        'carteira_de_trabalho_serie': fields.integer(u'Série da Carteira de Trabalho', size=5),
        'deficiencia': fields.selection(
         (
             ('0', u'Não possui'),
             ('1', u'Física'),
             ('2', u'Auditiva'),
             ('3', u'Visual'),
             ('4', u'Intelectual (Mental)'),
             ('5', u'Múltipla'),
             ('6', u'Rabilitado'),
         ), u'Deficiência'
        ),
        'etnia_id': fields.many2one('l10n_br_hr.etnia', u'Etnia'),

    }

hr_employee()

