### Embed Audio Options

1. **Embeding audio in GitHub pages.**

   Github pages use Jekyl to generate static web page.
   Markdown files are converted to html pages.  
   Below, exploring options to embed audio on page.

2. **OneDrive embeding**

   Move file to onedrive.  
   On onedrive page, generate embed iframe with link.  
   Tested link in some options.

   - Md Link

   [🔊 En](https://1drv.ms/u/c/37f44e52f80d7972/IQRoqaRxwZwHQp7DhgsZ1OuHAe1_SFLcJBV_GhykONj7804)

   - Need to open new tab, not convenient.

   - Audio html element

    <audio controls>
    <source src="https://1drv.ms/u/c/37f44e52f80d7972/IQRoqaRxwZwHQp7DhgsZ1OuHAe1_SFLcJBV_GhykONj7804" type="audio/mpeg">
    Your browser does not support the audio element.
    </audio>

   - Disabled player for some reason.

   - IFrame from OneDrive

    <iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQRoqaRxwZwHQp7DhgsZ1OuHAe1_SFLcJBV_GhykONj7804" width="200" height="120" frameborder="0" scrolling="no"></iframe>

   - I think this may work when one iframe per page.
     Tested with more, wasnt working well.

3. **Files on server**

   - Direct files on server.
     Works even with many players per page.
     Although, in markdown, one per page feels and look best.

   <audio controls>
   <source src="./../Morpheus_Documentation/audio_en/IRect.mp3" type="audio/mpeg">
   Your browser does not support the audio element.
   </audio>
