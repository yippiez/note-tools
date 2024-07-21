import argparse
import base64


def encode_image_to_base64(image_path):
    """Encode an image to base64."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')


def create_image_html(image_paths, width, height):
    """Create HTML with base64-encoded images."""
    images_html = ""
    for path in image_paths:
        # Encode the image to base64
        encoded_image = encode_image_to_base64(path)
        # Determine image style based on width and height
        style = "margin-right: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); border-radius: 5px;"
        if width is not None:
            style += f" width: {width}px;"
        if height is not None:
            style += f" height: {height}px;"

        # Create HTML for each image
        images_html += f'<img src="data:image/png;base64,{encoded_image}" alt="Image" style="{style}">\n'

    # Wrap images in a container
    html_content = f"""
    <style>
      .image-container {{
        display: flex;
        overflow-x: auto;
        white-space: nowrap;
        background-color: white;
        padding: 10px 10px 20px;
        border: 1px solid #ccc;
        margin-bottom: 20px;
      }}
      .image-container::-webkit-scrollbar {{
        height: 8px;
      }}
      .image-container::-webkit-scrollbar-thumb {{
        background-color: #888;
        border-radius: 4px;
      }}
      .image-container::-webkit-scrollbar-thumb:hover {{
        background-color: #555;
      }}
      .image-container::-webkit-scrollbar-track {{
        background-color: transparent;
      }}
      .image-container {{
        scrollbar-width: thin;
        scrollbar-color: #888 transparent;
      }}
    </style>
    <div class="image-container">
      {images_html}
    </div>
    """

    return html_content


def main():
    parser = argparse.ArgumentParser(
        description="Generate an HTML file with base64-encoded images.")
    parser.add_argument('-o', '--output', type=str, default='output.html',
                        help="Output HTML file path (default: output.html).")
    parser.add_argument('-W', '--width', type=int, default=None,
                        help="Width of the images in pixels.")
    parser.add_argument('-H', '--height', type=int,
                        default=None, help="Height of the images in pixels.")
    parser.add_argument('-i', '--input', type=str, nargs='+',
                        required=True, help="Paths to image files.")

    args = parser.parse_args()

    html_content = create_image_html(args.input, args.width, args.height)

    with open(args.output, 'w') as file:
        file.write(html_content)

    print(f"HTML file created: {args.output}")


if __name__ == "__main__":
    main()
