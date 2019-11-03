# Genusswerk Menu Parser

This is a small tool to parse the weekly menu of [the cantine next to my office](https://das-genusswerk.at/).

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
---
## About

Takes a Genusswerk menu PDF and parses it into daily entries using [camelot]() 

Currently only prints the result

Future Plans

* Connect to a mail account to react to weekly newsletter
* Add Slack integration to post and allow querying of menu
