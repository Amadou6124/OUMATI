/**
 * Script principal pour l'application Fiqh
 * Gère la navigation et les interactions utilisateur
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialisation de la navigation
    initNavigation();
    
    // Gestion des notifications
    initNotifications();
});

/**
 * Initialise la navigation et les effets visuels
 */
function initNavigation() {
    const navItems = document.querySelectorAll('.nav-item');
    const currentPage = getCurrentPage();
    
    // Active l'élément de navigation correspondant à la page actuelle
    navItems.forEach(item => {
        if (item.getAttribute('data-page') === currentPage) {
            item.classList.add('active');
        }
        
        item.addEventListener('click', function(e) {
            // Animation de clic
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = '';
            }, 200);
        });
    });
}

/**
 * Détermine la page actuelle basée sur l'URL
 * @returns {string} Le nom de la page actuelle
 */
function getCurrentPage() {
    const path = window.location.pathname;
    if (path.includes('explore')) return 'explore';
    if (path.includes('learning')) return 'learning';
    if (path.includes('profile')) return 'profile';
    return 'home'; // Par défaut
}

/**
 * Initialise la gestion des notifications
 */
function initNotifications() {
    const notificationIcon = document.querySelector('.nav-icon');
    
    if (notificationIcon) {
        notificationIcon.addEventListener('click', function(e) {
            e.preventDefault();
            toggleNotifications();
        });
    }
}

/**
 * Bascule l'affichage des notifications (à implémenter)
 */
function toggleNotifications() {
    // Implémentation future pour afficher les notifications
    console.log('Affichage des notifications');
}

/**
 * Affiche un message de bienvenue avec le nom de l'utilisateur
 */
function showWelcomeMessage() {
    const userName = document.querySelector('.user-name').textContent;
    if (userName && userName !== 'Invité') {
        console.log(`Bienvenue ${userName} dans FiqhApp!`);
    }
}

// Appel de la fonction de bienvenue
showWelcomeMessage();