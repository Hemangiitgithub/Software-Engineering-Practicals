import unittest
import OTP_Using_Function

class TestStringMethods(unittest.TestCase):

    def testcase1(self):
        Email = OTP_Using_Function.validate_email('hemangi.gavande29@gmail.com')
        self.assertEquals(True,Email)

    def testcase2(self):
        size = 4
        Email = OTP_Using_Function. generate_otp()
        self.assertEqual(len(Email), size)

    def testcase3(self):
        Email = OTP_Using_Function.send_mail(OTP_Using_Function. generate_otp())
        self.assertEquals(True,Email)

    # def testcase4(self):
    #     size = 4
    #
    #     Email = OTP_Using_Function.emailsender
    #     self.assertIn("@", Email)
    #     self.assertIn(".", Email)
    #     self.assertIn("com", Email)
    #
    #     res =OTP_Using_Function.otp(4)
    #     self.assertEqual(len(res), size)

if __name__ == '__main__':
    unittest.main()