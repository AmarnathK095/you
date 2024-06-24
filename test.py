import streamlit as st
import mysql.connector
import pandas as pd
import mysql.connector

def act():
    channel()    
    video()
    comment()


st.title("YouTube Data Harvesting and Warehousing ")    # Title, caption header for streamlit page
with st.sidebar:
    st.title(":red[YOUTUBE DATA HARVESTING AND WAREHOUSING USING SQL AND STREAMLIT]")
    st.header("Problem Statement")
    st.caption(''':orange[The problem statement is to create a Streamlit application that allows users
                to access and analyze data from multiple YouTube channels tables in database.]''')
    st.header(":green[DATA TABLES]")

# Connect SQL workbench with streamlit
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="password",database="youtube")
mycursor = mydb.cursor()

# Get  channel details from the table in server
def channel():
    mycursor.execute("select * from youtube.channel1")
    out=mycursor.fetchall()
    headers=[i[0] for i in mycursor.description]
    yield pd.DataFrame(out,columns=['channelName','subcribers','views','totalvideo','playlistid','channel_description','channel_id',])


if st.sidebar.button("CHANNEL"):
    st.write(channel())

#Get video details from the table
def video():
    mycursor.execute("select * from youtube.video")
    out=mycursor.fetchall()
    headers=[i[0] for i in mycursor.description]
    yield pd.DataFrame(out,columns=['title','description','video_id','duration','channelName','views','published_date date','favourite_count','thumbnail','like_count','dislike_count','caption_status','comment_count','channel_id'])


if st.sidebar.button("video"):
    st.write(video())

#get the comment details 
def comment():
    mycursor.execute("select * from youtube.comment")
    out=mycursor.fetchall()
    headers=[i[0] for i in mycursor.description]
    yield pd.DataFrame(out,columns=['comment_id','video_id','comment_text','author_name','published_date','channel_id'])

if st.sidebar.button("comment"):
    st.write(comment())


# query questions are listed

questions=st.selectbox(":orange[SELECT QUESTION]",("select option",
        "1 . What are the names of all the videos and their corresponding channels?",
        "2 . Which channels have the most number of videos, and how many videos dothey have?",
        "3 . What are the top 10 most viewed videos and their respective channels?",
        "4 . How many comments were made on each video, and what are their corresponding video names?",
        "5 . Which videos have the highest number of likes, and what are their corresponding channel names?",
        "6 . What is the total number of likes and dislikes for each video, and what are their corresponding video names?",
        "7 . What is the total number of views for each channel, and what are their corresponding channel names?",
        "8 . What are the names of all the channels that have published videos in the year 2022?",
        "9 . What is the average duration of all videos in each channel, and what are their corresponding channel names?",
        "10 . Which videos have the highest number of comments, and what are their corresponding channel names?"))

if questions=="1 . What are the names of all the videos and their corresponding channels?":
    mycursor.execute('select channelName,title from youtube.video1')
    data=mycursor.fetchall()
    st.write(pd.DataFrame(data,columns=['channelName','vedio_Title']))

elif questions=="2 . Which channels have the most number of videos, and how many videos dothey have?":
    mycursor.execute('select channelName,totalvideo from youtube.channel order by totalvideo desc')
    data=mycursor.fetchall() 
    st.write(pd.DataFrame(data,columns=['Channel_Name','Vedio_Count']))

elif questions=="3 . What are the top 10 most viewed videos and their respective channels?":
    mycursor.execute('select channelName,title,views from youtube.video1 order by views desc limit 10 ')
    data=mycursor.fetchall()
    st.write(pd.DataFrame(data,columns=['CHANNEL','VEDIO','VIEWS'],index=[1,2,3,4,5,6,7,8,9,10]))

elif questions=="4 . How many comments were made on each video, and what are their corresponding video names?":
    mycursor.execute('select title,comment_count,channelName from youtube.video1')
    data=mycursor.fetchall()
    st.write(pd.DataFrame(data,columns=['VEDIO','COMMENT_COUNT','CHANNEL']))

elif questions=="5 . Which videos have the highest number of likes, and what are their corresponding channel names?":
    mycursor.execute('select channelName,title,like_count from youtube.video1 order by like_count desc')
    data=mycursor.fetchall()
    st.write(pd.DataFrame(data,columns=['CHANNEL','VEDIO_TITLE','LIKES_COUNT']))
elif questions=="6 . What is the total number of likes and dislikes for each video, and what are their corresponding video names?": 
    mycursor.execute('select title ,like_count ,dislike_count from youtube.video1')
    data=mycursor.fetchall()
    st.write(pd.DataFrame(data,columns=['VEDIO_TITLE','NO OF LIKES','NO OF DISLIKES']))
elif questions=="7 . What is the total number of views for each channel, and what are their corresponding channel names?":
    mycursor.execute('select channelName , views from youtube.channel')
    data=mycursor.fetchall()
    st.write(pd.DataFrame(data,columns=['CHANNEL NAME','VIEW COUNT']))
elif questions=="8 . What are the names of all the channels that have published videos in the year 2022?": 
    mycursor.execute('select channelName,title,published_date from youtube.video1 where extract(year from published_date)=2022')
    data=mycursor.fetchall()
    st.write(pd.DataFrame(data,columns=['CHANNEL NAME','VEDIO TITLE','VEDIO DATE']))
elif questions=="9 . What is the average duration of all videos in each channel, and what are their corresponding channel names?":
    mycursor.execute('select channelName,avg(duration) from youtube.video1 group by channelName')
    data=mycursor.fetchall()
    st.write(pd.DataFrame(data,columns=['CHANNEL NAME','VEDIO DURIATION in seconds']))
elif questions== "10 . Which videos have the highest number of comments, and what are their corresponding channel names?":
    mycursor.execute('select channelName,title,comment_count from youtube.video1 order by comment_count desc')
    data=mycursor.fetchall()
    st.write(pd.DataFrame(data,columns=['CHANNEL NAME','VEDIO TITLE','COMMENT COUNT']))



act()
