import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
  
class TwitterClient(object): 
    ''' 
    คลาส Twitter ทั่วไปสำหรับการวิเคราะห์ความรู้สึก
    '''
    def __init__(self): 
        ''' 
        ตัวสร้าง Casls หรือวิธีการเริ่มต้น 
        '''
        # คีย์และโทเค็นจาก Twitter Dev Console
        consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXX'
        consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
  
        # พยายามตรวจสอบสิทธิ์ 
        try: 
            # สร้างวัตถุ OAuthHandler 
            self.auth = OAuthHandler(consumer_key, consumer_secret) 
            # ตั้งค่าโทเค็นการเข้าถึงและข้อมูลลับ
            self.auth.set_access_token(access_token, access_token_secret) 
            # สร้างวัตถุ tweepy API เพื่อดึงทวีต
            self.api = tweepy.API(self.auth) 
        except: 
            print("Error: Authentication Failed") 
  
    def clean_tweet(self, tweet): 
        ''' 
        ฟังก์ชั่นยูทิลิตี้เพื่อล้างข้อความทวีตโดยการลบลิงก์อักขระพิเศษ
        โดยใช้คำสั่ง regex อย่างง่าย
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) 
                                    |(\w+:\/\/\S+)", " ", tweet).split()) 
  
    def get_tweet_sentiment(self, tweet): 
        ''' 
        ฟังก์ชั่นยูทิลิตี้เพื่อจำแนกความรู้สึกของทวีตที่ส่งผ่าน
        โดยใช้วิธีความรู้สึกของ textblob
        '''
        # สร้างวัตถุ TextBlob ของข้อความทวีตที่ส่งผ่าน 
        analysis = TextBlob(self.clean_tweet(tweet)) 
        # ตั้งความเชื่อมั่น
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'
  
    def get_tweets(self, query, count = 10): 
        ''' 
        ฟังก์ชั่นหลักในการดึงทวีตและแยกวิเคราะห์
        '''
        #รายการว่างเพื่อจัดเก็บทวีตที่แยกวิเคราะห์ 
        tweets = [] 
  
        try: 
            #โทรหา twitter api เพื่อดึงทวีต
            fetched_tweets = self.api.search(q = query, count = count) 
  
            # แยกวิเคราะห์ทวีตทีละรายการ
            for tweet in fetched_tweets: 
                #พจนานุกรมที่ว่างเปล่าเพื่อจัดเก็บพารามิเตอร์ที่จำเป็นของทวีต 
                parsed_tweet = {} 
  
                # บันทึกข้อความของทวีต 
                parsed_tweet['text'] = tweet.text 
                # ประหยัดความรู้สึกของทวีต 
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 
  
                # ต่อท้ายทวีตที่แยกวิเคราะห์ไปยังรายการทวีต
                if tweet.retweet_count > 0: 
                    #หากทวีตมีการรีทวีตตรวจสอบให้แน่ใจว่ามีการต่อท้ายเพียงครั้งเดียว 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
  
            #ส่งคืนทวีตที่แยกวิเคราะห์
            return tweets 
  
        except tweepy.TweepError as e: 
            #ข้อผิดพลาดในการพิมพ์ (ถ้ามี)
            print("Error : " + str(e)) 
  
def main(): 
    #การสร้างวัตถุของ TwitterClient Class
    api = TwitterClient() 
    #ฟังก์ชั่นการโทรเพื่อรับทวีต
    tweets = api.get_tweets(query = 'Donald Trump', count = 200) 
  
    #เลือกทวีตเชิงบวกจากทวีต 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    #เปอร์เซ็นต์ของทวีตเชิงบวก 
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
    #เลือกทวีตเชิงลบจากทวีต 
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    #เปอร์เซ็นต์ของทวีตเชิงลบ
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
    #เปอร์เซ็นต์ของทวีตที่เป็นกลาง 
    print("Neutral tweets percentage: {} % \ 
        ".format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))) 
  
    #พิมพ์ทวีตในเชิงบวก 5 รายการแรก 
    print("\n\nPositive tweets:") 
    for tweet in ptweets[:10]: 
        print(tweet['text']) 
  
    #พิมพ์ทวีตเชิงลบ 5 รายการแรก
    print("\n\nNegative tweets:") 
    for tweet in ntweets[:10]: 
        print(tweet['text']) 
  
if __name__ == "__main__": 
    #เรียกใช้ฟังก์ชันหลัก
    main() 