# Normandy

Normandy is a personal assistant that uses speech recognition provided by Pocketsphinx and Houndify.


## Installation

Requirements: Python 3

**Linux/Mac Dependencies:**

```bash
./install.sh
```

**Houndify:**

Normandy uses Houndify for speech recognition beyond the keyword. Houndify provides a limited free developer account that you can use for limited API requests (100 per day).

Register for a free developer account in Houndify.

https://www.houndify.com/signup

[Navigate to your dashboard](https://www.houndify.com/dashboard) and [create a new client](https://www.houndify.com/applications/register?newClient=true). Choose "Desktop Application" as the platform.

Navigate to your client application and copy the Client ID and Client Key, paste into `config/config.json` under the `houndify` section.

## Usage

Run the application using the following command:

```bash
python3 normandy.py
```

Before issuing a command you must first say the keyword configured in `config/config.json`. By default this keyword is "computer".

You must speak the keyword first. The command can be spoken in the same sentence. You don't have to wait.

## Configuration

| Config property | Description |
|----------|------|
| houndify | A parent key for the Houndify configuration |
|   client_id | The Houndify client ID |
|   client_key | The Houndify client key |
| keyword | A spoken word to activate the assistant using offline recognition, and begin online recognition |

The `keyword` property should be a simple, easy to identify word. It's recommended to use one or two words at the most, 3 syllables or less. By default the keyword is "computer". The system may have trouble with heavy accents, so make sure the keyword is not affected by any accent. For instance, "computer" is often recognized as "come here" - these recognition errors are alleviated with a [Levenshtein](https://en.wikipedia.org/wiki/Levenshtein_distance) algorithm.

Houndify may recognize alternative languages to English, however the keyword interpreter (pocketsphinx) does not by default. If you wish to speak another language for the keyword, then choose an English word that most closely matches or rhymes with the other language.

**Commands**

Commands can be found in the `config/commands.json` file. The file is structured as an array with command objects.

```json
[
  {
    "utterance": "say hello",
    "command": "python3 tts.py 'hello'",
    "subprocess_options": []
  }
]
```

You would activate the command above with the following phase: "computer say hello". The command uses the tts.py component included in the project.

**Plugins**

Plugins can be found in the `plugins` folder (see Issue #1). These plugins are community developed and any additional dependency should be included in the `install.sh` file.

A plugin can be run by issuing a Python or Bash command in the command config.

```json
[
  {
    "utterance": "how are you feeling",
    "command": "python3 plugins/ps_stats.py",
    "subprocess_options": []
  },
  {
    "utterance": "what time is it",
    "command": "bash plugins/time.sh",
    "subprocess_options": []
  }
]
```
