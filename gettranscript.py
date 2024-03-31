from youtube_transcript_api import YouTubeTranscriptApi
import summ

video_id = "R3wwUt5kKjg"
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

#transcript = transcript_list.find_manually_created_transcript(['de', 'en'])
transcript = transcript_list.find_generated_transcript(['tr']).fetch()

subtitles = ""
for subtitle in transcript:
    subtitles += " "+subtitle['text']

print(summ.summarize(subtitles,10))