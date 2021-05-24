const selected = document.querySelector('.movie-boxes')

function printEventData(e) {
  if (e.target.classList.contains('captured')) {
    e.target.classList.toggle('on')
  }
}

selected.addEventListener('mouseover', printEventData)
selected.addEventListener('mouseout', printEventData)