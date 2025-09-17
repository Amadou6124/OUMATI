// Gestion du défilement horizontal et des indicateurs
document.addEventListener('DOMContentLoaded', function() {
    const scrollContainers = document.querySelectorAll('.horizontal-scroll');
    
    scrollContainers.forEach(container => {
        // Créer des indicateurs de défilement dynamiques si nécessaire
        initScrollIndicators(container);
        
        // Gérer le défilement avec snap
        container.addEventListener('scroll', function() {
            updateScrollIndicators(this);
        });
    });
});

function initScrollIndicators(container) {
    const indicator = container.nextElementSibling;
    if (indicator && indicator.classList.contains('scroll-indicator')) {
        const itemCount = container.children.length;
        // S'assurer que le nombre de points correspond au nombre d'éléments
        if (indicator.children.length !== itemCount) {
            indicator.innerHTML = '';
            for (let i = 0; i < itemCount; i++) {
                const dot = document.createElement('span');
                dot.classList.add('dot');
                if (i === 0) dot.classList.add('active');
                indicator.appendChild(dot);
            }
        }
    }
}

function updateScrollIndicators(container) {
    const indicator = container.nextElementSibling;
    if (indicator && indicator.classList.contains('scroll-indicator')) {
        const scrollPos = container.scrollLeft;
        const scrollWidth = container.scrollWidth - container.clientWidth;
        const itemCount = container.children.length;
        
        // Calculer l'élément actif basé sur la position de défilement
        const activeIndex = Math.round((scrollPos / scrollWidth) * (itemCount - 1));
        
        // Mettre à jour les indicateurs
        const dots = indicator.querySelectorAll('.dot');
        dots.forEach((dot, index) => {
            if (index === activeIndex) {
                dot.classList.add('active');
            } else {
                dot.classList.remove('active');
            }
        });
    }
}