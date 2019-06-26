window.addEventListener('scroll', () => {
   let nav = document.getElementById('navbr');
   nav.style.backgroundColor = 'rgba(255,255,255,' + (1/(1+Math.pow(2,-18*(window.pageYOffset/window.innerHeight)+7)) * 1).toFixed(2) + ')';
}, false);
