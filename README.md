# Student Reflection Analysis

## Purpose

This repository is a collection of files and instructions to anonymize and compile student reflections exported from the Canvas LMS.

This is part of a project to test the capabilities of generative AI to write Python code to automate the tedious task of anonymizing and compiling student's reflections to feed the resulting structured output to an AI model in an AI-digestible format while maintaining student privacy. One can then use the AI model with student reflections to evaluate trends in students' learning and quickly adjust teaching to improve instructional effectiveness.

I generated the Python scripts in this repository without any understanding of the Python language. This is evidence of the fact that one needn't need much technical proficiency to use these tools and techniques.

I've made these files publicly available in hopes that others will use more reflective exercises (which are a valuable form of formative assessment) in their courses, see how generative AI can be useful to help evaluate their instruction and their students' learning, and be convinced that they don't need to be a computer scientist to do computer sciency things.

## What are these files and what do they do?

These files are numbered in the order they should be run, or alternatively, once all the scripts and files are ready, you can use `0singlescript.py` to run them all in order. 

Here is a rundown about what each script does:

| Script | Explanation |
| ----------- | ----------- |
| `1anonymizer.py` | Replaces student names with numbers for privacy |
| `2combinehtml.py` | Create a file for each student with all reflections in chronological order |
| `3htmlheadings.py` | Adjust HTML headings for heirarchy |
| `4singlefile.py` | Compile all the students' reflections into a sigle file, heirarchally organized for AI analysis |

## Reflection Assignments in Canvas

>**WARNING:** For any of this to work, your Canvas reflection exercise assignments must use the "text box" input for submissions. Text box submissions are exported in HTML, and this repository's scripts are designed to manipulate those specific HTML files.

## File Preparation

Using these files will require a bit of preparation:

1. Batch Download and extract the student reflection ZIP files from Canvas. 
2. Name the folders for each set of reflections starting with numbers (e.g. 01reflections; 02reflections; 03reflections;...) to ensure chronology in the outputs
3. Put all those folders into a folder with the python scripts from this repository
4. Adjust the files as needed...

### Script Adjustments

#### 1anonymizer.py

For this file, you will need to add your student's names and unique numeric identifiers for each with a text editor. I typically use [Visual Studio Code](https://code.visualstudio.com) to edit code. The file has notes for where the names an numbers go, and what it should look like. Yours should look something like this:

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

The names should be as they exist in your roster on Canvas because each reflection will start with their name, in roster format. For this I made a spreadsheet with the students names in column A (copied directly from the class roster on Canvas), random numbers in column B, and then a formula to take the first two cells and convert it into the above format (`="('"&A2&"', '"&B2&"'),"`). Be sure that you save a key to tell you which number corresponds with which student to distinguish the sets of reflections.

#### 2combinehtml.py

This script assumes that your reflection assignments are named and organized like mine. For instance, since my class was a week-long course, each reflection corresponds to one of 5 days. You will need to feed the script to an AI tool and explain how reflections were titled and organized in my class (Day 1 Reflection, Day 2 Reflection, ..., Final Reflection). Then tell the AI that you want to edit it to work with how you titled and organized your reflection assignments. If you struggle with this, you can give the file to an AI tool and ask it what it looks for about the files, and say something like "I want to use this for my class, and the titles for my reflections are _x_. Please update it to work for my reflections.

#### 3htmlheadings.py

This one is one-size fits all, so no modifications needed.

#### 4singlefile.py

Ditto!

## Running the Scripts

When I used ChatGPT to make the first script, I followed that by asking "Ok. I added the file to the folder. how do I run it?” and then followed its instructions. If you don't know how to run python scripts, like I didn't, it is easily googleable or you can just get instructions from generative AI. 

Python is run via your operating system's [terminal](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Environment_setup/Command_line). You will have to make sure you have [Python](https://www.python.org/downloads/) installed, and for the scripts in this repo, you will also need to install `beautifulsoup4`. You can do that by running `pip install beautifulsoup4` in your terminal after installing Python. If this jargon scares you, I promise it is simpler than you think. You can even give an AI tool the files in this repository and ask it what you need to do to run them.

## Using the Final Outputs

You will have one html file for each student, and a single html file with all student's reflections when you are done processing them with the above scripts. Once you have those files, you have some options about how to use them. Here are just a few.

1. You can open them like any other file and read them. They will open in your default web browser, and you can interact with them as you would any other basic HTML page.
2. You can feed them to an AI chat and ask it questions. I've included a [sample prompt](https://github.com/rbbrownelluh/ReflectionAnalysis/blob/main/samplestartprompt.txt) that I've used to do that with ChatGPT, but you will need to adjust it based on the subject of your course and your preferences.
3. You can create something like a custom GPT so you can have a more permanent tool to use over time. I've included a [sample set of instructions](https://github.com/rbbrownelluh/ReflectionAnalysis/blob/main/SampleGPTInstructions.txt) for a custom GPT that I use. I also made a [puclic custom GPT](https://chatgpt.com/g/g-vIcMYYOYn-legal-research-reflection-analyst) so anyone can preview some of the capabilites with a sample set of processed reflections.
