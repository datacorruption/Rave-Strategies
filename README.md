<p align="center"><img src="https://user-images.githubusercontent.com/2317743/124702841-05e89c80-dea6-11eb-9e98-5d4c3342a140.png"></p>

## About

Rave Strategies is a tool for generating creative prompts to assist in the production of rave tracks. It provides the following guidance each time it's run:

- Tempo
- Genre
- Key
- Sound Sources
- Sequencer
- Song Length
- Song Description

## Sample Output

>Write a 170bpm jungle track in F# minor using Paripi Destroyer / Korg NTS-1 / PO33 KO with a duration of ~3:00.
>
>It should glow like a figure from a half-remembered dream.

<br/>

>Write a 90bpm gabber track in B major using Zero Point Oscillator / ER301 / Crater sequenced by Teletype with a duration of ~2:00.
>
>It should taste like a stone on the ocean floor.

<br/>

>Write a 200bpm vaporwave track in Bb major using General CV / Tyme Sefari MK2 / Akemie's Castle sequenced by Cirklon with a duration of ~5:00.
>
>It should transform like a love in the pit of your stomach.

## Requirements
- Python3
- Network Connection

## Dependencies
- python-dotenv

## Setup
- Install dependencies
- Create .env file within root directory of project, formatted as follows:
```
GMAIL_USER=your_email_address
GMAIL_PASSWORD=your_password
EMAIL_RECIPIENT=email_address_receiving_rave_strategies
```
- Modify system_list and sequencer_list in songdata.py to reflect your own gear.

## Usage

```sh
$ python3 rave-strategies.py
```

## To Do
- Add weighted probability to sequencer selection
- Expand vocab for actions, things, contexts


## Who Made This?
I'm [Jeremiah Johnson](http://jeremiahjohnson.rip) — electronic musician, creative technologist, and hiker. Currently designing, coding, and consulting at [Final Form](https://www.finalform.systems). Previously, I’ve worked as Lead Creative Technologist at Barbarian, Data Engineer at Columbia University Medical Center, Adjunct Professor at New York University, Creative Director for an international music festival, and contributor to O'Reilly's technical books. I have a music production studio in Tucson, AZ where I use modular synths and drum machines alongside obsolete videogame consoles to produce rave tracks for the end of the world under the name [𝑵𝑼𝑳𝑳𝑺𝑳𝑬𝑬𝑷](http://nullsleep.com). You can find my tunes on [Bandcamp](https://nullsleep.bandcamp.com) and [SoundCloud](https://soundcloud.com/nullsleep).

Twitter: [@Nullsleep](https://twitter.com/Nullsleep)</br>
Instagram: [@Nullsleep](https://instagram.com/Nullsleep)
