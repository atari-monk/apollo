function addLinks() {
  const sidebar = document.getElementById('nav-links')
  const currentPath = window.location.pathname

  const homeLink =
    '<li><a href="https://atari-monk.github.io/apollo/">Home</a></li>'
  sidebar.innerHTML = homeLink

  const pathSegments = currentPath.split('/').filter(Boolean)

  const lastSegment = pathSegments[pathSegments.length - 1]
  const filePattern = /^file\d{3}\.html$/

  if (filePattern.test(lastSegment)) {
    const baseIndexPath = pathSegments.slice(0, -1).join('/')
    const indexLink = `<li><a href="https://atari-monk.github.io/${baseIndexPath}/">Index</a></li>`
    sidebar.innerHTML += indexLink
  }
}

addLinks()
function toggleDarkMode() {
  const currentMode = localStorage.getItem('dark-mode') === 'true'
  document.body.classList.toggle('dark-mode', !currentMode)
  localStorage.setItem('dark-mode', !currentMode)
}

addLinks()
if (localStorage.getItem('dark-mode') === 'true') {
  document.body.classList.add('dark-mode')
}

const darkModeButton = document.getElementById('dark-mode-toggle')
if (darkModeButton) {
  darkModeButton.addEventListener('click', toggleDarkMode)
}
