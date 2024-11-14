.. _editor:

Text Editors
-------------

Text editors are used for editing plain text files. 
The Campus Cluster has two text editing programs: `vi <http://en.wikibooks.org/wiki/Learning_the_vi_Editor>`_ (and an improved version called `vim <http://www.vim.org/>`_) and `nano <http://www.nano-editor.org/>`_.

vi/vim is one of the most commonly used text editors, however Campus Cluster staff recommend that new Linux users start off using nano; nano may be more similar to the way users edit text files on non-Linux based machines. 

The general syntax to begin editing a file with nano is:

.. code-block:: terminal

   nano file.txt

The same syntax is used to edit a file with vim:

.. code-block:: terminal

   vi file.txt

A newer version of vim (non-default) is available and accessed via the modulefile vim (see :ref:`modules`).

.. raw:: html

   <details>
   <summary><a><b>nano Text Editor Example</b> <i>(click to expand/collapse)</i></a></summary>

This example creates a "hello world" C program in nano.

#. Type the following to open a blank text file named ``hello.c``:

   .. code-block:: terminal

      [My_NetID@cc-login1 ~]$ nano hello.c

#. Type the program exactly as shown below in your nano text editing session.

   .. code-block:: terminal

      #include 

      main()
      {
        printf("Hello, C World!n");

      /* The sleep() function causes the program  */
      /* to wait 90 seconds before ending.        */
      /* This line is optional.                   */
        sleep(90);
   
      }

#. After entering the C program, exit the nano text editing session by holding down control (**Ctrl**) and **X**, which is indicated by a "**^X**" in the bottom left corner of the nano session. 

   Exiting a nano session after editing a text file will prompt to save the changes made to the text file. To save changes *without* exiting the nano session, hold down control (**Ctrl**) and **O**.

.. raw:: html

   </details>

|
