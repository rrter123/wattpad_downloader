## Version 1.0.0 - 20.05.2021
This script downloads wattpad stories and saves them in a nicely formatted .txt file. Chapter names are kept. Formatting, that is, **bold** and _italic_, are not.

Works on Python3

To use first install requirements with 
`pip install -r requirements.txt`
Right now only beautifulsoup4 is required.

To download the story run:
`python main.py link_to_the_story filename`
Link has to be directly to the main page of the story.
If you don't provide a filename it will by default be "Downloaded Wattpad Story"

#### Things I might do in the future
Automatially setting the filename to the story name 
Getting to the main link from chapter links
Saving the story directly into epub  
Add tests