# ----------------------------------------------------------------------------------------------------------------------------
# Test file operations using pytest's built-in tmp_path fixture.Here we are testing a function that writes data to a file
# and then reads it back.To avoid using real files or polluting your file system, you use pytest's tmp_path fixture,
# which creates a temporary directory that’s automatically cleaned up after the test run.
# ----------------------------------------------------------------------------------------------------------------------------

#Test: Write and read from a temporary file using tmp_path
def test_file_write_and_read(tmp_path):
    # Arrange
    # Create a file path inside the temporary directory. tmp_path is a pathlib.Path object provided by pytest
    file_path = tmp_path / "sample.txt"

    # Sample data to write into the file
    test_data = "Pytest makes file testing easy!"

    # Act
    # Write the test data into the file
    file_path.write_text(test_data)

    # Read the data back from the file
    read_data = file_path.read_text()

    #Assert

    # Check if the file was created
    assert file_path.exists()

    # Check if the path is a file (not a directory)
    assert file_path.is_file()

    # Validate that the content written and read are the same
    assert read_data == test_data

    # (Optional) Print the file path to verify where it was created
    print(f"Temporary file created at: {file_path}")
