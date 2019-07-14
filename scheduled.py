import os
import schedule
import time
import logging
from slack import WebClient

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

def sendMessage(slack_client, msg):
  # make the POST request through the python slack client
  updateMsg = slack_client.chat_postMessage(
    channel='#nwsl-schedule',
    text=msg
  )

  # check if the request was a success
  if updateMsg['ok'] is not True:
    logging.error(updateMsg)
  else:
    logging.debug(updateMsg)

if __name__ == "__main__":
  SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
  slack_client = WebClient(token=SLACK_BOT_TOKEN)
  logging.debug("authorized slack client")

  # # For testing
  msg = "Ahoy thirsty soccer fans!"
  sendMessage(slack_client, msg)
  #schedule.every(60).seconds.do(lambda: sendMessage(slack_client, msg))

  # schedule.every().monday.at("13:15").do(lambda: sendMessage(slack_client, msg))
  #logging.info("entering loop")

  #while True:
  #  schedule.run_pending()
  #  time.sleep(5) # sleep for 5 seconds between checks on the scheduler
