function addLinks() {
  const sidebar = document.getElementById('nav-links')
  const currentPath = window.location.pathname

  if (currentPath === '/apollo/' || currentPath === '/apollo/index.html') {
    return
  }

  const homeLink =
    '<li><a href="https://atari-monk.github.io/apollo/">Index</a></li>'
  sidebar.innerHTML = homeLink

  const pathSegments = currentPath.split('/').filter(Boolean)

  const lastSegment = pathSegments[pathSegments.length - 1]
  const filePattern = /\.html$/

  if (filePattern.test(lastSegment)) {
    const baseIndexPath = pathSegments.slice(0, -1).join('/')
    const indexLink = `<li><a href="https://atari-monk.github.io/${baseIndexPath}/">Index</a></li>`
    sidebar.innerHTML += indexLink
  }
}

addLinks()
if (
  window.location.pathname !== '/apollo/' &&
  window.location.pathname !== '/apollo/index.html'
) {
  document.body.classList.add('dark-mode')
}

function handleScrollForSidebar() {
  const footer = document.getElementById('sidebar')
  const scrollPosition = window.scrollY + window.innerHeight
  const documentHeight = document.documentElement.scrollHeight

  if (
    window.location.pathname === '/apollo/' ||
    window.location.pathname === '/apollo/index.html'
  ) {
    return
  }

  if (scrollPosition >= documentHeight - 100) {
    footer.classList.add('show')
  } else {
    footer.classList.remove('show')
  }
}

window.addEventListener('scroll', handleScrollForSidebar)
window.addEventListener('resize', handleScrollForSidebar)
handleScrollForSidebar()
