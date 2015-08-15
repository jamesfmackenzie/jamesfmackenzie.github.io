---
layout: post
title: Use Plex to Stream Almost Any Video From PC to Xbox One
date: '2014-04-09 18:29:00'
categories: stream_to_xbone
permalink: /:title
---

Last time, [I suggested we could use Plex Media Server to stream almost any video from PC to Xbox One](/plex-to-the-rescue/). Here's how to actually do it.

###Install Plex 

I won't go into great detail on this since it's already [documented on the Plex website](https://plexapp.zendesk.com/hc/en-us/articles/200380843-Overview), but here's how to setup Plex Media Server:

1. [Download Plex Media Server](https://plex.tv/downloads).
2. [Install it on your PC](https://plexapp.zendesk.com/hc/en-us/articles/200288586-Installation).
3. [Open the Plex Media Manager](http://localhost:32400/web/index.html#!/dashboard).
3. [Set up a media library](https://plexapp.zendesk.com/hc/en-us/articles/200288926-Creating-Libraries), pointing it to the Videos folder on your PC.
4. Turn on DLNA via <code>Settings -> Plex Media Server -> DLNA -> DLNA enabled</code>:

![Turning on Plex DLNA](/img/posts/2014_03_17_21_01_27_Plex_Web.png)

###Create a Windows DLNA media profile

Create a new file called <code>Windows DLNA.xml</code> with the content below. Save it in <code>C:\Program Files (x86)\Plex\Plex Media Server\Resources\Profiles</code>.

    <?xml version="1.0" encoding="utf-8"?>
    <Client name="Windows DLNA">
      <!-- Save as Windows DLNA.xml in C:\Program Files (x86)\Plex\Plex Media Server\Resources\Profiles -->
      <Identification>
          <!-- Uniquely identify Windows 8 DLNA client via User-Agent -->
          <Header name="User-Agent" substring="Microsoft-DLNA DLNADOC" />
        </Identification>
      <TranscodeTargets>
        <VideoProfile protocol="http" container="mpegts" codec="h264" audioCodec="aac,ac3,eac3" context="streaming">
          <Setting name="VideoEncodeFlags" value="-x264opts cabac=0" />
          <Setting name="SubtitleSize" value="100" />
        </VideoProfile>
        <VideoProfile protocol="slss" container="mp4" codec="h264" audioCodec="aac" context="streaming">
          <Setting name="VideoEncodeFlags" value="-x264opts cabac=0:keyint=50:min_keyint=50:scenecut=0" />
          <Setting name="SubtitleSize" value="100" />
          <Setting name="AudioSyncFlags" value="3" />
        </VideoProfile>
        <VideoProfile protocol="hls" container="mpegts" codec="h264" audioCodec="aac" context="streaming">
          <Setting name="VideoEncodeFlags" value="-x264opts cabac=1:level=41" />
          <Setting name="SubtitleSize" value="100" />
        </VideoProfile>
        <VideoProfile container="mp4" codec="h264" audioCodec="aac,ac3,eac3" context="static" />
        <MusicProfile container="mp3" codec="mp3" />
        <PhotoProfile container="jpeg" />
      </TranscodeTargets>
      <DirectPlayProfiles>
        <!-- Notice no .mkv in here. This means it will always be transcoded instead of being sent to the Windows 8 client directly -->
        <VideoProfile container="mp4,mov" codec="h264,mpeg4" audioCodec="aac,ac3,eac3,mp3,pcm" />
        <VideoProfile container="mpegts" codec="h264" audioCodec="aac,ac3,eac3,mp3,mp2,pcm" />
        <VideoProfile container="asf" codec="wmv2,wmv3,vc1" audioCodec="wmav2,wmapro,wmavoice" />
        <VideoProfile container="avi" codec="mpeg4,msmpeg4,mjpeg" audioCodec="mp3,ac3,eac3,mp2,pcm" />
        <MusicProfile container="asf" codec="wmav2,wmapro,wmavoice" />
        <MusicProfile container="mp4" codec="aac" />
        <MusicProfile container="mp3" codec="mp3" />
        <PhotoProfile container="jpeg" />
      </DirectPlayProfiles>
      <CodecProfiles>
        <VideoAudioCodec name="aac,eac3">
          <Limitations>
            <UpperBound name="audio.channels" value="8" />
          </Limitations>
        </VideoAudioCodec>
        <VideoAudioCodec name="ac3">
          <Limitations>
            <UpperBound name="audio.channels" value="6" />
          </Limitations>
        </VideoAudioCodec>
      </CodecProfiles>
      <TranscodeTargetProfiles>
        <VideoTranscodeTarget protocol="*" context="all">
          <VideoCodec name="*">
            <Limitations>
              <!-- Windows doesn't appear to play 10-bit h264 -->
              <UpperBound name="video.bitDepth" value="8" isRequired="false" />
            </Limitations>
          </VideoCodec>
        </VideoTranscodeTarget>
      </TranscodeTargetProfiles>
    </Client>

###Create an Xbox One DLNA media profile

Create another new file called <code>Xbox One.xml</code> with the content below. Save it in <code>C:\Program Files (x86)\Plex\Plex Media Server\Resources\Profiles</code>.

    <?xml version="1.0" encoding="utf-8"?>
    <Client name="Xbox One">
      <!-- Save as Xbox One.xml in C:\Program Files (x86)\Plex\Plex Media Server\Resources\Profiles -->
      <!-- Note: this profile is heavily based on the Xbox 360 profile. There's likely room for improvement here -->
      <Identification>
        <Header name="User-Agent" substring="NSPlayer" />
      </Identification>
      <DeviceDescription>
        <ModelName>Windows Media Player Sharing</ModelName>
        <ModelNumber>12.0</ModelNumber>
        <ModelUrl>http://www.microsoft.com/</ModelUrl>
        <Manufacturer>Microsoft Corporation</Manufacturer>
        <ManufacturerUrl>http://www.microsoft.com/</ManufacturerUrl>
        <X-DlnaDoc>DMS-1.50</X-DlnaDoc>
        <X-DlnaCap />
      </DeviceDescription>
      <TranscodeTargets>
        <VideoProfile container="mpegts" codec="h264" audioCodec="ac3">
        </VideoProfile>
        <MusicProfile container="mp3" codec="mp3" />
        <PhotoProfile container="jpeg" />
      </TranscodeTargets>
      <DirectPlayProfiles>
        <VideoProfile container="mpegts" codec="h264" audioCodec="ac3" />
        <VideoProfile container="avi" codec="mpeg4" audioCodec="ac3,mp3" />
        <VideoProfile container="avi" codec="h264" audioCodec="aac" />
        <VideoProfile container="mp4,mov" codec="h264,mpeg4" audioCodec="aac,ac3" />
        <VideoProfile container="asf" codec="wmv2,wmv3,vc1" audioCodec="wmav2,wmapro" />
        <MusicProfile container="asf" codec="wmav2,wmapro,wmavoice" />
        <MusicProfile container="mp3" codec="mp3" />
        <PhotoProfile container="jpeg" />
      </DirectPlayProfiles>
      <CodecProfiles>
        <VideoCodec name="mpeg4">
          <Limitations>
            <UpperBound name="video.frameRate" value="30" isRequired="false" />
            <UpperBound name="video.bitrate" value="5120" isRequired="false" />
          </Limitations>
        </VideoCodec>
        <VideoCodec name="h264">
          <Limitations>
            <UpperBound name="video.width" value="1920" />
            <UpperBound name="video.height" value="1080" />
          </Limitations>
        </VideoCodec>
        <VideoCodec name="wmv2,wmv3,vc1">
          <Limitations>
            <UpperBound name="video.width" value="1920" />
            <UpperBound name="video.height" value="1080" />
            <!-- FPS upper bound takes care of requirement that advanced profile level be <= 3 -->
            <UpperBound name="video.frameRate" value="30" isRequired="false" />
            <UpperBound name="video.bitrate" value="15360" isRequired="false" />
          </Limitations>
        </VideoCodec>
        <VideoAudioCodec name="ac3,wmav2,wmapro">
          <Limitations>
            <UpperBound name="audio.channels" value="6" isRequired="false" />
          </Limitations>
        </VideoAudioCodec>
        <VideoAudioCodec name="aac">
          <Limitations>
            <UpperBound name="audio.channels" value="2" isRequired="false" />
            <Match name="audio.profile" value="lc" isRequired="false" />
          </Limitations>
        </VideoAudioCodec>
      </CodecProfiles>
      <ContainerProfiles>
        <VideoContainer name="mp4,mov">
          <Limitations>
            <!-- Microsoft doesn't document this, but it appears to be true -->
            <Match name="part.has64bitOffsets" value="0" isRequired="false" />
          </Limitations>
        </VideoContainer>
      </ContainerProfiles>
      <DlnaMediaProfiles>
        <DlnaVideoProfile container="avi" mimeType="video/avi" />
      </DlnaMediaProfiles>
    </Client>

###Restart Plex

1. Shut down Plex Media Server (you can find the icon in your Task Tray).
2. Restart Plex Media Server from your Start Menu / Start Screen.

###Stream your content! 

After restarting Plex, you should see a "Plex Media Server" icon in Windows Explorer:

![Plex Explorer icon](/img/posts/2014_03_17_20_24_56_This_PC.png)

If you can't see it, you might need to:

1. Open Windows Explorer.
2. Navigate to <code>Computer -> Access Media</code>.
3. Click on <code>Connect to a media server</code>:

![Connect to a media server](/img/posts/2014_03_17_22_19_41_This_PC-1.png)

One the icon appears, find your content and stream it to your One:

![playtomkv](/img/posts/2014_03_18_00_35_32_Wonders_of_the_Solar_System.png)

![Xbox One Play To with mkv](/img/posts/tv.jpg)

Easy!

###What about subtitles?

Enabling subtitles is pretty easy. Whilst on the PC:

1. Open the [Plex Media Manager](http://localhost:32400/web/index.html#!/dashboard).
2. Find the show you want to enable subtitles for, hit the drop-down next to "SUBTITLES" and make a language selection:

![Enabling subtitles](/img/posts/2014_03_19_19_16_36_Plex_Web.png)

That's it! The subtitles will be rendered next time you Play To.

###How does it work?

If you're interested, here's how it works.

* The Windows DLNA profile ensures that Plex only sends the Windows DLNA client file formats it supports Play To for. Any unsupported file formats will be converted to supported ones on-the-fly.

In the logfile extract below, Plex detects that Windows 8 doesn't support  <code>mkv/h264/aac</code> and remuxes (converts) it:

    **[From %localappdata%\Plex Media Server\Logs\Plex DLNA Server.log]**
    Mar 17, 2014 21:36:28:973 [7484] DEBUG - Mapped client to profile Windows DLNA using header User-Agent: Microsoft-Windows/6.3 UPnP/1.0 Microsoft-DLNA DLNADOC/1.50
    Mar 17, 2014 21:36:35:097 [9048] DEBUG - MDE: E26 - World of Dreams: mkv/h264/aac is not a directplay video profile
    Mar 17, 2014 21:36:35:097 [9048] DEBUG - MDE: remuxing h264 video stream
    Mar 17, 2014 21:36:35:097 [9048] DEBUG - MDE: remuxing aac audio stream

* The Xbox One profile ensures that Plex only send the One file formats it can successfully stream. Again, unsupported formats are converted on the fly.

In the logfile extract below, Plex detects the Xbox One client ensures any unsupported video is converted before being sent:

    **[From %localappdata%\Plex Media Server\Logs\Plex DLNA Server.log]**
    Mar 17, 2014 22:07:41:030 [6120] DEBUG - Mapped client to profile Xbox One using header User-Agent: NSPlayer/12.00.9600.16411 WMFSDK/12.00.9600.16411
    
That's it!