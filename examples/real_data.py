import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from examples.create_test_data import create_test_data
from image_slide.viewer import image_slide


def show_real_data():
    data = create_test_data()
    image_slide(data, title="Real Data Example")


if __name__ == "__main__":
    show_real_data()
