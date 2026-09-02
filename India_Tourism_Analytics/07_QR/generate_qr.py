"""
============================================================================
Project 2: India Tourist Attractions & Tourism Analytics System
Script: 07_QR/generate_qr.py
Purpose: Generates dedicated Project 2 QR Code image linking strictly to the
         Project 2 GitHub Repository for faculty verification.
============================================================================
"""

import sys
from pathlib import Path
import qrcode

# Dedicated Project 2 Repository URL
PROJECT_2_GITHUB_URL = "https://github.com/231401077-pranav/Mini-project-2-"

OUTPUT_QR_PATH = Path(__file__).resolve().parent / "India_Tourism_Analytics_QR.png"


def generate_project_qr():
    """Generates high-resolution PNG QR Code for Project 2 faculty audit."""
    print(f"Generating QR Code for Project 2 Repository: {PROJECT_2_GITHUB_URL}")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(PROJECT_2_GITHUB_URL)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#0f172a", back_color="#ffffff")
    img.save(OUTPUT_QR_PATH)

    print(f"QR Code successfully saved to: {OUTPUT_QR_PATH}")


if __name__ == "__main__":
    generate_project_qr()
