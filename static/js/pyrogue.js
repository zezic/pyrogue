const keyBindings = [
  { keys: ['ArrowUp', 'w'], action: 'move', data: [ 0, -1 ] },
  { keys: ['ArrowLeft', 'a'], action: 'move', data: [ -1, 0 ] },
  { keys: ['ArrowDown', 's'], action: 'move', data: [ 0, 1 ] },
  { keys: ['ArrowRight', 'd'], action: 'move', data: [ 1, 0 ] }
]

class LevelRenderer {
  constructor ({ element }) {
    this.element = element
  }
  render (level) {
    const rowsElement = document.createElement('div')
    rowsElement.classList.add('rows')
    level.forEach(row => {
      const rowElement = document.createElement('div')
      rowElement.classList.add('row')
      row.forEach(char => {
        const charElement = document.createElement('span')
        charElement.innerText = char
        rowElement.appendChild(charElement)
      })
      rowsElement.appendChild(rowElement)
    })
    while (this.element.firstChild) {
      this.element.removeChild(this.element.firstChild)
    }
    this.element.appendChild(rowsElement)
  }
}

class PyRogueClient {
  constructor ({ levelElement }) {
    this.renderer = new LevelRenderer({ element: levelElement })
    this.bindKeys()
  }
  async fetchLevel () {
    const response = await fetch('/api/level')
    return await response.json()
  }
  async syncState () {
    const level = await this.fetchLevel()
    this.renderer.render(level)
  }
  async requestMove (magnitude) {
    try {
      await fetch('/api/walk', {
        method: 'POST',
        body: JSON.stringify({ magnitude })
      })
      await this.syncState()
    } catch (error) {
      alert(error)
    }
  }
  handleKeyDown (event) {
    const binding = keyBindings.find(binding => {
      return binding.keys.includes(event.key)
    })
    if (!binding) { return }
    if (binding.action === 'move') {
      this.requestMove(binding.data)
    }
  }
  bindKeys () {
    document.addEventListener('keydown', (event) => this.handleKeyDown(event))
  }
  async work () {
    await this.syncState()
  }
}

document.addEventListener('DOMContentLoaded', function(event) {
  const client = new PyRogueClient({
    levelElement: document.getElementsByClassName('level')[0]
  })
  client.work()
})
