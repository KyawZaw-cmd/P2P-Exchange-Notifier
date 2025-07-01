from datetime import datetime
from pytz import timezone
from PIL import Image, ImageDraw, ImageFont
import configparser
import os
import logging
import calculate

logging.basicConfig(filename='photogenerate.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_new_image():
    try:
        # Get the path of the current directory
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Open the original image
        original_image_path = os.path.join(current_directory, "original_image.jpg")
        if not os.path.exists(original_image_path):
            logging.error(f"Original image not found at {original_image_path}")
            return None

        with Image.open(original_image_path) as img:
            # Create an ImageDraw object
            draw = ImageDraw.Draw(img)

            # Specify font file, size, and color
            font_file = "arial.ttf"
            font_size = 26
            font_color = (0, 0, 0)
            font = ImageFont.truetype(font_file, font_size)

            # Specify the number of rows and columns in the table
            num_rows = 4
            num_cols = 3

            # Read table data from file, if available
            table_data_path = os.path.join(current_directory, 'table_data.txt')
            if os.path.exists(table_data_path):
                with open(table_data_path, 'r') as f:
                    table_data = [line.split() for line in f.readlines()]

                # Check if the number of rows and columns in table_data matches the expected values
                if len(table_data) != num_rows or any(len(row) != num_cols for row in table_data):
                    logging.error("Incorrect number of rows or columns in table data.")
                    return None

                # Specify position of the text on the image
                text_position = (280, 357)

                # Draw the table on the image
                for row in range(num_rows):
                    for col in range(num_cols):
                        draw.text(text_position, table_data[row][col], font=font, fill=font_color)
                        text_position = (text_position[0] + 180, text_position[1])
                    text_position = (280, text_position[1] + 100)

            else:
                logging.error("Table data not found.")
                return None

            tz = timezone('Asia/Yangon')
            now = datetime.now(tz)
            date_time_string = now.strftime("%m/%d/%Y %H:%M:%S")

            # Specify position and format of the date and time text
            #date_time_position = (770, 760)
            date_time_position = (60, 120)
            date_time_format = "{}"
            font_size = 18
            font1 = ImageFont.truetype(font_file, font_size)
            
            # Draw the date and time on the image
            draw.text(date_time_position, date_time_format.format(date_time_string), font=font1, fill=font_color)


        # Save the new image
        new_image_path = os.path.join(current_directory, "new_image.jpg")
        img.save(new_image_path)
        return new_image_path

    except Exception as e:
        logging.error(f"Error generating new image: {e}")
        return None


if __name__ == "__main__":
    new_image_path = generate_new_image()