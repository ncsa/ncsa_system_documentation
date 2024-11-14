.. _windows:

Windows Linux Compatibility
---------------------------

There are some issues to be aware of when transitioning between Windows systems and the Campus Cluster.

- Linux and Windows use different formats for line breaks in text files, which can cause problems when reading Windows Notepad edited files on the Campus Cluster. For the same reason, when reading Linux created text files in Windows, Notepad will present the file in a single line. **WordPad** on Windows is recommended for editing text files when transitioning between Windows systems and the Campus Cluster.

- Unlike Windows and Mac OS X, Linux file and directory (folder) names are case sensitive.

- Avoid spaces in file or directory names on Linux because it can cause problems. One option is to rename files with a character such as “_” or “.” in place of the spaces *before* transferring to the Campus Cluster. If you keep spaces in your file names, see `How to Read a Filename with Spaces in Linux <https://linuxopsys.com/topics/how-to-read-filename-with-spaces-in-linux>`_ for how to deal with them.
