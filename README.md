# Notebook Cleaner

Notebook Cleaner is a command line tool that removes additional information from a Jupyter notebook file.

### Motivation

Some softwares or platforms may store additional information, such as user name, in the `metadata` of a `.ipynb` file, which is insecure.

### Requirements

+ Python (Python 3 is recommended, while Python 2 is also supported.)

### Usage

```sh
$ python notebook-cleaner.py FILE.ipynb
```
This will write the result back into the original file. The output file can be specified with `--output`.

### Note

* Unless `--output` is provided, this overwrites the original (input) file. It always overwrites the output file if it exists. Consider making a backup before using this.

* This only cleans the metadata. It will not remove the user information if it is not stored in the `metadata`. As a result, this does not remove all information about the author. For example, it's still possible to infer your identity from the coding style you're using.

### How it works

This removes additional data from each cell by setting its `metadata` to empty. It also removes additional keys from the `metadata` of the whole notebook, leaving only the language and kernel information.
