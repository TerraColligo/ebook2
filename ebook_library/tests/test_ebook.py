from odoo.tests.common import TransactionCase

class TestEBook(TransactionCase):
  def setUp(self, *args, **kwargs):
    super(TestEBook, self).setUp(*args, **kwargs)

  def test_create_ebook(self):
    """Create an eBook"""
    EBook = self.env['ebook_library.ebook']#.sudo(self.demo_user)
    ebook_1 = EBook.create({
      'name': 'Test eBook 1',
    })
    self.assertEqual(ebook_1.name, 'Test eBook 1')
