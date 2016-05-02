import re
import unittest
from .testutils import system

class IpAddrTestCase(unittest.TestCase):

    def test_ipaddr(self):
        """
        Test ip addr
        """
        out,err,ret = system("ip addr | grep 'inet '")
        out = out.decode('utf-8')
        ip=[]
        iplist=out.split("\n")
        for i in range(0,len(iplist)-1):
            ip.append((re.findall( r'[0-9]+(?:\.[0-9]+){3}',iplist[i] ))[0])
        for i in ip:
            self.assertTrue(i)

if __name__ == '__main__':
    unittest.main()
