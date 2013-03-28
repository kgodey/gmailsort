# The path to the maildir folder that is being sorted by this script.
ORIGIN_MAILDIR = '/home/kgodey/.maildir/.kritigodeygmail/cur/'

# The path to the destination maildir that the e-mail is sorted into. Takes label name as an argument.
DEST_MAILDIR = lambda label: os.path.join('/home/kgodey/.maildir/', '.kritigodeygmail.%s' % label)

# Labels to be ignored while sorting.
IGNORED_LABELS = ['\\Inbox', '\\Important', '\\Muted', '\\Starred', 'Boomerang', 'Boomerang-Outbox']

# Order of precedence for labels, sorted by importance. If an e-mail has multiple labels, it will be sorted into the folder corresponding to the label which appears earliest in this list. Note that GMail system labels show up as '\\LabelName'.
LABEL_ORDER = ['\\Sent', '\\Draft', 'Jobs', 'Books', 'Family', 'Friends', 'Correspondence', 'Work',  'Oberlin', 'Class', 'Clubs', 'Mailing List', 'Automated', 'Commercial', 'Django', 'facebook']

# Mapping of GMail labels to folder names. These only need to be specified for folder names that are different from the GMail label names. They can also be used to sort multiple labels into the same folder.
LABELS_TO_FIX = {
	'\\Sent': 'Sent',
	'\\Draft': 'Drafts',
	'Mailing List': 'Mailing-List',
	'Django': 'Mailing-List',
	'Website': 'Automated',
	'facebook': 'Automated',
}

# Globbable expression of maildir paths containing emails that are being sorted by sortchats.py. See Python glob module for details.
CHAT_ORIGIN_MAILDIR = '/home/kgodey/.maildir/.kritigodeygmail.*/cur/'
''
# Maildir into which chats are to be sorted. Only used by sortchats.py.
CHAT_DEST_MAILDIR = '/home/kgodey/.maildir/.kritigodeygmail.Chats/'