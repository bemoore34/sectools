from passlib.hash import pbkdf2_sha512
import re
import ipaddress


__author__ = 'bmoore'


class Utils(object):

    @staticmethod
    def email_is_valid(email):
        email_address_matcher = re.compile('^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def hash_password(password):
        """
        Hashes a password using pbkdf2_sha512
        :param password: The sha512 password from the login/register form
        :return: A sha512->pbkdf2_sha512 encrypted password
        """
        return pbkdf2_sha512.hash(password)
        # Note - the "encrypt" method used in the course has been deprecated. Use "hash" - more accurate anyway.

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Checks that the password the user sent matches what is in the database. The password in
        the database is encrypted.
        :param password: sha512-hashed password
        :param hashed_password: pbkdf2_sha512 encrypted password
        :return: True is passwords match, False otherwise
        """
        return pbkdf2_sha512.verify(password, hashed_password)

    @staticmethod
    def check_ip4_address(strvalue):
        """
        Check whether a supplied string is a valid IP address
        :param strvalue: supplied value
        :return: True is string is a valid IP address
        """
        try:
            ipaddress.IPv4Address(strvalue)
            return True
        except ipaddress.AddressValueError:
            return False

    @staticmethod
    def internal_address(ipaddr):
        """
        Check whether a provided IP address is an internal address
        :param ipaddr: a provided ip address
        :return: True if matches a valid internal IP address range
        """
        # Note - also have to account for the 106 range!
        ipaddr = ipaddress.
        if self.ipv4:
            ip = ipaddress.IPv4Address(self.value)
        else:
            ip = ipaddress.IPv6Address(self.value)
        return ip.is_private
