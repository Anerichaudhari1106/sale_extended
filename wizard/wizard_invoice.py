# -*- coding: utf-8 -*-

from odoo import fields, models, api


class InvoiceWizard(models.TransientModel):
    _name = 'create.invoice'

    payment_record = fields.Selection(
        selection=[
            ('delivered', "Regular invoice"),
            ('percentage', "Down payment"),
            ('fixed', "Down payment"),
        ],
        string="Create Invoice")

    def confirm_action(self):
        invoice_obj = self.env['account.invoice']
        # model_name=str(self.env.context.get('active_model'))
        sale_obj = self.env[self.env.context.get('active_model')].search(
            [('id', '=', self.env.context.get('active_id'))])

        invoice_line = self.env['account.invoice.line']
        list = []
        for rec in sale_obj.order_line:


            a = invoice_line.create({'product_id': rec.product_id.id,
                                     'price': rec.price,
                                     'quntity': rec.quntity
                                     })
            list.append(a.id)

        invoice = invoice_obj.create({'customer_name': sale_obj.customer_name.id,
                                      'create_date': sale_obj.create_date,
                                      'status': sale_obj.status,
                                      'amount_total': sale_obj.amount_total,
                                      'invoice_order_line_ids': [(6, 0, list)]
                                      })

