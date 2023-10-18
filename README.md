# HubSpot Parsing script
## Project description
Project consists of script that parses three latest posts from https://blog.hubspot.com, for example: https://blog.hubspot.com/marketing, 
and calculates statistics of the parsed texts, such as: 
- number of letters,
- number of words,
- chosen amount of most used keywords.
## Setup
The project was developed and tested on Python v3.8.0. 
If you can't run Makefiles on your machine, use the commands after "or".
1. Create and activate virtual environment, ex. ``python -m venv venv``, then ``activate``.
2. Install project requirements: ``make base_install`` or ``pip install -r requirements.txt``.
3. You can now run the script, with for example: ``make base_run`` or ``python hubspot_parser.py``
## Instruction
You can run the default parsing from Makefile, or config the script by running it manually. 

List of optional arguments for the manual run (shows with `make help`) command:
```
optional arguments:
  -h, --help            Shows help message
  -b BLOG, --blog BLOG  Name of chosen blog, default: marketing
  -t, --test            Perform unit tests and don't perform parsing
  -k, --keywords        Number of calculated keywords to be shown, default: 5
```
The script runs parsing for /marketing blog by default, if you want to change it, use `--blog` argument with name of the chosen blog 
(must be one of existing blogs from the `AVAILABLE_BLOGS` list in config.py).

An amount of keywords parsed can also be changed manually, use `-k` or `--keywords` argument with chosen amount of keywords to change the default value.
  
## Example usage
1. ``python hubspot_parser.py --blog ai -k 4`` - calculates parameters for three latest articles from https://blog.hubspot.com/ai, and prints 4 most used keywords.
2. ``python hubspot_parser.py --b website -keywords 8`` - calculates parameters for three latest articles from https://blog.hubspot.com/website, and prints 8 most used keywords.

## Unit tests
You can perform basic unit tests for some script functions by running the script with `-t` argument, or by running ``make unit_tests``.
