import unittest
from testutils import system


class TestBase(unittest.TestCase):

    def test_selinux(self):
        "Tests the SELinux"
        out, err, eid = system('getenforce')
        out = out.strip()
        self.assertEquals(out, 'Enforcing')

    def test_logging(self):
        "Tests journald logging"
        out, err, eid = system('journalctl -a --no-pager -r --since=$(date +%Y-%m-%d) -n1')
        self.assertGreater(len(out.split()), 3, "journalctl output is missing.")

    @unittest.expectedFailure
    def test_services(self):
        "No service should fail in the startup."
        out, err, eid = system('systemctl --all --failed')
        self.assertIn('0 loaded units listed', out)


if __name__ == '__main__':
    unittest.main()
