from unittest import TestCase
from .crypto import CryptoPassword


class TestCrypto(TestCase):
    def test_encrypt_should_be_different_of_input(self):
        mocked_password = 'password'

        encrypted_password = CryptoPassword.hash_password(mocked_password)

        self.assertNotEqual(mocked_password, encrypted_password)

    def test_decrypt_should_be_equal_of_input(self):
        mocked_password = 'password'

        encrypted_password = CryptoPassword.hash_password(mocked_password)

        self.assertTrue(
            CryptoPassword.check_password(
                mocked_password,
                encrypted_password
            )
        )
