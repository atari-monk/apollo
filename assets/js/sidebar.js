function addLinks() {
  const sidebar = document.getElementById('nav-links')
  const currentPath = window.location.pathname
  const homeLink =
    '<li><a href="https://atari-monk.github.io/apollo/">Home</a></li>'
  sidebar.innerHTML = homeLink

  const pathSegments = currentPath.split('/').filter(Boolean)
  const apolloIndex = pathSegments.indexOf('apollo')
  const relevantSegments = pathSegments.slice(apolloIndex + 1)

  if (relevantSegments.length > 0) {
    const baseIndexPath = relevantSegments.join('/')
    const indexLink = `<li><a href="https://atari-monk.github.io/${baseIndexPath}/">Current Folder Index</a></li>`
    sidebar.innerHTML += indexLink
  }
}

addLinks()
