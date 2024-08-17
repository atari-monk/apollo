function addLinks() {
  const sidebar = document.getElementById('nav-links')
  const currentPath = window.location.pathname

  const homeLink =
    '<li><a href="https://atari-monk.github.io/apollo/">Home</a></li>'
  sidebar.innerHTML = homeLink

  const pathSegments = currentPath.split('/').filter(Boolean)

  if (pathSegments.length > 2) {
    const baseIndexPath = pathSegments.slice(0, -1).join('/')
    const indexLink = `<li><a href="https://atari-monk.github.io/apollo/${baseIndexPath}/">Current Folder Index</a></li>`
    sidebar.innerHTML += indexLink
  }
}

addLinks()
