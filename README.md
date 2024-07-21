# note-tools

`note-tools` is a repository of tools designed to enhance note-taking in Jupyter notebooks (`.ipynb`). This collection includes utilities for managing and displaying content in a notebook environment.

### Tools

#### Generating a image gallery
<span style="color:red;">generate_notes_sidescroll.py</span>

Converts a list of images to a scrollable gallery that includes photos as base64 string.

**Usage**:

```bash
python generate_html.py -o output.html -W 300 -H 150 -i image1.png image2.png image3.png

    -i, --input : Paths to the image files (at least one required).
    -o, --output : Path to the output HTML file (default: output.html).
    -W, --width : Width of the images in pixels (optional).
    -H, --height : Height of the images in pixels (optional).
```

### Contributing

Open an issue or submit a pull request to get involved. Feel free to contribute to the repository by adding more tools or improving existing ones. 

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


---