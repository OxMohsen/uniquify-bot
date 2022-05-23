<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL3 License][license-shield]][license-url]


<br />
<div align="center">
  <a href="https://github.com/OxMohsen/uniquify-bot">
    <img src="https://img.apksum.com/4c/com.duplicate.files.remover.duplicatefinderfiles/1.0/icon.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">uniquify bot</h3>

  <p align="center">
    Uniquify bot is a Telegram bot that deletes duplicate files (Video, Audio, Photo, Voice, and Document) from target chat.
    <br />
    <a href="https://github.com/OxMohsen/uniquify-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/OxMohsen/uniquify-bot/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



## About The Project

uniquify bot will help you to find and delete duplicate files in your channel or group.
this bot uses `file_unique_id` to find duplicate files, so we can assure you that there is the same file as the deleted file in your group or channel.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [pyrogram](https://pyrogram.org/)

<p align="right">(<a href="#top">back to top</a>)</p>


## Getting Started

To get a local copy up and running follow these simple example steps.

### Installation

1. Get your `api_id` and `api_hash` in [https://my.telegram.org](https://my.telegram.org)
2. Create a new bot in [https://t.me/botfather](https://t.me/botfather)
3. Clone the repo
   ```sh
   git clone https://github.com/OxMohsen/uniquify-bot.git
   ```
4. navigate into the new folder
   ```sh
   cd uniquify-bot
   ```
5. Install python packages
   ```sh
   pip3 install -r requirements.txt
   ```
5. rename the `sample-config.py` to `config.py`
6. fill the `config.py` with your data
7. run the bot
   ```sh
   python3 main.py
   ```

if you using heroku, you can run the bot with the following steps.
1. get your `api_id` and `api_hash` in [https://my.telegram.org](https://my.telegram.org)
2. create a new bot in [https://t.me/botfather](https://t.me/botfather)
3. press the following button:
    <br><a href="https://heroku.com/deploy?template=https://github.com/OxMohsen/uniquify-bot">
    <img height="30px" src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku">
    </a>


<p align="right">(<a href="#top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


## License

Distributed under the GPLv3 License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


## Contact

Your Name - [@OxMohsen](https://twitter.com/OxMohsen) - oxmohsen@oxmohsen.ir

Project Link: [https://github.com/OxMohsen/uniquify-bot](https://github.com/OxMohsen/uniquify-bot)

<p align="right">(<a href="#top">back to top</a>)</p>


[contributors-shield]: https://img.shields.io/github/contributors/OxMohsen/uniquify-bot.svg?style=for-the-badge
[contributors-url]: https://github.com/OxMohsen/uniquify-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/OxMohsen/uniquify-bot.svg?style=for-the-badge
[forks-url]: https://github.com/OxMohsen/uniquify-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/OxMohsen/uniquify-bot.svg?style=for-the-badge
[stars-url]: https://github.com/OxMohsen/uniquify-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/OxMohsen/uniquify-bot.svg?style=for-the-badge
[issues-url]: https://github.com/OxMohsen/uniquify-bot/issues
[license-shield]: https://img.shields.io/github/license/OxMohsen/uniquify-bot.svg?style=for-the-badge
[license-url]: https://github.com/OxMohsen/uniquify-bot/blob/main/LICENSE