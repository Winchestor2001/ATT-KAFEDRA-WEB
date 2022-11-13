let prog = document.querySelectorAll('.prog')
prog.forEach(progress =>{
    progress.style.cssText = `--value:${progress.getAttribute('data-progress')}`
})
