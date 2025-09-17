   document.addEventListener('DOMContentLoaded', function() {
            const searchInput = document.querySelector('.search-input');
            const resultsSection = document.querySelector('.results-section');
            const popularSearches = document.querySelector('.popular-searches');
            const categoriesList = document.querySelector('.categories-list');
            const filterBadges = document.querySelectorAll('.filter-badge');
            
            // Gestion de la recherche
            searchInput.addEventListener('keyup', function(e) {
                if (e.key === 'Enter' && this.value.trim() !== '') {
                    // Afficher les résultats et masquer les sections d'accueil
                    resultsSection.style.display = 'block';
                    popularSearches.style.display = 'none';
                    categoriesList.style.display = 'none';
                    
                    // Ici, vous ajouteriez la logique pour lancer la recherche
                    console.log('Recherche pour:', this.value);
                }
            });
            
            // Gestion des filtres
            filterBadges.forEach(badge => {
                badge.addEventListener('click', function() {
                    this.classList.toggle('active');
                    // Ici, vous ajouteriez la logique pour filtrer les résultats
                });
            });
            
            // Gestion des recherches populaires
            document.querySelectorAll('.popular-search-card').forEach(card => {
                card.addEventListener('click', function(e) {
                    e.preventDefault();
                    searchInput.value = this.textContent;
                    
                    // Afficher les résultats et masquer les sections d'accueil
                    resultsSection.style.display = 'block';
                    popularSearches.style.display = 'none';
                    categoriesList.style.display = 'none';
                    
                    // Ici, vous ajouteriez la logique pour lancer la recherche
                    console.log('Recherche populaire:', this.textContent);
                });
            });
        });
    