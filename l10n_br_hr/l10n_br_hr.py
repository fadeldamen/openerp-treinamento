# -*- encoding: utf-8 -*-
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
class l10n_br_hr_etnia(osv.osv):
	_name = 'l10n_br_hr.etnia'
	_columns = {
		'code': fields.char(u'Codigo', size=2, required=True),
		'name': fields.char(u'Descrição', size=60, required=True),
	}

l10n_br_hr_etnia()

class l10n_br_hr_ocupacao(osv.osv):
    _name = 'l10n_br_hr.ocupacao'
    _description = u'Ocupação'
    _columns = {
        'code': fields.char(u'Código', size=5, required=True),
        'name': fields.char(u'Descrição', size=10, required=True),
        }

    def name_get(self, cr, uid, ids, context=None):
        if not ids:
            return []
        reads = self.read(cr, uid, ids, ['name', 'code'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['code']:
                name = str(record['code']) + ' - ' + name
            res.append((record['id'], name))
        return res
    def name_search(self, cr, user, name, args=None, operator='ilike', context=None, limit=80):
        if not args:
            args = []
        if context is None:
            context = {}
        ids = self.search(cr, user, ['|', ('name', operator, name), ('code', operator, name)] + args, limit=limit, context=context)
        return self.name_get(cr, user, ids, context)


l10n_br_hr_ocupacao()
