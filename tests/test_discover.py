import os
import sys
import pytest
import io
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', "ansys", "tools", "example_coverage")))
import example_coverage

class TestClass:
    def setup_class(self):
        self.current_directory = os.getcwd()

    def teardown_class(self):
        pass

    def test_package_c(self):
        folder_path = os.path.join(self.current_directory, "assets", "moduleC")

        # Redirect stdout.
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        example_coverage.create_report(folder_path)
        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Get the current report content.
        current_report_content = capturedOutput.getvalue()

        reference_report_content = """Name                                            Methods     Missed   Covered
-------------------------------------------------------------------------------
moduleC.module_c                                      5          1     80.0%
-------------------------------------------------------------------------------
Total                                                 5          1     80.0%
"""

        # Compare the current report content and the reference one.
        assert current_report_content == reference_report_content


    def test_empty_folder(self):
        """ Provide a folder that does not contain any file or folder."""
        folder_path = os.path.join(self.current_directory, "assets", "EmptyFolder")

        with pytest.raises(Exception):
            example_coverage.create_report(folder_path, match="None file nor folder available in")

    def test_only_init_module(self):
        """ Provide a folder that contains solely an __init__.py file."""
        folder_path = os.path.join(self.current_directory, "assets", "OnlyInit")

        with pytest.raises(Exception):
            example_coverage.create_report(folder_path, match="None module found in: ")


    def test_module_b(self):
        """ The package tested is made of a single module.
        None __init__.py file is available.
        In this module, there is a single private function.
        So, none example is expected for this entire module."""
        folder_path = os.path.join(self.current_directory, "assets", "moduleB")

        # Redirect stdout.
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        example_coverage.create_report(folder_path)
        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Get the current report content.
        current_report_content = capturedOutput.getvalue()

        reference_report_content = """Name                                            Methods     Missed   Covered
-------------------------------------------------------------------------------
moduleB.module_b                                      0          0    100.0%
-------------------------------------------------------------------------------
Total                                                 0          0    100.0%
"""

        # Compare the current report content and the reference one.
        assert current_report_content == reference_report_content


    def test_module_a(self):
        """ The package tested is made of several modules and submodules."""
        folder_path = os.path.join(self.current_directory, "assets", "moduleA")

        # Redirect stdout.
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        example_coverage.create_report(folder_path)
        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Get the current report content.
        current_report_content = capturedOutput.getvalue()

        reference_report_content = """Name                                            Methods     Missed   Covered
-------------------------------------------------------------------------------
moduleA.moduleAA.module_aa                            5          1     80.0%
moduleA.moduleAA.moduleAAA.module_aaa                 5          1     80.0%
moduleA.moduleAB.module_ab                            7          1     85.7%
-------------------------------------------------------------------------------
Total                                                17          3     82.4%
"""

        # Compare the current report content and the reference one.
        assert current_report_content == reference_report_content