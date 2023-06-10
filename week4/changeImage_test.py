#!/usr/bin/env python3
import os
import unittest
from PIL import Image
from changeImage import convert_images

class ImageConverterTestCase(unittest.TestCase):
    def setUp(self):
        # Create a temporary test directory
        self.test_dir = 'test_images'
        os.makedirs(self.test_dir, exist_ok=True)

        # Create sample TIFF images for testing
        self.create_sample_image('test_image1.tiff', (800, 600))
        self.create_sample_image('test_image2.tiff', (1200, 900))
        self.create_sample_image('test_image3.jpg', (400, 300))  # Non-TIFF file

    def tearDown(self):
        # Remove the temporary test directory and its contents
        for file_name in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, file_name)
            os.remove(file_path)
        os.rmdir(self.test_dir)

    def create_sample_image(self, file_name, size):
        # Create a sample image with the given file name and size
        image_path = os.path.join(self.test_dir, file_name)
        image = Image.new('RGB', size)
        image.save(image_path)

    def test_convert_images(self):
        # Define the expected output file paths and formats
        expected_output_paths = [
            os.path.join(self.test_dir, 'test_image1.jpeg'),
            os.path.join(self.test_dir, 'test_image2.jpeg'),
        ]
        expected_output_format = 'JPEG'

        # Perform the image conversion
        convert_images(self.test_dir, (600, 400), 'jpeg')

        # Assert that the output files exist
        for output_path in expected_output_paths:
            self.assertTrue(os.path.exists(output_path))

        # Assert that the output files are in the expected format
        for output_path in expected_output_paths:
            with Image.open(output_path) as output_image:
                self.assertEqual(output_image.format, expected_output_format)

unittest.main()