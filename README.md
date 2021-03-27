# Code for the Kindle highlight note cracking

This repository contains a script to crack the highlight notes from kindle clipping.txt and create a note.txt file for all the notes without citations

## Steps

1. Copy the `My Clippings.txt` file into the kindle_note_cracker repo 
    ``` cp ~/my_path_of_kindle/documents/My Clippings.txt kindle_note_cracker/My Clippings.txt ```

1. Move to the repo and run the following commands
 ``` cd kindle_note_cracker ```

 - if cracking all notes
 ``` python -m crack_note.py all ```
 
 - if cracking note from one book (note: fuzzy match works, so only substr of the bookname are required)
 ``` python -m crack_note.py bookname ```

