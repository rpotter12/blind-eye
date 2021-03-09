<p align="center">
  <img src="images/logo.png">
</p>
            
[![Downloads](https://pepy.tech/badge/wplay)](https://pepy.tech/project/wplay)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/749acf4cad424fbeb96a412963aa83ea)](https://app.codacy.com/app/rpotter12/whatsapp-play?utm_source=github.com&utm_medium=referral&utm_content=rpotter12/whatsapp-play&utm_campaign=Badge_Grade_Settings)
[![PyPi](https://img.shields.io/pypi/v/wplay)](https://pypi.org/project/wplay/)
![CircleCI](https://circleci.com/gh/rpotter12/whatsapp-play/tree/master.svg?style=svg&circle-token=2b67dd21e60a01fdd36a670629574479aeb2f5c4)
[![Docker](https://img.shields.io/docker/cloud/build/rpotter12/whatsapp-play)](https://hub.docker.com/repository/docker/rpotter12/whatsapp-play/general)
[![Build Status](https://travis-ci.org/rpotter12/whatsapp-play.svg?branch=master)](https://travis-ci.org/rpotter12/whatsapp-play)
[![codecov](https://codecov.io/gh/rpotter12/whatsapp-play/branch/master/graph/badge.svg)](https://codecov.io/gh/rpotter12/whatsapp-play)
[![twitter](https://img.shields.io/twitter/url/https/github.com/rpotter12/whatsapp-play.svg?style=social)](https://twitter.com/rpotter121998)
[![HitCount](http://hits.dwyl.io/rpotter12/whatsapp-play.svg)](http://hits.dwyl.io/rpotter12/whatsapp-play)
[![Gitter](https://badges.gitter.im/whatsapp-play/community.svg)](https://gitter.im/whatsapp-play/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/rpotter12/whatsapp-play) 

It is a command line software through which you can play with your WhatsApp. It has different options to play with your WhatsApp, like message blast, online tracking, whatsapp chat. This software aims to provide all the facilities to use and implement a multitude of WhatsApp features. This CLI software does not require any API key for the execution.

***online_tracker*** tracks the online and offline timings of your WhatsApp contact. It will check the online status and will immediately store that data into a .txt file. In order to make this work, make sure your Whatsapp language is set to English. Blog link: [https://github.com/rpotter12/rpotter12.github.io/blob/master/blogs/blog3-tracking-26-07-2019.md](https://github.com/rpotter12/rpotter12.github.io/blob/master/blogs/blog3-tracking-26-07-2019.md)

***terminal_chat*** stands for WhatsApp chat. Through this you can chat with your WhatsApp contact directly from the command line. Initially, recent chat is displayed and then the last received message is displayed every time you send a message. The chatbot gets activated when the target sends commands starting with /.Send /help command to see usage.

***chat_intermediator*** lets you be an intermediator between two people.

***message_service*** is a substitute for the API; it allows you to communicate your programs to wplay. You can modify our file messages.json with the number and message and the service will read the JSON and send the message. Check [Wiki Usage](https://github.com/rpotter12/whatsapp-play/wiki/Usage#whatsapp-service) for details.

***telegram_bot*** sends the tracking status to our telegram bot.

***message_blast*** is a message bomb script. It sends messages to your WhatsApp contact continously. The number of messages is decided by you. You can blast infinite number of messages to your WhatsApp contact.

***message_timer*** is a message timer script. It sends messages to your WhatsApp contact from time to time. The number of messages and type of messages is decided by you. It's possible to send messages at random intervals, with the message type chosen randomly.

***save_chat*** is a script to save the chat of the particular target.

***schedule_message*** is a script to send message at a schedule time.

***about_changer*** lets you create a customizable about you section for your profile, or, lets you change the about section of your profile according to lastest headlines.

***get_news*** is a script to get all types of news in your whatsapp group. Visit <https://newsapi.org/> to get your own API key and paste it in newsapi = NewsApiClient(api_key="YOUR API KEY")

***get_profile_photos*** is a script to download profile photos of all the contacts in your whatsapp contact list.

***broadcast_message*** is a script to allow the terminal to send a broadcast message to all the selected target persons.

***target_info*** is a script to get information about the target user's contact number like Location (Country & City/Area), Carrier and Timezone.

***download_media*** is a script to download all the media present in the target user's chat.

---

## Installation

### Install whatsapp-play from PyPI: <br />
Windows: `python -m pip install wplay` <br />
Unix/Linux/Mac: `python3 -m pip install wplay` <br />
**Installation Video:** [Simple Installation Link](https://youtu.be/HS6ksu6rCxQ)

### Alternate way - Run whatsapp-play from source code: <br />
**Windows**<br />
```
$ git clone https://github.com/rpotter12/whatsapp-play.git
$ cd whatsapp-play
$ python -m pip install -r requirements.txt
$ python -m wplay -h
```

**Unix/Linux/Mac**<br />
```
$ git clone https://github.com/rpotter12/whatsapp-play.git
$ cd whatsapp-play
$ python3 -m pip install -r requirements.txt
$ python3 -m wplay -h
```

## Usage
<img src="images/usage.png"><br />

For detailed usage of command visit: [https://github.com/rpotter12/whatsapp-play/wiki/Usage](https://github.com/rpotter12/whatsapp-play/wiki/Usage)

## Contribute

The easiest way to contribute to **Whatsapp-Play** is by starring the repository and opening more and more [issues](https://github.com/rpotter12/whatsapp-play/issues) for features you'd like to see in future. <br />

First step is to create a fork and clone, then you can solve the [issues](https://github.com/rpotter12/whatsapp-play/issues) listed and help us find new ones. Then try debugging with Visual Studio Code it is necessary to create a launcher with the arguments. <br />

Steps to create a launcher with arguments follow the steps bellow: <br />
1. Click in 'Debug' tab
1. Click in 'Add Configuration'
1. Select 'Module'
1. Type 'wplay' and press Enter
1. A json file will be opened. Inside configurations add the args, for example: "args":["-wb","name"] 

**Debug Tutorial Video:** [Debug Tutorial Link](https://youtu.be/NyJgUGvyWnY)<br />
Check more about contribution guidelines [here](https://www.github.com/rpotter12/whatsapp-play/CONTRIBUTION.md)

## Disclaimer
This software is for educational purpose only. Keeping eye on a innocent person can make person's life stressful.

## License
[![License](https://img.shields.io/github/license/rpotter12/whatsapp-play.svg)](https://github.com/rpotter12/whatsapp-play/blob/master/README.md)

***If you like the project, support us by star***
## Face-X is a part of these open source programs❄

<p align="center">
  <a>
   <img  width="420" height="120"  src="https://miro.medium.com/max/2624/1*fqJaH_oISOR96gLgpJBwWQ.png">

</p>

</br>

## 🌟 Contributors 

Thanks to these wonderful people ✨✨:

<table>
	<tr>
		<td>
			<a href="https://github.com/rpotter12/whatsapp-play/graphs/contributors">
  				<img src="https://contrib.rocks/image?repo=rpotter12/whatsapp-play" />
			</a>
		</td>
	</tr>
</table>
