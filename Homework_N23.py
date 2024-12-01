# import unittest
# from bank import BankAccount
#
#
# class TestBankAccount(unittest.TestCase):
#
#     def setUp(self):
#         self.account = BankAccount(owner="Alice", balance=100)
#
#     def test_initial_balance(self):
#         self.assertEqual(self.account.balance, 100)
#         self.assertEqual(self.account.owner, "Alice")
#
#     def test_deposit_positive_amount(self):
#         self.account.deposit(50)
#         self.assertEqual(self.account.balance, 150)
#
#     def test_deposit_negative_amount(self):
#         with self.assertRaises(ValueError):
#             self.account.deposit(-10)
#
#     def test_withdraw_valid_amount(self):
#         self.account.withdraw(50)
#         self.assertEqual(self.account.balance, 50)
#
#     def test_withdraw_insufficient_funds(self):
#         with self.assertRaises(ValueError):
#             self.account.withdraw(150)
#
#     def test_get_balance(self):
#         self.assertEqual(self.account.get_balance(), 100)
#
#     def test_zero_deposit(self):
#         with self.assertRaises(ValueError):
#             self.account.deposit(0)
#
#     def test_zero_withdrawal(self):
#         self.account.withdraw(0)
#         self.assertEqual(self.account.balance, 100)
#
#
# if __name__ == '__main__':
#     unittest.main()


# Shoping Cart Tests

import unittest
from shoppingCart import ShoppingCart  # Replace with the correct file name


class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item("Apple", 1.5, 3)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0], {'name': 'Apple', 'price': 1.5, 'quantity': 3})

    def test_add_item_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("Orange", 1.0, 0)

    def test_total_price(self):
        self.cart.add_item("Apple", 1.5, 2)
        self.cart.add_item("Banana", 0.5, 4)
        self.assertEqual(self.cart.total_price(), 5.0)

    def test_remove_item(self):
        self.cart.add_item("Apple", 1.5, 2)
        self.cart.add_item("Banana", 0.5, 4)
        self.cart.remove_item("Apple")
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]['name'], "Banana")

    def test_remove_item_not_in_cart(self):
        self.cart.add_item("Apple", 1.5, 2)
        self.cart.remove_item("Orange")
        self.assertEqual(len(self.cart.items), 1)

    def test_is_empty(self):
        self.assertTrue(self.cart.is_empty())
        self.cart.add_item("Apple", 1.5, 2)
        self.assertFalse(self.cart.is_empty())

    def test_cart_empty_after_removing_all_items(self):
        self.cart.add_item("Apple", 1.5, 2)
        self.cart.add_item("Banana", 0.5, 4)
        self.cart.remove_item("Apple")
        self.cart.remove_item("Banana")
        self.assertTrue(self.cart.is_empty())


if __name__ == '__main__':
    unittest.main()
