// borrow.js - Handles AJAX borrow/return operations
$(document).ready(function() {
    console.log('Borrow.js loaded');

    // Get CSRF token from meta tag
    var csrftoken = $('meta[name="csrf-token"]').attr('content');
    console.log('CSRF Token from meta:', csrftoken);

    // If meta tag not found, try to get from cookie (fallback)
    if (!csrftoken) {
        csrftoken = getCookie('csrftoken');
        console.log('CSRF Token from cookie:', csrftoken);
    }

    // Borrow button (detail page)
    $('#borrow-btn').on('click', function(e) {
        e.preventDefault();
        console.log('Borrow button clicked');
        var btn = $(this);
        var url = btn.data('url');
        $.ajax({
            url: url,
            type: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            success: function(response) {
                console.log('Borrow success:', response);
                $('#borrow-message').html('<div class="alert alert-success">' + response.message + '</div>');
                btn.prop('disabled', true).text('Borrowed');
                $('#available-copies').text(response.available);
            },
            error: function(xhr, status, error) {
                console.error('Borrow error:', status, error, xhr.responseText);
                var msg = xhr.responseJSON ? xhr.responseJSON.message : 'Operation failed';
                $('#borrow-message').html('<div class="alert alert-danger">' + msg + '</div>');
            }
        });
    });

    // Return button (my borrows page) - event delegation
    $(document).on('click', '.return-btn', function(e) {
        e.preventDefault();
        console.log('Return button clicked');
        var btn = $(this);
        var recordId = btn.data('record-id');
        var url = btn.data('url');
        console.log('Return URL:', url);
        $.ajax({
            url: url,
            type: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            success: function(response) {
                console.log('Return success:', response);
                $('#record-' + recordId).remove(); // Remove the table row
                $('#return-message').html('<div class="alert alert-success">' + response.message + '</div>');
            },
            error: function(xhr, status, error) {
                console.error('Return error:', status, error, xhr.responseText);
                var msg = xhr.responseJSON ? xhr.responseJSON.message : 'Return failed';
                $('#return-message').html('<div class="alert alert-danger">' + msg + '</div>');
            }
        });
    });

    // Helper function to get CSRF token from cookie
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});