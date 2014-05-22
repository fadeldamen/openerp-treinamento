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
import re

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
        'ocupacao_id': fields.many2one('l10n_br_hr.ocupacao', u'Ocupação'),


    }
    _sql_constraints = [
        ('hr_employee_matricula_uniq', 'UNIQUE(matricula)',
        u'Já existe um empregado cadastrado com esta matrícula!'),
    ]
    def on_change_mask_pis_pasep(self, cr, uid, ids, pis_pasep):
        result = {'value': {'pis_pasep': False}}
        if not pis_pasep:
            return pis_pasep
        val = re.sub('[^0-9]', '', pis_pasep)
        if len(val) == 11:
            pis_pasep = "%s.%s.%s-%s" % (val[0:3], val[3:8], val[8:10], val[10:])
            result['value']['pis_pasep'] = pis_pasep
        return result


hr_employee()

