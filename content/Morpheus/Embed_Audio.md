### Embed Audio Options

1. **Embeding audio in GitHub pages.**

Github pages use Jekyl to generate static web page.
Markdown files are converted to html pages.  
Below, exploring options to embed audio on page.

2. **OneDrive embeding**

- Need to open new tab, not convenient.

  [🔊 En](https://1drv.ms/u/c/37f44e52f80d7972/IQRoqaRxwZwHQp7DhgsZ1OuHAe1_SFLcJBV_GhykONj7804)

- Disabled player for some reason.

<audio controls>
  <source src="https://1drv.ms/u/c/37f44e52f80d7972/IQRoqaRxwZwHQp7DhgsZ1OuHAe1_SFLcJBV_GhykONj7804" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

- This kind of works.  
  After more tests resigned from this.  
  It loads or not, quite randomly.  
  Instead directly storing audio in repo.

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQRoqaRxwZwHQp7DhgsZ1OuHAe1_SFLcJBV_GhykONj7804" width="200" height="120" frameborder="0" scrolling="no"></iframe>

3. **Files on server**

- Direct files on server.

<audio controls>
  <source src="./../Morpheus_Documentation/audio_en/IRect.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>
