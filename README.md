# Reflection Analysis

## Purpose

I generated these files to take Canvas reflection exercise submissions from students, anonymize them, and structure them into a file for each student and one file with a compilation of all students' reflections, in chronological order. I use these files with generative AI to evaluate trends in students' learning over time and find ways to improve my teaching. I generated these files primarily by using ChatGPT, and this project is the breadth of my current experience using python scripts.

I've made these files available in hopes that others will increase their use of reflective exercises in their courses, see that one can find ways to improve the effectiveness of their classes with generative AI, and with hopes that people will send me feedback on their experiments with similar or related techniques.

## What are these files and what do they do?

These files are numbered in the order they should be run, or alternately, once the scripts and files are ready, you can use `0singlescript.py` to run them all in order. Here is a rundown about what each script does.

| Script | Explanation |
| ----------- | ----------- |
| 1anonymizer.py | Replaces student names with numbers for privacy |
| 2combinehtml.py | Create a file for each student reflections in chronological order |
| 3htmlheadings.py | Adjust the HTML headings for each file for heirarchy |
| 4singlefile.py | Compile all the students' reflections into a sigle file, heirarchally organized for AI analysis |


## File Preparation

To use these files, you will have to do a bit of preparation.

1. Batch Download and extract the student reflection files from Canvas (they are exported as zip files)
2. Name the folders for each set of reflections starting with numbers (e.g. 01reflections; 02reflections; 03reflections;...) to ensure chronology in the outputs
3. Put all those folders into a folder the python scripts in this repository
4. Adjust the files as needed. Information about that follows

### Script Adjustments

#### 1anonymizer.py

Is this one, you will need to add your student's names and unique numerical identifiers for each with a text editor like Visual Studio Code. The file has notes for where and how to put it, but yours should look someting like this:

```
replacements = [
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
]
```

The names should be as they exist in your roster on Canvas. What I did was make a spreadsheet with the students name in column A, random numbers in column B, and then a formula to take the first two cells and convert it into the format above (`="('"&A2&"', '"&B2&"'),"`). However you choose to do it, make sure that you save a key to tell you which number corresponds with which student so _you_ can know which student the AI refers to, without the AI knowing which student it is reffering to.

#### 2combinehtml.py

This script assumes that your reflection assignments are named and organized like mine. For instance, since my class was intersession, each reflection corresponds to one of 5 days. You will need to feed the script to an AI tool and explain how reflections were titled and organized in my class (Day 1 Reflection, Day 2 Reflection, ... Final Reflection), and that you want it to work for how you titled and organized your reflections. If you struggle with this, you can give the file to an AI tool and ask it what it looks for about the files, and say something like "I want to use this for my class, and the titles for my reflections are x. Please update it to work for my reflections.

#### 3htmlheadings.py

This one is one-size fits all, so no modifications needed.

#### 4singlefile.py
