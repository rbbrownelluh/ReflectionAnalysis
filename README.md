# Reflection Analysis

## File Preparation

To use these files, you will have to do a bit of preparation.

1. Batch Download and extract the student reflection files from Canvas
2. Name the folders for each set of reflections starting with numbers (e.g. 01reflections; 02reflections; 03reflections;...)
3. Put all those folders into another folder and add the python scripts in this repository into that same folder
4. Adjust the files as may be needed, as listed below

### Script Adjustments

#### 1anonymizer.py

Is this one, you will need to add your student's names and unique numerical identifiers for each with a text editor like Visual Studio Code. The file has notes for where and how to put it, but yours should look someting like this:

`replacements = [
    ('Laura Palmer', '82'),
    ('Dale Cooper', '22'),
    ('Audrey Horne', '44'),
    ('Donna Hayward', '51'),
    ('Shelly Johnson', '89'),
    ('Gordon Cole', '31'),
    ('Bobby Briggs', '90'),
    ('James Hurley', '91'),
    ('Josie Packard', '36'),
    # Add more pairs as needed
]`

The names should be as they exist in your roster on Canvas. What I did was make a spreadsheet with the students name in one column, random numbers in the next, and then a formula to take the first two cells and convert it into the format above (`="('"&A2&"', '"&B2&"'),"`). However you choose to do it, make sure that you save a key to tell you which number corresponds with which student so _you_ can know which student the AI refers to, without the AI knowing which student it is reffering to.

#### 2combinehtml.py

This script assumes that your reflection assignments are named and organized like mine. For instance, since my class was intersession, each reflection corresponds to one of 5 days. You will need to feed the script to an AI tool and explain how reflections were titled and organized in my class (Day 1 Reflection, Day 2 Reflection, ... Final Reflection), and that you want it to work for how you titled and organized your reflections. If you struggle with this, you can give the file to an AI tool and ask it what it looks for about the files, and say something like "I want to use this for my class, and the titles for my reflections are x. Please update it to work for my reflections.

#### 3htmlheadings.py
