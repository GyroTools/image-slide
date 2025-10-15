import numpy as np


def create_test_data():
    """Create test data for demonstration."""
    # Create a simple test image stack
    n_images = 20
    height, width = 100, 100

    # Create different types of test images
    images = np.empty((height, width, n_images))

    for i in range(n_images):
        # Create different patterns
        x, y = np.meshgrid(
            np.linspace(0, 4 * np.pi, width), np.linspace(0, 4 * np.pi, height)
        )

        if i < 5:
            # Sine wave pattern
            img = np.sin(x + i * 0.5) * np.cos(y + i * 0.3)
        elif i < 10:
            # Concentric circles
            r = np.sqrt((x - 2 * np.pi) ** 2 + (y - 2 * np.pi) ** 2)
            img = np.sin(r - i * 0.2)
        elif i < 15:
            # Gaussian blobs
            img = np.exp(-((x - 2 * np.pi - i * 0.2) ** 2 + (y - 2 * np.pi) ** 2) / 2)
        else:
            # Complex pattern
            img = np.sin(x) * np.exp(
                -((x - 2 * np.pi) ** 2 + (y - 2 * np.pi) ** 2) / 10
            ) + 0.1 * np.random.randn(height, width)

        images[:, :, i] = img

    return images


def create_complex_test_data():
    """Create complex test data for demonstration."""
    shape = (128, 128, 13, 8, 1, 1, 5)
    n_images = np.prod(shape[2:])
    height, width = shape[0], shape[1]

    images = np.empty((height, width, n_images), dtype=complex)

    for i in range(n_images):
        x, y = np.meshgrid(
            np.linspace(0, 2 * np.pi, width), np.linspace(0, 2 * np.pi, height)
        )

        # Create complex images with varying phase
        magnitude = np.cos(float(i / 10)) * np.exp(
            -((x - np.pi) ** 2 + (y - np.pi) ** 2) / 2
        )
        phase = x + y + i * 0.3

        complex_img = magnitude * np.exp(1j * phase)
        images[:, :, i] = complex_img

    return np.reshape(images, shape, order="F")
