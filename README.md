# Genusswerk Menu Parser

This is a small tool to parse the weekly menu of [the canteen next to my office](https://das-genusswerk.at/).

This is what a bored engineer does, after the joking question "Did you parse the PDF?" stays with him over the weekend.

---
## Dependencies

Uses python3, and the following libaries:

[camelot](https://camelot-py.readthedocs.io/en/master/)
[matplotlib](https://matplotlib.org/)
[slackclient](https://github.com/slackapi/python-slackclient)

Camelot depends on `python3-tk` and `ghostscript`, so install these, and then

```
pip install camelot-py[cv] matplotlib slackclient
```
### Docker Alternative

Alternatively use the WIP Dockerfile to build a waaaay to large docker image.

Image allows for same options as running directly

---
## About

Takes a Genusswerk menu PDF and parses it into daily entries using [camelot]() 

**Usage**: See output of `python genusswerkparser.py -h`

**Slack Integration**: 
Using `-s` slack integration requires `SLACK_API_TOKEN` and `SLACK_CHANNEL` set as env vars.


## Future Plans

* Put into a container in which it runs weekly or daily to notify of today's menu
* Add volume for container to allow caching menus
* Add Slack integration to allow querying of menu
