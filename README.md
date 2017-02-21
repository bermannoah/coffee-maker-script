# Coffee Maker Script

This is the script that is used by [Coffee Maker Bot](https://github.com/bermannoah/coffee-maker-bot) to run a servo
and then make delicious coffee. Largely an experimental project.

### Installation Instructions

First, a word of warning: this is really only useful on a Raspberry Pi connected with Adafruit's 16 Channel PWM/Servo HAT for Rasperry Pi. Got it? Got it. Cool.

- 1. You'll need to install this library. On the pi, run `sudo apt-get install python-smbus`. You might not need to run it as sudo, but just in case I thought I'd mention it.
- 2. Clone down this repo. Make sure it's in the same directory as Coffee Maker Bot (but not inside Coffee Maker Bot's own directory).
- 3. Modify to suit your needs. I use the npm [clri](https://www.npmjs.com/package/clri) package to actually run the script from within Coffee Maker Bot.

### Enjoy delicious coffee!
