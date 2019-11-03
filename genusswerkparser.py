import argparse
import pdf_table_parser as parser
import os
#import slack

def handleMenu(path, sendToSlack=False, debug=False):
    week = parser.parsePdfMenu(path, debug)
    print (week)
    
    if sendToSlack:
       sendMenuToSlack(week)

def sendMenuToSlack(week):
    print('Slack integration not implemented yet')
#   slackToken = os.environ["SLACK_API_TOKEN"]
#   client = slack.WebClient(token=slackToken)
#    for menu in week.menus:
#        client.chat_postMessage(
#            channel = "",
#            text = str(menu)
#        )

if __name__ == '__main__': 
    path = 'sample.pdf' 
    
    argParser = argparse.ArgumentParser(description='Parse the Genusswerk weekly menu')
    argParser.add_argument('--file','-f', help='The Genusswerk menu pdf you want to parse')
    argParser.add_argument('--debug','-d', action='store_true', help='Show parsing debug information')
    argParser.add_argument('--send-to-slack', '-s', action='store_true', help='Send parsed menu to slack')
    args = argParser.parse_args()
    
    if (args.file):
        path = args.file
    handleMenu(path, args.send_to_slack, args.debug)
