from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json


import errno
import os
import sys, random
import tempfile

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('nBOZlu9u30ITxAt1tZXkbvAHsgb2/EIHhBo8mwuzg/dqIAhJNjqW/A97MBf2lX2B+5L7NicAQYMLSJh6vw/MZ6Gpsbbj1am/jIHH18e9azTknd/6Jxi2qFEMMFlmrrjHixXEE4hQKCkJw/DbNW7z9gdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('7bc5b547eb74a52213c4e88af08da151')
#===========[ NOTE SAVER ]=======================
notes = {}

# Post Request
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get user_id
    gid = event.source.sender_id #get group_id
#=====[ LEAVE GROUP OR ROOM ]==========
    if text == '/bye':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Leaving group'))
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Leaving group'))
            line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
            #=====[ CAROUSEL MESSAGE ]==========
    elif text == '@jp1':
        message = TemplateSendMessage(
            alt_text='Jadwal Pelajaran',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title='Senin',
                        text='Sedang Tahap pengerjaan',
                        actions=[
                            URITemplateAction(
                                label='Creator',
                                uri='https://line.me/ti/p/~rhnprmd'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Selasa',
                        text='Sedang Tahap pengerjaan',
                        actions=[
                            URITemplateAction(
                                label='Creator',
                                uri='https://line.me/ti/p/~rhnprmd'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Rabu',
                        text='Sedang Tahap pengerjaan',
                        actions=[
                            URITemplateAction(
                                label='Creator',
                                uri='https://line.me/ti/p/~rhnprmd'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Kamis',
                        text='Sedang Tahap pengerjaan',
                        actions=[
                            URITemplateAction(
                                label='Creator',
                                uri='https://line.me/ti/p/~rhnprmd'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#=====[ FLEX MESSAGE ]==========
#=====[ CAROUSEL MESSAGE ]==========
    elif text == '/test':
        image_carousel_template_message = TemplateSendMessage(
            alt_text='ImageCarousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://c.pxhere.com/images/a8/90/fce6814d341b7ed50a522418df04-1440147.jpg!d',
                        action=PostbackAction(
                            label='postback1',
                            text='postback text1',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://c.pxhere.com/images/41/89/db5bad17f91dd0186f117bd56b5b-1445355.jpg!d',
                        action=PostbackAction(
                            label='postback2',
                            text='postback text2',
                            data='action=buy&itemid=2'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, image_carousel_template_message)
#=====[ FLEX MESSAGE ]==========
#=====[ TEMPLATE MESSAGE ]=============
    elif text == '/menu':
        buttons_template = TemplateSendMessage(
            alt_text='Menu Bot',
            template=ButtonsTemplate(
                title='Menu Bot',
                text= 'Tap the Button',
                actions=[
                    MessageTemplateAction(
                        label='Info',
                        text='/info'
                    ),
                    MessageTemplateAction(
                        label='Sosial media',
                        text='/sosmed'
                    ),
                    MessageTemplateAction(
                        label='Bot out!!!',
                        text='/bye'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)
#=====[ CAROUSEL MESSAGE ]==========
    elif text == '/sosmed':
        message = TemplateSendMessage(
            alt_text='SosialMedia',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title='Instagram',
                        text='Follow instagram kami!!!',
                        actions=[
                            URITemplateAction(
                                label='Instagram',
                                uri='https://www.instagram.com/osistrikabta'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Line',
                        text='Add line kami!!!',
                        actions=[
                            URITemplateAction(
                                label='Line',
                                uri='https://line.me/ti/p/~@xqk3695y'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#=====[ FLEX MESSAGE ]==========
    elif text == '/info':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://instagram.fcgk2-1.fna.fbcdn.net/vp/508aca5ef58a753abbbe920f4a983fc0/5C18895F/t51.2885-19/s150x150/23735022_1795261150771794_2580732426670047232_n.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='https://www.instagram.com/osistrikabta', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='OSIS SMA NEGERI 3 TANGERANG', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/grey_star.png'),
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/grey_star.png'),
                            TextComponent(text='4.0', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Place',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Tangerang, Indonesia',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Info',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="Untuk informasi lebih lanjut silahkan follow instagram @osistrikabta",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Follow Instagram', uri="https://www.instagram.com/osistrikabta")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="hello", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
#=======================================================================================================================
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
