GMail sorting scripts
=====================

These scripts help sort email messages that were downloaded from GMail using `getmail 4.34.0+` into folders based on GMail labels. Currently, only the maildir format is supported. There are three scripts:

* `mailparse.py`: This looks at all the e-mails in a maildir and returns a list of unique labels. I recommend running this before setting up the next two scripts. The "configuration" for this is in the code itself.

* `sortchats.py`: This sorts all the chats in a set of maildirs into one "Chats" folder. A group of origin directories and a destination directory is configurable via the `gmailsort_settings.py` file. See `example_settings.py` for more information.

* `mailsort.py`: This sorts the emails in one origin maildir into folders based on labels. It needs a lot of configuration in `gmailsort_settings.py` please check out `example_settings.py` for more information.

* * *

This is a highly customised set of scripts, so please read the code carefully before using. That said, I'd like it to be more general purpose in the future – here are my todos:

* Use a non-Python configuration file.
* Make `mailparse.py` configurable.
* Allow more options for destination maildirs.
* Support `mbox`.