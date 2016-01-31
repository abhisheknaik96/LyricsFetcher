# LyricsFetcher
Description : On the press of a button, fetches the lyrics of the song currently playing (on Rhythbox in Ubuntu) either locally, or from the internet.

Inspiration : 

If my laptop is on, my music is on.
Whenever I had any doubts about what was just said in the song, I used to google up the lyrics and find out. Moreover, for the songs that I really liked, I used to open the lyrics page again and again whenever the song played, in order to quickly memorise it.

Which led me to the geek in me ask - Why don't I automate this?
So I sat down, designed what I wanted exactly, and set about coding it in Python + Bash, my favourite scripting languages. 

Here's the high overview of the functioning:

1. On the press of a hotkey, the script kicks into action.
2. Finds out the song currently playing, with some Bash-magic.
3. Checks if the lyrics are already present on the local machine. If yes, goes to 7.
4. If not, googles for it, goes to the 'atozlyrics' link.
5. Scrapes the HTML for the lyrics.
6. Saves the lyrics.
7. Displays the lyrics in a text editor.


ToDo:

Currently supports only English songs.

1. To find a reliable Hindi song lyrics website.
2. Detect the language of the song, using its name. (NLP-funda)  