import os
import sys
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', "src", "example_coverage")))
import example_coverage
sys.path.append("D:\\GitHub\\example-coverage\\tests\\assets\\moduleC")

class TestClass:
    def setup_class(self):
        self.current_directory = os.getcwd()

    def teardown_class(self):
        pass

    def test_evaluate_examples_coverage(self):
        package_path = os.path.join(self.current_directory, "assets", "moduleC", "__init__.py")
        example_coverage.evaluate_examples_coverage(package_path)
        print (sys.stdout)
        assert os.path.exists(test_project)