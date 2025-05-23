document.addEventListener('DOMContentLoaded', function() {
    // Back to top button
    const backToTop = document.getElementById('backToTop');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 200) {
        backToTop.style.display = 'block';
      } else {
        backToTop.style.display = 'none';
      }
    });
  
    backToTop.addEventListener('click', () => {
      window.scrollTo({top:0, behavior:'smooth'});
    });
  });
  