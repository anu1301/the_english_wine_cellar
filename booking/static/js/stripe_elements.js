/*
    Core logic/payment flow comes from:
    https://stripe.com/docs/payments/accept-a-payment

    CSS comes from: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {
    style: style
});
card.mount('#card_element');

// Handles realtime validation errors on card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card_errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handles submission of form
var form = document.getElementById('payment_form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    // Prevents multiple submissions
    card.update({
        'disabled': true
    });
    $('#submit-button').attr('disabled', true);
    // Triggers the overlay and spinner icon and fades
    $('#booking-form').fadeToggle(100);
    $('#loading-over').fadeToggle(100);


    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/booking/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                }
            },
    }).then(function (result) {
        if (result.error) {
            var errorDiv = document.getElementById('card_errors');
            var html = `
            <span class="icon" role="alert">
            <i class="fas fa-times"></i>
            </span>
            <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $('#payment_form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            card.update({
                'disabled': false
            });
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
}).fail(function() {
        // Reloads the page - the error will be in django messages
        location.reload();
    });
});
