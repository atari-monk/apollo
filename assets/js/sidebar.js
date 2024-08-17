function getCurrentFolderLevel() {
  const pathArray = window.location.pathname.split('/')
  const folderLevel = pathArray.length - 2
  return folderLevel
}

function addLinks() {
  const sidebar = document.getElementById('nav-links')
  const path = window.location.pathname
  const folderLevel = getCurrentFolderLevel()

  let homeLink = ''
  let indexLink = ''
  let mainLink = ''

  if (folderLevel === 1) {
    homeLink = `<li><a href="../../../index.md">Home</a></li>`
  } else if (folderLevel === 2) {
    indexLink = `<li><a href="index.md">Index</a></li>`
    mainLink = `<li><a href="../../../index.md">Main</a></li>`
  } else if (folderLevel > 2) {
    indexLink = `<li><a href="../index.md">Index</a></li>`
    mainLink = `<li><a href="../../../index.md">Main</a></li>`
  }

  sidebar.innerHTML = `
        ${homeLink}
        ${indexLink}
        ${mainLink}
    `
}

addLinks()
