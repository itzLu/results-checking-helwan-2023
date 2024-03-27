<h1 align="center">Results Notification Automation Script</h1>

<p align="center">
  <strong>A Python script to automate notifications for changes in departmental options and results.</strong>
</p>

## Features

- **Web Scraping**: Utilizes Selenium WebDriver to scrape departmental options from a designated webpage.
- **Change Detection**: Compares the current departmental options with previously known options to identify any updates.
- **Notification**: Sends notifications via Discord webhook to alert users about newly available departmental options.
- **Configuration**: Easily configurable with options stored in a JSON file for seamless integration and customization.

## Usage

1. Configure the script by editing the `known_options.json` file to specify the initial known options.
2. Update the `url` variable in the script to point to the target webpage containing departmental options.
3. Set up a Discord webhook URL for receiving notifications and update the `discord_webhook_url` variable in the script.
4. Run the script:

   ```bash
   python department_options_notifier.py
   ```

5. The script will scrape the webpage, compare the departmental options with the known options, and send notifications for any updates detected.

## Discord Server

For receiving notifications from this script, join our Discord server: [Results Notification Server](https://discord.gg/cxPNyPe82C)


