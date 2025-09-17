/**
 * Script pour la page de profil FiqhApp
 * Gère les interactions de la page de profil
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialisation des fonctionnalités
    initFAQ();
    initDeleteAccountButton();
    initFormSubmissions();
});

/**
 * Initialise le système FAQ (questions/réponses)
 */
function initFAQ() {
    const faqQuestions = document.querySelectorAll('.faq-question');
    
    faqQuestions.forEach(question => {
        question.addEventListener('click', function() {
            const faqId = this.getAttribute('data-faq');
            const answer = document.getElementById(`faq-${faqId}`);
            const icon = this.querySelector('i');
            
            // Fermer toutes les autres réponses FAQ
            document.querySelectorAll('.faq-answer').forEach(ans => {
                if (ans.id !== `faq-${faqId}` && ans.classList.contains('show')) {
                    ans.classList.remove('show');
                    const otherIcon = ans.previousElementSibling.querySelector('i');
                    if (otherIcon) {
                        otherIcon.classList.remove('fa-chevron-up');
                        otherIcon.classList.add('fa-chevron-down');
                    }
                }
            });
            
            // Basculer l'affichage de la réponse
            answer.classList.toggle('show');
            
            // Changer l'icône
            if (answer.classList.contains('show')) {
                icon.classList.remove('fa-chevron-down');
                icon.classList.add('fa-chevron-up');
            } else {
                icon.classList.remove('fa-chevron-up');
                icon.classList.add('fa-chevron-down');
            }
        });
    });
}

/**
 * Initialise le bouton de suppression de compte
 */
function initDeleteAccountButton() {
    const deleteBtn = document.getElementById('deleteAccountBtn');
    
    if (deleteBtn) {
        deleteBtn.addEventListener('click', function(e) {
            e.preventDefault();
            
            if (confirm('Êtes-vous sûr de vouloir demander la suppression de votre compte ? Cette action est irréversible.')) {
                // Envoyer une demande de suppression de compte
                requestAccountDeletion();
            }
        });
    }
}

/**
 * Simule l'envoi d'une demande de suppression de compte
 */
function requestAccountDeletion() {
    // Ici, vous enverriez normalement une requête AJAX à votre backend
    console.log('Demande de suppression de compte envoyée');
    
    // Afficher un message de confirmation
    alert('Votre demande de suppression de compte a été envoyée. Notre équipe vous contactera sous peu.');
}

/**
 * Initialise les soumissions de formulaires
 */
function initFormSubmissions() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Vous pouvez ajouter une validation de formulaire ici
            console.log('Formulaire soumis:', this.id || this.getAttribute('action'));
            
            // Pour cet exemple, nous n'empêchons pas la soumission réelle
            // mais dans une application réelle, vous pourriez vouloir valider d'abord
        });
    });
}

/**
 * Affiche un message de notification
 * @param {string} message - Le message à afficher
 * @param {string} type - Le type de message (success, error, warning)
 */
function showNotification(message, type = 'success') {
    // Créer l'élément de notification
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show`;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1050;
        min-width: 300px;
    `;
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Ajouter à la page
    document.body.appendChild(notification);
    
    // Supprimer automatiquement après 5 secondes
    setTimeout(() => {
        if (notification.parentNode) {
            notification.parentNode.removeChild(notification);
        }
    }, 5000);
}