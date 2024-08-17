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
document.body.classList.add('dark-mode')

function handleScroll() {
  const footer = document.getElementById('sidebar')
  const scrollPosition = window.scrollY + window.innerHeight
  const documentHeight = document.documentElement.scrollHeight

  if (scrollPosition >= documentHeight - 100) {
    // Show footer when near bottom
    footer.classList.add('show')
  } else {
    footer.classList.remove('show')
  }
}

// Check on scroll and resize
window.addEventListener('scroll', handleScroll)
window.addEventListener('resize', handleScroll) // Ensure footer adjusts on resize
handleScroll() // Initial check
