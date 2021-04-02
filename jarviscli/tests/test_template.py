import unittest
from tests import PluginTest
from plugins import template
import os
from os.path import expanduser

class TemplateTest(PluginTest):
    def setUp(self):
        self.test = self.load_plugin(template.template)

    # test creation of different templates
    # these tests pass a valid args string and then check the directory, and files have been created
    def test_python_template(self):
        args = '-l python -n test_python -p ~'
        self.test.run(args)
        self.assertTrue(os.path.exists(expanduser("~/test_python")))
        self.assertTrue(os.path.exists(expanduser("~/test_python/main.py")))
        os.system("rm -rf ~/test_python")

    def test_java_template(self):
        args = '-l java -n test_java -p ~'
        self.test.run(args)
        self.assertTrue(os.path.exists(expanduser("~/test_java")))
        self.assertTrue(os.path.exists(expanduser("~/test_java/Test_java.java")))
        os.system("rm -rf ~/test_java")

    def test_c_template(self):
        args = '-l c -n test_c -p ~'
        self.test.run(args)
        self.assertTrue(os.path.exists(expanduser("~/test_c")))
        self.assertTrue(os.path.exists(expanduser("~/test_c/main.c")))
        self.assertTrue(os.path.exists(expanduser("~/test_c/Makefile")))
        os.system("rm -rf ~/test_c")

    def test_node_template(self):
        args = '-l node -n test_node -p ~'
        self.test.run(args)
        self.assertTrue(os.path.exists(expanduser("~/test_node")))
        self.assertTrue(os.path.exists(expanduser("~/test_node/index.html")))
        self.assertTrue(os.path.exists(expanduser("~/test_node/main.js")))
        self.assertTrue(os.path.exists(expanduser("~/test_node/package.json")))
        os.system("rm -rf ~/test_node")

    def test_rust_template(self):
        args = '-l rust -n test_rust -p ~'
        self.test.run(args)
        self.assertTrue(os.path.exists(expanduser("~/test_rust")))
        self.assertTrue(os.path.exists(expanduser("~/test_rust/Cargo.toml")))
        self.assertTrue(os.path.exists(expanduser("~/test_rust/src/main.rs")))
        os.system("rm -rf ~/test_rust")

    # test invalid arguments being passed
    def test_arg_parser(self):
        args = '-l python -n test_args -p ~ -f stuff -d fake'
        self.test.run(args)
        self.assertTrue(os.path.exists(expanduser("~/test_args")))
        os.system("rm -rf ~/test_args")

if __name__ == '__main__':
    unittest.main()