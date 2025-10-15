"""
ImageSlideViewer - An interactive image viewer for multidimensional numpy arrays.

A comprehensive Python image viewer with the following features:
- Navigate through image stacks with slider controls
- Support for complex arrays (magnitude, phase, real, imaginary)
- Contrast and brightness adjustment controls
- Multiple colormap options
- Keyboard shortcuts for navigation
- Compact, professional interface
"""

from .image_slide import ImageSlideViewer, image_slide

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

__all__ = ["ImageSlideViewer"]
