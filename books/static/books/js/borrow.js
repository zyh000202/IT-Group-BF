// borrow.js - AJAX processing of borrowing and returning books

$(document).ready(function() {
    // Book borrowing button (on the book details page)
    $('#borrow-btn').on('click', function(e) {
        e.preventDefault();
        var bookId = $(this).data('book-id');
        var url = $(this).data('url');
        $.ajax({
            url: url,
            type: 'POST',
            headers: {'X-CSRFToken': csrftoken},  // csrftoken is defined in the template
            success: function(response) {
                $('#borrow-message').html('<div class="alert alert-success">' + response.message + '</div>');
                $('#borrow-btn').prop('disabled', true).text('Borrowed');
                $('#available-copies').text(response.available);
            },
            error: function(xhr) {
                var msg = xhr.responseJSON ? xhr.responseJSON.message : 'Operation failed';
                $('#borrow-message').html('<div class="alert alert-danger">' + msg + '</div>');
            }
        });
    });

    // Return button (on My Borrowing page)
    $('.return-btn').on('click', function(e) {
        e.preventDefault();
        var btn = $(this);
        var recordId = btn.data('record-id');
        var url = btn.data('url');
        $.ajax({
            url: url,
            type: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            success: function(response) {
                $('#record-' + recordId).remove();  // Remove Current Row
                $('#return-message').html('<div class="alert alert-success">Return succeeded</div>');
            },
            error: function() {
                alert('Return failed, please try again later');
            }
        });
    });
});