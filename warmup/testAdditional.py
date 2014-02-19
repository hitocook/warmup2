import unittest
import os
import testLib

class TestAddUser(testLib.RestTestCase):
    SUCCESS = 1
    ERR_BAD_CREDENTIALS = -1
    ERR_USER_EXISTS = -2
    ERR_BAD_USERNAME = -3
    ERR_BAD_PASSWORD = -4

    MAX_USERNAME_LENGTH = 128
    MAX_PASSWORD_LENGTH = 128

    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAdd1(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 1)
    def testAdd2(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : '', 'password' : 'password'} )
        self.assertResponse(respData, count = None, errCode = self.ERR_BAD_USERNAME)
    def testAdd3(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 1)
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'wordpass'} )
        self.assertResponse(respData, count = None, errCode = self.ERR_USER_EXISTS)
    def testAdd4(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'a'+'verylongusername' * 8 , 'password' : 'password'} )
        self.assertResponse(respData, count = None, errCode = self.ERR_BAD_USERNAME)
    def testAdd5(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'verylongusername' * 8 , 'password' : 'password'} )
        self.assertResponse(respData, count = 1)
    def testAdd6(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user2' , 'password' : 'a'+'verylongpassword' * 8} )
        self.assertResponse(respData, count = None, errCode = self.ERR_BAD_PASSWORD)
    def testAdd7(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user2', 'password' : 'verylongpassword' * 8 } )
        self.assertResponse(respData, count = 1)
    def testAdd8(self):
        respData = self.makeRequest("/users/add", method="POST", data = { 'user' : 'user3', 'password' : ''} )
        self.assertResponse(respData, count = 1)
    def testReset(self):
        respData = self.makeRequest("/TESTAPI/resetFixture", method="POST", data = {} )                
        self.assertResponse(respData, count = None)

class TestLogin(testLib.RestTestCase):
    SUCCESS = 1
    ERR_BAD_CREDENTIALS = -1
    ERR_USER_EXISTS = -2
    ERR_BAD_USERNAME = -3
    ERR_BAD_PASSWORD = -4

    MAX_USERNAME_LENGTH = 128
    MAX_PASSWORD_LENGTH = 128

    """Test adding users"""
    def assertResponse(self, respData, count = 1, errCode = testLib.RestTestCase.SUCCESS):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testLogin1(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'password'} )
        self.assertResponse(respData, count = 2)
    def testLogin2(self):
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : '', 'password' : 'password'} )
        self.assertResponse(respData, count = None, errCode = self.ERR_BAD_CREDENTIALS)
    def testLogin3(self):
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user1', 'password' : 'wordpass'} )
        self.assertResponse(respData, count = None, errCode = self.ERR_BAD_CREDENTIALS)
    def testLogin4(self):
        self.makeRequest("/users/add", method="POST", data = { 'user' : 'user2', 'password' : 'haha'} )
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user2', 'password' : 'hello'} )
        self.assertResponse(respData, count = None, errCode = self.ERR_BAD_CREDENTIALS)
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user2', 'password' : 'haha'} )
        self.assertResponse(respData, count = 2)
        respData = self.makeRequest("/users/login", method="POST", data = { 'user' : 'user2', 'password' : 'haha'} )
        self.assertResponse(respData, count = 3)
    def testReset(self):
        respData = self.makeRequest("/TESTAPI/resetFixture", method="POST", data = {} )                
        self.assertResponse(respData, count = None)
