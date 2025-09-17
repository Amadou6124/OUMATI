
        // Filtrage des cours
        document.addEventListener('DOMContentLoaded', function() {
            const filterButtons = document.querySelectorAll('.filter-btn');
            const courseCards = document.querySelectorAll('.course-card');
            
            filterButtons.forEach(button => {
                button.addEventListener('click', function() {
                    // Retirer la classe active de tous les boutons
                    filterButtons.forEach(btn => {
                        btn.classList.remove('btn-primary');
                        btn.classList.add('btn-outline-primary');
                    });
                    
                    // Ajouter la classe active au bouton cliqué
                    this.classList.remove('btn-outline-primary');
                    this.classList.add('btn-primary');
                    
                    const filter = this.getAttribute('data-filter');
                    
                    // Afficher/masquer les cours en fonction du filtre
                    courseCards.forEach(card => {
                        if (filter === 'all') {
                            card.style.display = 'flex';
                        } else {
                            const status = card.getAttribute('data-status');
                            if (status === filter) {
                                card.style.display = 'flex';
                            } else {
                                card.style.display = 'none';
                            }
                        }
                    });
                    
                    // Masquer les titres de section si nécessaire
                    document.querySelectorAll('.section-title').forEach(title => {
                        const section = title.nextElementSibling;
                        const visibleCards = section.querySelectorAll('.course-card[style*="display: flex"]');
                        
                        if (visibleCards.length === 0) {
                            title.style.display = 'none';
                        } else {
                            title.style.display = 'block';
                        }
                    });
                });
            });
        });
    