from Pytube import Youtube 

link = input("Entre the link : ")

video = Youtube(link)
stream = video.streams.get_highest_resolution()
stream.download()