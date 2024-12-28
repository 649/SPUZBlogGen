# SPUZ Blog Post Generator

* Author: [@037](https://x.com/037)

This python script allows you to produce blog posts for the spuz.me platform. You may reverse engineer this script if you find it useful to automate content production for your own blog!

### Recent changes
* Added the ability to save drafts of blog posts
* Moved html content into its own template

### Prerequisites

The only thing you need installed is Python 3.x

```
apt-get install python3
```

You also need the following dependency installed:
```
pip install jinja2
```

You'll need to change the `WORK_DIR` in the code to reflect where you want your drafts and completed blogs to be stored.

Since I keep all my blog post images under "./img/", you're required to have all images stored under that directory.

Your directory tree should look like this for where your `WORK_DIR` is set:
```
./img/
```

Once you've created that folder "img", all images will be stored there. Images must be present prior to entering filename in the script or else it will tell you it's invalid.

Since you do not have the proper CSS and Javascript libraries, once the script is done running, the output (an HTML file) will not render properly.

This output file will only work when uploaded to the spuz.me platform. 
Of course, not everyone will want that, and so if you want to use this script for your own blog, you must modify the HTML content within the python script on your own.

Feel free to optimize and make pull requests! ;-)