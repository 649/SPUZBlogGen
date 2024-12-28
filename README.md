# SPUZ Blog Post Generator

**Author**: [@037](https://x.com/037)

This Python script generates blog posts for the *spuz.me* platform. If you find it useful for your own blog, you’re welcome to modify or automate it however you see fit.

---

## Recent Changes

- **Draft Saving**: Automatically saves and loads drafts.
- **Template Support**: Separates HTML structure into a dedicated template (`template.html`).

---

## Prerequisites

1. **Python 3.x**  
```bash
apt-get install python3
```

2. **Jinja2**  
```bash
pip install jinja2
```

---

## Configuration

- **WORK_DIR**  
  Update the `WORK_DIR` path in the script to indicate where drafts and finished blog posts should be saved.  

- **Image Storage**  
  All images must reside in `./img/`. Thumbnail images go in `./img/nails/`.

A sample directory structure under your `WORK_DIR` might look like:
```bash
WORK_DIR/
  ├─ img/
  │   └─ nails/
  ├─ ... (other files/folders)
  └─ script.py
```

> **Note**: The script checks for valid image paths before insertion. If the file does not exist under `./img/` (or `./img/nails/` for thumbnails), the script will warn you that it’s invalid.

---

## Usage Notes

1. Run the script and follow the interactive prompts to:
   - Set the blog post’s title, description, author info, and primary images.
   - Add subheaders, paragraphs, images, and embedded videos.

2. When finalized, the script outputs an `.html` file that references **spuz.me**’s CSS and JS. If you’re using this script elsewhere, you will likely need to adjust the HTML to match your own blog’s styling and framework.

3. Drafts are stored as JSON files, allowing you to resume unfinished work at any time.

---

## Disclaimer

The generated HTML is designed for use on spuz.me, which hosts the required CSS and JavaScript assets. If you plan to reuse this script for another blog platform, **be aware** that the output may need additional styling or scripting changes.

Pull requests and optimizations are welcome! Have fun blogging!
