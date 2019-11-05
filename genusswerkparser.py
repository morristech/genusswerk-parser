import menudownloader

import argparse
import pdf_table_parser as parser
import os
import slack
import subprocess

def handleMenu(path, useFullWeek=False, sendToSlack=False, notify=False, debug=False):
    if (path == None):
        success, filename = menudownloader.downloadCurrentMenu()
        if (success == False):
            print('Failed to download menu!')
            return
        path = filename

    week = parser.parsePdfMenu(path, debug)
    notification = str(week) if useFullWeek else str(week.getTodaysMenu())
    
    if (notification == None):
        print('But you could view the current week menu with the -w flag')
        return
    
    print(notification)
    
    if sendToSlack:
       sendMenuToSlack(notification)

    if notify:
        sendNotification(notification)

    menudownloader.cleanup()

def sendMenuToSlack(text):
    print('Slack integration not implemented yet')
    slackToken = os.environ["SLACK_API_TOKEN"]
    client = slack.WebClient(token=slackToken)
#    for menu in week.menus:
#        client.chat_postMessage(
#            channel = "",
#            text = text
#        )

def sendNotification(text):
    subprocess.Popen(['notify-send', '-i', 'Genusswerk Menu', text])

if __name__ == '__main__':    
    argParser = argparse.ArgumentParser(description='Parse the Genusswerk weekly menu')
    argParser.add_argument('--file','-f', help='The Genusswerk menu pdf you want to parse')
    argParser.add_argument('--week','-w', action='store_true', help='Return complete week, instead of todays menu')
    argParser.add_argument('--send-to-slack', '-s', action='store_true', help='Send parsed menu to slack')
    argParser.add_argument('--send-notification', '-n', action='store_true', help='Show parsed menu as notification')
    argParser.add_argument('--debug','-d', action='store_true', help='Show parsing debug information')
    args = argParser.parse_args()
    
    handleMenu(args.file, args.week, args.send_to_slack, args.send_notification, args.debug)
