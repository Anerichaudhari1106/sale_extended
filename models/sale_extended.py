# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo  import fields, models,api

class SaleList(models.Model):
    _name = 'sale.list'


    name = fields.Char(string="Numbers",default="New",readonly=True)
    customer_name = fields.Many2one(comodel_name = 'customer.details',string = 'Customer',required=True)
   
    create_date = fields.Datetime(  # Override of default create_date field from ORM
        string="Creation Date")
    status = fields.Selection(
         selection=[
            ('draft', "Draft"),
            ('conform', "Conform"),
            ('done', "Done"),
            ('cancel',"cancel")
         ],
         string="Status",default='draft')

    amount_total = fields.Float(string="Total")
    discount = fields.Float(string = "Discount")
    order_line = fields.One2many('sale.list.line','sale_oder_id',string="Order Line")
    discount = fields.Float(string="Discount")
    discount_total = fields.Float(string="Discount with Total")
    sub_1 = fields.Float(string='sub_1',help="Add number for Sub 1")
    sub_2 = fields.Float(string='sub_2')
    sub_3 = fields.Float(string='sub_3')
    total_sub = fields.Float(string='total_sub',
                             compute ='_compute_total_sub')

    # <------@api-method-------->

    @api.onchange('order_line')
    def _onchange_amount_total(self):
        if self.order_line:
            total=0
            for rec in self.order_line:
                amount=total+rec.price
                total=amount
            self.amount_total=amount

    @api.onchange('discount')
    def _onchange_discount_total(self):
        if self.discount:
            self.discount_total=self.amount_total*self.discount/100

    @api.onchange('sub_1', 'sub_2', 'sub_3')
    def _onchange_total_sub(self):

        if self.sub_1 or self.sub_2 or self.sub_3:
            self.total_sub = self.sub_1+self.sub_2+self.sub_3 


    @api.depends('sub_1','sub_2','sub_3')
    def _compute_total_sub(self):

        for rec in self:
            rec.total_sub= rec.sub_1 +rec.sub_2+rec.sub_3

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['name'] = self.env['ir.sequence'].next_by_code('sale_list')
            return super(SaleList, self).create(vals_list)

    def order_cancel(self):
        self.status='cancel'

    def order_draft(self):
        self.status='draft'
    def order_conform(self):
        self.status='conform'
    def order_done(self):
        self.status='done'
        

    
    def create_invoice(self):
         # customer = self.env['customer.details'].search([('name','=','ashu')])
         # for rec in customer:
         #    rec.write({
         #        'address':'visnagar'
         #        })
         return self.env.ref('sale_extended.action_view_create_invoice1111111').read()[0]

        # return self.env.ref('sale_extended.action_view_create_invoice1111111').read()[0]

        # return {
        #     'type': 'ir.actions.act_window',
        #     'name': 'create invoice',
        #     'view_mode': 'form',
        #     'res_model': 'create.invoice',
        #     'target': 'new'}
            
                

    def _cron_convert_conform_order(self):
        order = self.env['sale.list'].search([])
        product = self.env['product.details'].search([])


        for rec in order:
            rec.status='conform'

class SaleOderLineExtended(models.Model):
    _name = 'sale.list.line'


    product_id= fields.Many2one('product.details', string = "Product", index=True)
    sale_oder_id= fields.Many2one('sale.list', string = "Order")
    price = fields.Float(string = "price")
    quntity = fields.Float(string = "Quntity")


    @api.onchange('product_id')
    def _onchange_price(self):
        if self.product_id:
            self.price=self.product_id.price

class Product(models.Model):
    _name = 'product.details'

    name = fields.Char(string= "product name")
    price = fields.Float(string = "price")

class Customers(models.Model):
    _name='customer.details'


    name = fields.Char(string = "Customer Name")
    address = fields.Text(string = "Address")  
    contect_no = fields.Integer(string = "Mobile No.")

class InvoiceExtended(models.Model):
    _name = 'account.invoice'

    name = fields.Char(string="Numbers", default="New", readonly=True)
    customer_name = fields.Many2one(comodel_name='customer.details', string='Customer', required=True)

    create_date = fields.Datetime(  # Override of default create_date field from ORM
        string="Creation Date")
    status = fields.Selection(
        selection=[
            ('draft', "Draft"),
            ('conform', "Conform"),
            ('done', "Done"),
            ('cancel', "cancel")
        ],
        string="Status", default='draft')

    amount_total = fields.Float(string="Total")

    invoice_order_line_ids= fields.One2many('account.invoice.line', 'invoice_id', string="Order Line")
    discount = fields.Float(string="Discount")
    discount_total = fields.Float(string="Discount with Total")
   
    product_id = fields.Many2one('product.details', string="Product", index=True)
    price = fields.Float(string="price")

class AccountLineExtended(models.Model):
    _name = 'account.invoice.line'


    product_id= fields.Many2one('product.details', string = "Product", index=True)
    invoice_id= fields.Many2one('account.invoice', string = "Order")
    price = fields.Float(string = "price")
    quntity = fields.Float(string = "Quntity")




    


