import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '870', 'Valencia St']

# Check if command line arguments were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

#
webbrowser.open('https://www.google.ie/maps/place/' + address)
