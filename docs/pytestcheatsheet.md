
1. Installation:
   ```bash
   pip install pytest
   ```

2. Writing Tests:
   - Test files should be named `test_*.py` or `*_test.py`
   - Test functions should be named `test_*`
   ```python
   def test_addition():
       assert 2 + 2 == 4

   def test_subtraction():
       assert 5 - 3 == 2
   ```

3. Running Tests:
   ```bash
   pytest  # Run all tests in the current directory and subdirectories
   pytest test_file.py  # Run tests in a specific file
   pytest test_directory/  # Run tests in a specific directory
   ```

4. Assertions:
   ```python
   assert expression  # Basic assertion
   assert expression, "Failure message"  # Assertion with a failure message

   # Common assertions
   assert value == expected  # Equality assertion
   assert value != expected  # Inequality assertion
   assert value < expected  # Less than assertion
   assert value <= expected  # Less than or equal to assertion
   assert value > expected  # Greater than assertion
   assert value >= expected  # Greater than or equal to assertion
   assert value in collection  # Membership assertion
   assert value is None  # None assertion
   assert bool(value) is True  # Boolean assertion
   ```

5. Fixtures:
   - Fixtures are functions that provide a fixed baseline for tests
   - Defined using the `@pytest.fixture` decorator
   ```python
   import pytest

   @pytest.fixture
   def setup_data():
       # Set up test data
       data = [1, 2, 3]
       return data

   def test_using_fixture(setup_data):
       assert len(setup_data) == 3
   ```

6. Parametrized Tests:
   - Run the same test with different input values
   - Defined using the `@pytest.mark.parametrize` decorator
   ```python
   import pytest

   @pytest.mark.parametrize("input_value, expected_output", [
       (2, 4),
       (3, 9),
       (4, 16)
   ])
   def test_square(input_value, expected_output):
       assert input_value ** 2 == expected_output
   ```

7. Skipping Tests:
   - Skip tests based on certain conditions
   - Use the `@pytest.mark.skip` or `@pytest.mark.skipif` decorator
   ```python
   import pytest

   @pytest.mark.skip(reason="Not implemented yet")
   def test_not_implemented():
       pass

   @pytest.mark.skipif(sys.version_info < (3, 6), reason="Requires Python 3.6 or higher")
   def test_requires_python_3_6():
       pass
   ```

8. Marking Tests:
   - Categorize tests using custom markers
   - Define markers using the `@pytest.mark.<marker_name>` decorator
   ```python
   import pytest

   @pytest.mark.slow
   def test_slow_operation():
       pass

   @pytest.mark.fast
   def test_fast_operation():
       pass
   ```

   - Run tests with specific markers:
     ```bash
     pytest -m slow  # Run tests marked as slow
     pytest -m "not slow"  # Run tests not marked as slow
     ```

9. Test Coverage:
   - Install pytest-cov plugin: `pip install pytest-cov`
   - Run tests with coverage:
     ```bash
     pytest --cov=mymodule tests/  # Generate coverage report for 'mymodule'
     pytest --cov=mymodule --cov-report=html tests/  # Generate HTML coverage report
     ```

10. Mocking:
    - Use the `unittest.mock` module or the `pytest-mock` plugin for mocking
    ```python
    from unittest.mock import MagicMock

    def test_mock_function():
        mock_object = MagicMock()
        mock_object.method.return_value = 42

        result = mock_object.method()
        assert result == 42
    ```

Remember to organize your tests into separate files and directories based on the structure of your project. Use meaningful names for your test files, test functions, and fixtures to enhance readability and maintainability.

Regularly run your tests as part of your development and CI/CD pipeline to catch regressions and ensure the quality of your codebase.

Refer to the pytest documentation (https://docs.pytest.org/) for more advanced features, plugins, and configuration options.

