// TaskFlow Main Logic

document.addEventListener('DOMContentLoaded', () => {
    'use strict'

    // Bootstrap Form Validation
    const forms = document.querySelectorAll('.needs-validation')
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }
            form.classList.add('was-validated')
        }, false)
    })

    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert')
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert)
            bsAlert.close()
        }, 5000)
    })
});

// Helper for Task Animations on Load
window.onload = () => {
    const taskContainer = document.getElementById('taskContainer');
    if (taskContainer) {
        taskContainer.classList.add('ready');
    }
};
