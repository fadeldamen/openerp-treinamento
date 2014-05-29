from osv import fields, osv


class user_from_employee(osv.TransientModel):
    _name = 'l10n_br_hr.user_from_employee'
    _description = 'Creates and associates user from employee data'

    _columns = {
         'employee_id': fields.many2one('hr.employee', string=u'Funcionário'),
         'name': fields.char(u'Nome', size=128, required=True, select=True),
          'login': fields.char(u'Login', size=64, required=True,
                         help="Used to log into the system"),
         'state': fields.selection([
            ('initial', 'Initial'),
            ('associated', 'Already Associated'),
            ('done', 'Done'),
        ],
        )
    }

    def _get_default_employee(self, cr, uid, context=None):
        return context.get('employee_id', None)

    def _get_default_state(self, cr, uid, context=None):
        return 'initial'

    def _get_default_name(self, cr, uid, context=None):
        return context.get('employee_name', '')





    _defaults = {
        'state': _get_default_state,
        'name': _get_default_name,
        'employee_id': _get_default_employee,
    }

    def done(self, cr, uid, ids, context=None):
        return {'type': 'ir.actions.act_window_close'}

    def create_user(self, cr, uid, ids, context=None):

        user_obj = self.pool.get('res.users')
        employee_obj = self.pool.get('hr.employee')

        for wizard in self.browse(cr, uid, ids, context=context):

            user_id = user_obj.create(cr, uid, {
                'name': wizard.name,
                'login': wizard.login,
                'company_id': context.get('company_id'),
                }, context=context)

            employee_obj.write(cr, uid, wizard.employee_id.id, {
                'user_id': user_id
                }, context=context)

            self.write(cr, uid, wizard.id, {'state': 'done'}, context=context)

        ir_model_data = self.pool.get('ir.model.data')
        __, view_id = ir_model_data.get_object_reference(
            cr, uid, 'l10n_br_hr', 'l10n_br_hr_user_from_employee_wizard_form'
            )
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'l10n_br_hr.user_from_employee',
            'res_id': ids[0],
            'view_type': 'form',
            'view_mode': 'form',
            'views': [(view_id, 'form')],
            'view_id': False,
            'target': 'new',
            'nodestroy': True,
            }

user_from_employee()

