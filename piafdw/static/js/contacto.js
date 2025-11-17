// Espera a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', () => {

    // Seleccionar el formulario
    const contactForm = document.getElementById('contactForm');
    
    // Si no existe el formulario en la página actual, no hacer nada
    if (!contactForm) {
        return;
    }

    // Seleccionar los campos usando los IDs que Django genera
    const nameField = document.getElementById('id_nombre');
    const emailField = document.getElementById('id_email');
    const subjectField = document.getElementById('id_asunto');
    const messageField = document.getElementById('id_mensaje');

    // Seleccionar los elementos de mensaje de error (definidos en el HTML)
    const nameError = document.getElementById('name-error');
    const emailError = document.getElementById('email-error');
    const subjectError = document.getElementById('asunto-error');
    const messageError = document.getElementById('message-error');

    // Patrón de Regex simple para validar email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Función para mostrar errores
    function showError(field, errorElement, message) {
        if (field) field.classList.add('error'); // 'error' aplica el borde rojo
        if (errorElement) errorElement.textContent = message;
    }

    // Función para limpiar errores
    function clearError(field, errorElement) {
        if (field) field.classList.remove('error');
        if (errorElement) errorElement.textContent = '';
    }

    // Función principal de validación
    function validateForm() {
        let isValid = true;

        // 1. Validar Nombre
        if (nameField.value.trim() === '') {
            showError(nameField, nameError, 'El nombre es obligatorio.');
            isValid = false;
        } else {
            clearError(nameField, nameError);
        }

        // 2. Validar Email
        if (emailField.value.trim() === '') {
            showError(emailField, emailError, 'El correo electrónico es obligatorio.');
            isValid = false;
        } else if (!emailRegex.test(emailField.value.trim())) {
            showError(emailField, emailError, 'El formato del correo no es válido.');
            isValid = false;
        } else {
            clearError(emailField, emailError);
        }
        
        // 3. Validar Asunto
        if (subjectField.value.trim() === '') {
            showError(subjectField, subjectError, 'El asunto es obligatorio.');
            isValid = false;
        } else {
            clearError(subjectField, subjectError);
        }

        // 4. Validar Mensaje
        if (messageField.value.trim() === '') {
            showError(messageField, messageError, 'El mensaje no puede estar vacío.');
            isValid = false;
        } else {
            clearError(messageField, messageError);
        }

        return isValid;
    }

    // Escuchar el evento 'submit' del formulario
    contactForm.addEventListener('submit', (event) => {
        // Prevenir el envío si la validación (JS) falla
        if (!validateForm()) {
            event.preventDefault();
        }
    });

    // Validación en tiempo real al salir del campo (on blur)
    
    nameField.addEventListener('blur', () => {
        if (nameField.value.trim() === '') {
            showError(nameField, nameError, 'El nombre es obligatorio.');
        } else {
            clearError(nameField, nameError);
        }
    });

    emailField.addEventListener('blur', () => {
        if (emailField.value.trim() === '') {
            showError(emailField, emailError, 'El correo electrónico es obligatorio.');
        } else if (!emailRegex.test(emailField.value.trim())) {
            showError(emailField, emailError, 'El formato del correo no es válido.');
        } else {
            clearError(emailField, emailError);
        }
    });
    
    subjectField.addEventListener('blur', () => {
        if (subjectField.value.trim() === '') {
            showError(subjectField, subjectError, 'El asunto es obligatorio.');
        } else {
            clearError(subjectField, subjectError);
        }
    });

    messageField.addEventListener('blur', () => {
        if (messageField.value.trim() === '') {
            showError(messageField, messageError, 'El mensaje no puede estar vacío.');
        } else {
            clearError(messageField, messageError);
        }
    });

});