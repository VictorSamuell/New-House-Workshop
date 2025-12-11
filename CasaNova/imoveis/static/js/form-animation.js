// animação pro css
document.addEventListener('DOMContentLoaded', function() {
    const labels = document.querySelectorAll('.animated-label');
    
    labels.forEach(label => {
        const text = label.textContent;
        label.innerHTML = '';
        
        text.split('').forEach((char, index) => {
            const span = document.createElement('span');
            span.textContent = char;
            span.style.display = 'inline-block';
            span.style.transitionDelay = (index * 50) + 'ms';
            label.appendChild(span);
        });
    });
});
